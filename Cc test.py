# Imports

import tkinter as tk
from functions import *
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
#Variables

win = Tk()
win.title('Calculator prototype GUI Test 0.2.0')
win.iconbitmap(default="CalculatorCc.ico")
win.geometry('283x400')

#Number Frame initialize

allframe=tk.Frame(win)
bframe1=tk.Frame(allframe)
bframe2=tk.Frame(allframe)
bframe3=tk.Frame(allframe)
bframe4=tk.Frame(allframe)
bframe5=tk.Frame(allframe)
bframe6=tk.Frame(allframe)

#Button initialize

BA = ttk.Button(bframe1, text ="", command = test)
Bflt = ttk.Button(bframe1, text ="", command = test)
B0 = ttk.Button(bframe1, text ="", command = test)
BCC = ttk.Button(bframe1, text ="", command = test)
Beq = ttk.Button(bframe1, text ="", command = equal)

BB = ttk.Button(bframe2, text ="B", command = test)
B1 = ttk.Button(bframe2, text ="1", command = addup1)
B2 = ttk.Button(bframe2, text ="2", command = addup2)
B3 = ttk.Button(bframe2, text ="3", command = addup3)
Bplus = ttk.Button(bframe2, text ="+", command = bstoreplus)

BC = ttk.Button(bframe3, text ="C", command = test)
B4 = ttk.Button(bframe3, text ="4", command = addup4)
B5 = ttk.Button(bframe3, text ="5", command = addup5)
B6 = ttk.Button(bframe3, text ="6", command = addup6)
Bmin = ttk.Button(bframe3, text ="-", command = bmin)

BD = ttk.Button(bframe4, text ="D", command = test)
B7 = ttk.Button(bframe4, text ="7", command = addup7)
B8 = ttk.Button(bframe4, text ="8", command = addup8)
B9 = ttk.Button(bframe4, text ="9", command = addup9)
BTim = ttk.Button(bframe4, text ="*", command = test)

BE = ttk.Button(bframe5, text ="E", command = test)
BSK1 = ttk.Button(bframe5, text ="(", command = test)
BSK2 = ttk.Button(bframe5, text =")", command = test)
Bdiv = ttk.Button(bframe5, text ="/", command = test)
Bbcksp = ttk.Button(bframe5, text ="←", command = backspace)

BF = ttk.Button(bframe6, text ="F", command = test)
BAC = ttk.Button(bframe6, text ="AC", command = ac)

#Buttons pack

BA.pack(side=LEFT, ipadx=15, ipady=10)
Bflt.pack(side=LEFT, ipadx=20, ipady=10)
B0.pack(side=LEFT, ipadx=18, ipady=10)
Beq.pack(side=RIGHT, ipadx=18, ipady=10)
BCC.pack(side=RIGHT, ipadx=14, ipady=10)

BB.pack(side=LEFT, ipadx=15, ipady=10)
B1.pack(side=LEFT, ipadx=18, ipady=10)
B2.pack(side=LEFT, ipadx=18, ipady=10)
Bplus.pack(side=RIGHT, ipadx=18, ipady=10)
B3.pack(side=RIGHT, ipadx=18, ipady=10)

BC.pack(side=LEFT, ipadx=15, ipady=10)
B4.pack(side=LEFT, ipadx=18, ipady=10)
B5.pack(side=LEFT, ipadx=18, ipady=10)
Bmin.pack(side=RIGHT, ipadx=20, ipady=10)
B6.pack(side=RIGHT, ipadx=18, ipady=10)

BD.pack(side=LEFT, ipadx=15, ipady=10)
B7.pack(side=LEFT, ipadx=18, ipady=10)
B8.pack(side=LEFT, ipadx=18, ipady=10)
BTim.pack(side=RIGHT, ipadx=20, ipady=10)
B9.pack(side=RIGHT, ipadx=18, ipady=10)

BE.pack(side=LEFT, ipadx=15, ipady=10)
BSK1.pack(side=LEFT, ipadx=19, ipady=10)
BSK2.pack(side=LEFT, ipadx=19, ipady=10)
Bbcksp.pack(side=RIGHT, ipadx=18, ipady=10)
Bdiv.pack(side=RIGHT, ipadx=18, ipady=10)

BF.pack(side=LEFT, ipadx=15, ipady=10)
BAC.pack(side=RIGHT, ipadx=15, ipady=10)

warn=Label(win, text='В связи с некоторыми неполадками, калькулятор, до поры до времени, работает в консоли PyCharm. Приносим извинения, мы уже работаем над этим!', font=("Arial", 12))
ver=Label(win, text='v0.2.0. GUI Update', font=("Arial", 12))


#B5.pack(anchor=CENTER, side=LEFT, padx=(10, 10)) | As example of variables
#        ↑Выравнивание  ↑Сторона        ↑отступ(Х,У)


#Frame pack

Label.pack(warn, anchor=N)
Label.pack(ver, side=BOTTOM, anchor=W)
bframe6.pack(anchor=CENTER, padx=155)
bframe5.pack(anchor=CENTER, padx=25)
bframe4.pack(anchor=CENTER, padx=25)
bframe3.pack(anchor=CENTER, padx=25)
bframe2.pack(anchor=CENTER, padx=25)
bframe1.pack(anchor=CENTER, padx=25)
allframe.pack(side=BOTTOM, fill=X, pady=25)


#есть идея
win.mainloop()
