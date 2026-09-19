from tkinter import messagebox

class F:
    def __init__(self, ui):
        self.ui = ui
        self.yournumber=['']
        self.currnumber=0
        self.op=['div', 'mul', 'add', 'min']
        self.result=0
        self.eq=False
        self.yournumberdisplay=''

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
        self.ui.A['command'] = lambda:self.addup('A')
        self.ui.B['command'] = lambda:self.addup('B')
        self.ui.C['command'] = lambda:self.addup('C')
        self.ui.D['command'] = lambda:self.addup('D')
        self.ui.E['command'] = lambda:self.addup('E')
        self.ui.F['command'] = lambda:self.addup('F')
        self.ui.BracketO['command'] = self.test
        self.ui.BracketC['command'] = self.test
        self.ui.Division['command'] = self.dv
        self.ui.Multiply['command'] = self.tm
        self.ui.Minus['command'] = self.min
        self.ui.Plus['command'] = self.plus
        self.ui.Equal['command'] = self.equal
        self.ui.Float['command'] = self.floatf
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
        self.ui.Float['state'] = 'normal'

    def addup(self, numb):
        if self.eq:
            self.yournumber=['']
            self.currnumber=0
            self.result=0
            self.eq=False

        self.yournumber[self.currnumber]+=str(numb)
    def changesystems(self):
        self.ButtonFunction()

    def dv(self):
        self.nextnum('div')

    def tm(self):
        self.nextnum('mul')

    def min(self):
        self.nextnum('min')

    def plus(self):
        self.nextnum('add')

    def equal(self):
        tempnum=[0]
        c=0
        chk=[]
        for i in self.yournumber:
            if i not in self.op:
                tempnum[c]+=float(i)
            else:
                if i=='div':
                    chk.append(5)
                    tempnum.append(0)
                    c+=1
                if i=='min':
                    chk.append(1)
                    tempnum.append(0)
                    c+=1
                if i=='add':
                    chk.append(2)
                    tempnum.append(0)
                    c+=1
                if i=='mul':
                    chk.append(4)
                    tempnum.append(0)
                    c+=1
        self.result=tempnum[0]
        for i in range(len(tempnum)-1):
            if chk[i]==5:
                self.result/=tempnum[i+1]
            if chk[i]==1:
                self.result-=tempnum[i+1]
            if chk[i]==2:
                self.result+=tempnum[i+1]
            if chk[i]==4:
                self.result*=tempnum[i+1]
        self.eq=True
        self.displayassistant()
        #self.result=0

    def displayassistant(self):
        self.yournumberdisplay=''
        for i in self.yournumber:
            if i not in self.op:
                self.yournumberdisplay+=i
            if i=='div':
                self.yournumberdisplay+=' / '
            if i=='min':
                self.yournumberdisplay+=' - '
            if i=='add':
                self.yournumberdisplay+=' + '
            if i=='mul':
                self.yournumberdisplay+=' * '
        if self.result==int(self.result):
            self.result=int(self.result)

    def ac(self):
        self.yournumber=['']
        self.result=0
        self.currnumber=0
        self.eq=False

    def nextnum(self, operation):
        self.yournumber.append(operation)
        self.yournumber.append('')
        self.currnumber+=2

    def floatf(self):
        self.addup('.')