import tkinter as tk
import os
from tkinter.constants import RIGHT
import webbrowser
 
# Just a simple tkinter button gui that lets me run various python files, launch templated notepads, or scrape my clipboard for fields and copy them to my clipboard.
def abort(self):
    self.quit()
    
def run_cb_scrape():
    os.system('C:\\Users\\Timothy\\python_folder1\\.venv\\Scripts\\python_various\\cb_scraper.py')
    
def launch_webpage():
    IG_url = ('https://warframe.market/')
    webbrowser.open_new(IG_url)

def open_python_notes():
    os.startfile('C:\\Users\\Timothy\\Desktop\\Python Notes.txt')

def wframe_item_orders():
    os.system('C:\\Users\\Timothy\\python_folder1\\.venv\\Scripts\\python_various\\market_request.py')

class buttons(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Finjimen Buttons")
        self.configure(background='black')
        self.geometry('+1730+0')
        
        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack(side=RIGHT)

        self.frame = tk.Frame(self)
        self.frame.pack(side=RIGHT)

        self.button1 = tk.Button(self.btn_frame, text='Abort & Close',bd=8,background='red',font='bold',width=18,command=lambda: abort(self))
        self.button1.pack()

        self.button3 = tk.Button(self.btn_frame, text='Scrape Clipboard',bd=8,background='gray',width=18,command=lambda: run_cb_scrape(),font='bold')
        self.button3.pack()

        self.button4 = tk.Button(self.btn_frame, text='Warframe Market',bd=8,background='maroon',foreground = 'white',width=18,command=lambda: launch_webpage(),font='bold')
        self.button4.pack()

        self.button5 = tk.Button(self.btn_frame, text='HTTP Request',bd=8,background='dodgerblue',foreground = 'black',width=18,command=lambda: wframe_item_orders(),font='bold')
        self.button5.pack()

        self.button6 = tk.Button(self.btn_frame, text='Python Notes',bd=8,background='gold',foreground = 'black',width=18,command=lambda: open_python_notes(),font='bold')
        self.button6.pack()     

app = buttons()
app.mainloop()