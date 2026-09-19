from math import *
from tkinter import messagebox

class F():
    def __init__(self):
        pass

    def test(self):
        messagebox.showinfo("", "THE WORLD IS YOUR CANVAS")
        messagebox.showinfo("", "SO TAKE UP YOUR BRUSH")
        messagebox.showinfo("", "AND PAINT")
        messagebox.showinfo("", "THE WORLD")
        messagebox.showerror('', 'RED.')

    def ButtonFunction(self):
        b0['command'] = addup0
        b1['command'] = addup1
        b2['command'] = addup2
        b3['command'] = addup3
        b4['command'] = addup4
        b5['command'] = addup5
        b6['command'] = addup6
        b7['command'] = addup7
        b8['command'] = addup8
        b9['command'] = addup9
        Parenthesis1['command'] = test
        Parenthesis2['command'] = test
        Division['command'] = dv
        Multiply['command'] = tm
        Minus['command'] = bmin
        Plus['command'] = bstoreplus
        Equal['command'] = equal
        b0['text'] = '0'
        Parenthesis1['text'] = '('
        Parenthesis2['text'] = ')'
        Division['text'] = '/'
        Multiply['text'] = '*'
        Minus['text'] = '-'
        Plus['text'] = '+'
        Equal['text'] = '='
        b0['state'] = DISABLED
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        A['state'] = DISABLED
        B['state'] = DISABLED
        C['state'] = DISABLED
        D['state'] = DISABLED
        E['state'] = DISABLED
        F['state'] = DISABLED
        BracketsO['state'] = DISABLED
        BracketsC['state'] = DISABLED
        Division['state'] = NORMAL
        Multiply['state'] = NORMAL
        Minus['state'] = NORMAL
        Plus['state'] = NORMAL
        Equal['state'] = NORMAL
        AC['state'] = NORMAL
        Backspace['state'] = NORMAL
