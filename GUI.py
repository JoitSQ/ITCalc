import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self):
        allFrame = tk.Frame(win)
        bFrame1 = tk.Frame(allFrame)
        bFrame2 = tk.Frame(allFrame)
        bFrame3 = tk.Frame(allFrame)
        bFrame4 = tk.Frame(allFrame)
        bFrame5 = tk.Frame(allFrame)
        bFrame6 = tk.Frame(allFrame)

        # Button initialize
        bA = ttk.Button(bFrame1, text="A", command=testaddupA, width=6, state=DISABLED)
        bFloat = ttk.Button(bFrame1, text=",", command=floatb, width=6, state=DISABLED)
        b0 = ttk.Button(bFrame1, text="0", command=addup0, width=6, state=DISABLED)
        bCc = ttk.Button(bFrame1, text="Сс", command=Cc, width=6)
        bEqual = ttk.Button(bFrame1, text="=", command=equal, width=6, state=DISABLED)

        bB = ttk.Button(bFrame2, text="B", command=testaddupB, width=6, state=DISABLED)
        b1 = ttk.Button(bFrame2, text="1", command=addup1, width=6, state=DISABLED)
        b2 = ttk.Button(bFrame2, text="2", command=addup2, width=6, state=DISABLED)
        b3 = ttk.Button(bFrame2, text="3", command=addup3, width=6, state=DISABLED)
        bPlus = ttk.Button(bFrame2, text="+", command=bstoreplus, width=6, state=DISABLED)

        bC = ttk.Button(bFrame3, text="C", command=testaddupC, width=6, state=DISABLED)
        b4 = ttk.Button(bFrame3, text="4", command=addup4, width=6, state=DISABLED)
        b5 = ttk.Button(bFrame3, text="5", command=addup5, width=6, state=DISABLED)
        b6 = ttk.Button(bFrame3, text="6", command=addup6, width=6, state=DISABLED)
        bMinus = ttk.Button(bFrame3, text="-", command=bmin, width=6, state=DISABLED)

        bD = ttk.Button(bFrame4, text="D", command=testaddupD, width=6, state=DISABLED)
        b7 = ttk.Button(bFrame4, text="7", command=addup7, width=6, state=DISABLED)
        b8 = ttk.Button(bFrame4, text="8", command=addup8, width=6, state=DISABLED)
        b9 = ttk.Button(bFrame4, text="9", command=addup9, width=6, state=DISABLED)
        bMultiply = ttk.Button(bFrame4, text="*", command=tm, width=6, state=DISABLED)

        bE = ttk.Button(bFrame5, text="E", command=testaddupE, width=6, state=DISABLED)
        bParenthesis1 = ttk.Button(bFrame5, text="(", command=test, width=6, state=DISABLED)
        bParenthesis2 = ttk.Button(bFrame5, text=")", command=test, width=6, state=DISABLED)
        bDivision = ttk.Button(bFrame5, text="/", command=dv, width=6, state=DISABLED)
        bBackspace = ttk.Button(bFrame5, text="←", command=backspace, width=6, state=DISABLED)

        bF = ttk.Button(bFrame6, text="F", command=testaddupF, width=6, state=DISABLED)
        bAC = ttk.Button(bFrame6, text="AC", command=ac, width=6, state=DISABLED)

        # Button pack

        bA.pack(side=LEFT, ipady=10)
        bFloat.pack(side=LEFT, ipady=10)
        b0.pack(side=LEFT, ipady=10)
        bEqual.pack(side=RIGHT, ipady=10)
        bCc.pack(side=RIGHT, ipady=10)

        bB.pack(side=LEFT, ipady=10)
        b1.pack(side=LEFT, ipady=10)
        b2.pack(side=LEFT, ipady=10)
        bPlus.pack(side=RIGHT, ipady=10)
        b3.pack(side=RIGHT, ipady=10)

        bC.pack(side=LEFT, ipady=10)
        b4.pack(side=LEFT, ipady=10)
        b5.pack(side=LEFT, ipady=10)
        bMinus.pack(side=RIGHT, ipady=10)
        b6.pack(side=RIGHT, ipady=10)

        bD.pack(side=LEFT, ipady=10)
        b7.pack(side=LEFT, ipady=10)
        b8.pack(side=LEFT, ipady=10)
        bMultiply.pack(side=RIGHT, ipady=10)
        b9.pack(side=RIGHT, ipady=10)

        bE.pack(side=LEFT, ipady=10)
        bParenthesis1.pack(side=LEFT, ipady=10)
        bParenthesis2.pack(side=LEFT, ipady=10)
        bBackspace.pack(side=RIGHT, ipady=10)
        bDivision.pack(side=RIGHT, ipady=10)

        bF.pack(side=LEFT, ipady=10, padx=[0, 69])
        bAC.pack(side=RIGHT, ipady=10, padx=[69, 0])

        # Warn

        warning1 = Label(win, text='В связи с некоторыми неполадками,', font=("Arial", 11))
        warning2 = Label(win, text='калькулятор, до поры, до времени,', font=("Arial", 11))
        warning3 = Label(win, text='работает в консоли PyCharm. Приносим', font=("Arial", 11))
        warning4 = Label(win, text='извинения, мы уже работаем над этим!', font=("Arial", 11))
        version = Label(win, text='v0.5.0 Первый выпущенный прототип ', font=("Arial", 12))

        # Window frame pack

        Label.pack(warning1, anchor=N)
        Label.pack(warning2, anchor=N)
        Label.pack(warning3, anchor=N)
        Label.pack(warning4, anchor=N)
        Label.pack(version, side=BOTTOM, anchor=W)
        bFrame6.pack(padx=[25, 25])
        bFrame5.pack(padx=[25, 25])
        bFrame4.pack(padx=[25, 25])
        bFrame3.pack(padx=[25, 25])
        bFrame2.pack(padx=[25, 25])
        bFrame1.pack(padx=[25, 25])
        allFrame.pack(side=BOTTOM, pady=[0, 5])

        # Оставить и ни в коем случае не убирать :)

        win.mainloop()