#!/bin/python
import urllib2
from beautifulsoup.beautifulsoup import BeautifulSoup 
from Tkinter import *
import Tix as tk
from tkinter.ttk import Progressbar, Style

print '''
[][][*] c0ded by Ajith Kp (ajithkp560) [http://www.terminalcoders.blogspot.com]
[][][*] HTML Parser: BeautifulSoup
[][][*] GUI: tk
[][][*] If tk is not installed run $ sudo apt-get install python-tk
[][][*] Grab the URL to input by right click on video and click 'Copy Video URL at current time'
'''


class GUI:
    def __init__(self,v):
        self.main=v
        self.t = StringVar()
        self.t.set(":.: Facebook Video Download Tool :.:")
        self.label=Label(v, textvariable=self.t, font='Helvetica -14 bold', bg='#3b5998', fg='#fcfcfc')
        self.label.config(highlightbackground='#fcfcfc')
        self.label.pack(padx=10, pady=10)
        
        self.entry = Entry(v, width=65, bg='#3b5998', fg='#fcfcfc')
        self.entry.config(highlightbackground='#fcfcfc')
        self.entry.pack(padx=10, pady=10)
        
        self.button=Button(v, text="Download",command=self.pressButton, bg="#3b5998", fg="#fcfcfc")
        self.button.config(highlightbackground='#fcfcfc')
        self.button.pack(padx=10, pady=10)
        
        
        self.n = 0
    def pressButton(self):
        link = self.entry.get()
        try:
            res = urllib2.urlopen(link)
            html = res.read().decode("iso-8859-1")
            soup = BeautifulSoup(html)
            tag = soup.find('meta',  property='og:video')#soup.body.find('meta', attrs={'property' : 'og:video:url'}).text
            vid_url = tag['content']
            file_name = vid_url.split('/')[-1].split('?')[0]#vid_url[vid_url.rfind("/")+1:]
            
            s = Style()
            s.theme_use("classic")   
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            self.progress = Progressbar(self.main, style="green.Horizontal.TProgressbar", orient = HORIZONTAL, length = 100, mode = 'determinate')
            self.progress.pack(pady = 10) 
            
            nhandler = urllib2.urlopen(vid_url)
            vid_file = open(file_name, 'wb')
            meta = nhandler.info()
            filesize = int (meta.getheaders ("Content-Length")[0])  
            filesizedown = 0
            blocksize = 10000
            self.message=Label(w, text='Download: %d / %d'%(filesizedown, filesize), font='Helvetica -13 bold', fg='#fcfcfc', bg='#3b5998')            
            self.message.pack(padx=10, pady=10)
            while True:
                buffer = nhandler.read(blocksize)
                if not buffer:
                    break
                filesizedown += len(buffer)
                vid_file.write(buffer)
                percent = filesizedown * 100. / filesize
                self.progress['value'] = percent
                self.main.update_idletasks() 
                self.message['text'] = 'Download: %d / %d'%(filesizedown, filesize)
            self.message['text']='Download Completed'
            self.message['fg']='#ccffcc'
        except Exception, e:
            self.label=Label(w, text="Error: %s"%(e), font='Helvetica -13 bold', fg='#fcfcfc', bg='#3b5998')
            self.label.pack()
w=Tk()
w.configure(background='#3b5998')
w.title("Facebook Video Downloader by Ajith Kp")
w.minsize(300,200)
gui=GUI(w)
w.mainloop()
