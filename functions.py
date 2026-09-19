from math import *
from tkinter import messagebox

class F():
    def __init__(self, ui):
        self.ui = ui
        self.yournumber=['']
        self.currnumber=0

    def test(self):
        messagebox.showinfo("huh", 'get your ass outta here im still testing yk')

    def ButtonFunction(self):
        self.ui.b0['command'] = lambda:self.addup(0)
        self.ui.b1['command'] = lambda:self.addup(1)
        self.ui.b2['command'] = lambda:self.addup(2)
        self.ui.b3['command'] = lambda:self.addup(3)
        self.ui.b4['command'] = lambda:self.addup(4)
        self.ui.b5['command'] = lambda:self.addup(5)
        self.ui.b6['command'] = lambda:self.addup(6)
        self.ui.b7['command'] = lambda:self.addup(7)
        self.ui.b8['command'] = lambda:self.addup(8)
        self.ui.b9['command'] = lambda:self.addup(9)
        self.ui.BracketO['command'] = self.test
        self.ui.BracketC['command'] = self.test
        self.ui.Division['command'] = self.dv
        self.ui.Multiply['command'] = self.tm
        self.ui.Minus['command'] = self.min
        self.ui.Plus['command'] = self.plus
        self.ui.Equal['command'] = self.equal
        self.ui.b0['text'] = '0'
        self.ui.BracketO['text'] = '('
        self.ui.BracketC['text'] = ')'
        self.ui.Division['text'] = '/'
        self.ui.Multiply['text'] = '*'
        self.ui.Minus['text'] = '-'
        self.ui.Plus['text'] = '+'
        self.ui.Equal['text'] = '='
        self.ui.b0['state'] = 'normal'
        self.ui.b1['state'] = 'normal'
        self.ui.b2['state'] = 'normal'
        self.ui.b3['state'] = 'normal'
        self.ui.b4['state'] = 'normal'
        self.ui.b5['state'] = 'normal'
        self.ui.b6['state'] = 'normal'
        self.ui.b7['state'] = 'normal'
        self.ui.b8['state'] = 'normal'
        self.ui.b9['state'] = 'normal'
        self.ui.A['state'] = 'normal'
        self.ui.B['state'] = 'normal'
        self.ui.C['state'] = 'normal'
        self.ui.D['state'] = 'normal'
        self.ui.E['state'] = 'normal'
        self.ui.F['state'] = 'normal'
        self.ui.BracketO['state'] = 'normal'
        self.ui.BracketC['state'] = 'normal'
        self.ui.Division['state'] = 'normal'
        self.ui.Multiply['state'] = 'normal'
        self.ui.Minus['state'] = 'normal'
        self.ui.Plus['state'] = 'normal'
        self.ui.Equal['state'] = 'normal'
        self.ui.AC['state'] = 'normal'
        self.ui.Backspace['state'] = 'normal'

    def addup(self, numb):
        self.yournumber[self.currnumber]+=str(numb)
    def changesystems(self):
        self.ButtonFunction()
    def dv(self):
        self.nextnum()
    def tm(self):
        self.nextnum()
    def min(self):
        self.nextnum()
    def equal(self):
        self.test()
    def plus(self):
        self.nextnum()
    def ac(self):
        self.yournumber=''
    def nextnum(self):
        self.yournumber.append('')
        self.currnumber+=1