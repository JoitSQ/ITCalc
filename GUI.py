import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self, window):
        from functions import F
        self.func = F(self)

        self.title = 'CCalc Revamped'
        self.versionindex = 'A'
        self.version = '0.1.6'

        self.win = window
        self.win.title(f'{self.title} {self.versionindex}{self.version}')
        self.win.geometry('500x500')
        self.win.resizable(False, False)

        self.allFrame = tk.Frame(self.win)
        self.bFrame1 = tk.Frame(self.allFrame)
        self.bFrame2 = tk.Frame(self.allFrame)
        self.bFrame3 = tk.Frame(self.allFrame)
        self.bFrame4 = tk.Frame(self.allFrame)
        self.bFrame5 = tk.Frame(self.allFrame)
        self.bFrame6 = tk.Frame(self.allFrame)

        self.A = ttk.Button(self.bFrame1, text='A', width=6, state='disabled')
        self.Float = ttk.Button(self.bFrame1, width=6, text=',', state='disabled')
        self.b0 = ttk.Button(self.bFrame1, width=6, text='0', state='disabled')
        self.Cc = ttk.Button(self.bFrame1, command=lambda:self.func.changesystems(), width=6, text='Cc')
        self.Equal = ttk.Button(self.bFrame1, width=6, text='=', state='disabled')

        self.B = ttk.Button(self.bFrame2, text="B", width=6, state='disabled')
        self.b1 = ttk.Button(self.bFrame2, text="1", width=6, state='disabled')
        self.b2 = ttk.Button(self.bFrame2, text="2", width=6, state='disabled')
        self.b3 = ttk.Button(self.bFrame2, text="3", width=6, state='disabled')
        self.Plus = ttk.Button(self.bFrame2, text="+", width=6, state='disabled')

        self.C = ttk.Button(self.bFrame3, text="C",  width=6, state='disabled')
        self.b4 = ttk.Button(self.bFrame3, text="4", width=6, state='disabled')
        self.b5 = ttk.Button(self.bFrame3, text="5", width=6, state='disabled')
        self.b6 = ttk.Button(self.bFrame3, text="6", width=6, state='disabled')
        self.Minus = ttk.Button(self.bFrame3, text="-", width=6, state='disabled')

        self.D = ttk.Button(self.bFrame4, text="D",  width=6, state='disabled')
        self.b7 = ttk.Button(self.bFrame4, text="7",width=6, state='disabled')
        self.b8 = ttk.Button(self.bFrame4, text="8",width=6, state='disabled')
        self.b9 = ttk.Button(self.bFrame4, text="9",width=6, state='disabled')
        self.Multiply = ttk.Button(self.bFrame4, text="*", command=self.func.test, width=6, state='disabled')

        self.E = ttk.Button(self.bFrame5, text="E", width=6, state='disabled')
        self.BracketO = ttk.Button(self.bFrame5, text="(", width=6, state='disabled')
        self.BracketC = ttk.Button(self.bFrame5, text=")", width=6, state='disabled')
        self.Division = ttk.Button(self.bFrame5, text="/", width=6, state='disabled')
        self.Backspace = ttk.Button(self.bFrame5, text="←", width=6, state='disabled')

        self.F = ttk.Button(self.bFrame6, text="F", width=6, state='disabled')
        self.AC = ttk.Button(self.bFrame6, text="AC", width=6, state='disabled')

        self.A.pack(side='left', ipady=10)
        self.Float.pack(side='left', ipady=10)
        self.b0.pack(side='left', ipady=10)
        self.Equal.pack(side='right', ipady=10)
        self.Cc.pack(side='right', ipady=10)

        self.B.pack(side='left', ipady=10)
        self.b1.pack(side='left', ipady=10)
        self.b2.pack(side='left', ipady=10)
        self.Plus.pack(side='right', ipady=10)
        self.b3.pack(side='right', ipady=10)

        self.C.pack(side='left', ipady=10)
        self.b4.pack(side='left', ipady=10)
        self.b5.pack(side='left', ipady=10)
        self.Minus.pack(side='right', ipady=10)
        self.b6.pack(side='right', ipady=10)

        self.D.pack(side='left', ipady=10)
        self.b7.pack(side='left', ipady=10)
        self.b8.pack(side='left', ipady=10)
        self.Multiply.pack(side='right', ipady=10)
        self.b9.pack(side='right', ipady=10)

        self.E.pack(side='left', ipady=10)
        self.BracketO.pack(side='left', ipady=10)
        self.BracketC.pack(side='left', ipady=10)
        self.Backspace.pack(side='right', ipady=10)
        self.Division.pack(side='right', ipady=10)

        self.F.pack(side='left', ipady=10, padx=69)
        self.AC.pack(side='right', ipady=10, padx=69, pady=0)

        self.number = tk.Label(self.win, text=self.func.yournumber, font=("Arial", 11))
        self.number.pack(side='top', anchor='nw', pady=25, padx=25)

        self.bFrame6.pack(padx=25)
        self.bFrame5.pack(padx=25)
        self.bFrame4.pack(padx=25)
        self.bFrame3.pack(padx=25)
        self.bFrame2.pack(padx=25)
        self.bFrame1.pack(padx=25)
        self.allFrame.pack(side='left', anchor='sw', pady=0, padx=5)

    def Numberupdater(self):
        self.func.displayassistant()
        self.number.configure(text=f'{self.func.yournumberdisplay} = {str(self.func.result)}')
        self.win.after(10, self.Numberupdater)