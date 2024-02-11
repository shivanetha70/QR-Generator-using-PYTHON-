import pyqrcode
import png
from tkinter import *

def qr_gen():
    code=inp.get()
    qr=pyqrcode.create(str(code))
    qr.png('code.png',scale=10)


gui=Tk()
gui.title("QR GENERATOR")
gui.geometry('400x300')
gui.resizable(0,0)


inp=StringVar()
lab=Label(text="Enter code to generate ",width='30',height='2').pack(pady=10)
ent=Entry(textvariable=inp,width='30').pack()
btn=Button(text='Generate',command=qr_gen,width='15',height='2',bg='grey').pack(pady=10)


gui.mainloop()