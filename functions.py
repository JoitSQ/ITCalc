from math import sqrt
from tkinter import messagebox

class F:
    def __init__(self, ui):
        self.ui = ui
        self.yournumberdisplay=''
        self.accelcheck=False
        self.distancecheck=False
        self.velcheck=False
        self.vel0check=False
        self.xcheck=False
        self.x0check=False
        self.timecheck = False
        self.xisthere=False
        self.x0isthere=False
        self.vel0isthere=False
        self.velisthere=False
        self.accelisthere=False
        self.tisthere=False
        self.result=[]
        self.displayresult=''
        self.formula=0
        self.a=[self.accelcheck, self.distancecheck, self.velcheck, self.vel0check, self.xcheck, self.x0check]

    def updater(self, parser):
        if parser=='a':
            self.accelcheck=True if not self.accelcheck else False
        if parser=='x0':
            self.x0check=True if not self.x0check else False
        if parser=='x':
            self.xcheck=True if not self.xcheck else False
        if parser=='v0':
            self.vel0check=True if not self.vel0check else False
        if parser=='v':
            self.velcheck=True if not self.velcheck else False
        if parser=='s':
            self.distancecheck=True if parser=='s' and not self.distancecheck else False
        if parser=='t':
            self.timecheck = True if not self.timecheck else False

        self.a=[self.accelcheck, self.distancecheck, self.velcheck, self.vel0check, self.xcheck, self.x0check]

    def initparser(self):
        self.result=[]
        t = ['A', 'S', 'V', 'V0', 'X', 'X0', 'T']
        self.a=[self.accelcheck, self.distancecheck, self.velcheck, self.vel0check, self.xcheck, self.x0check, self.timecheck]
        for i in range(len(self.a)):
            print(self.a[i])
            if self.a[i]:
                self.result.append(f'{t[i]} = {self.physparcer(t[i])} \n')
                print('done with', t[i])


    def test(self):
        messagebox.showinfo("huh", 'get your ass outta here im still testing yk')

    def varcheck(self):
        self.vel0isthere=True if self.ui.vel0.get()!='' else False
        self.velisthere=True if self.ui.vel.get()!='' else False
        self.tisthere=True if self.ui.t.get()!='' else False
        self.xisthere=True if self.ui.x.get()!='' else False
        self.x0isthere=True if self.ui.x0.get()!='' else False
        self.accelisthere=True if self.ui.accel.get()!='' else False


    def physparcer(self, index):
        self.varcheck()
        x = int(self.ui.x.get()) if self.xisthere else 0
        x0 = int(self.ui.x0.get()) if self.x0isthere else 0
        vel0 = int(self.ui.vel0.get()) if self.vel0isthere else 0
        vel = int(self.ui.vel.get()) if self.velisthere else 0
        t = int(self.ui.t.get()) if self.tisthere else 0
        accel = int(self.ui.accel.get()) if self.accelisthere else 0


        if index=='S':

            if self.xisthere and self.x0isthere:

                self.formula = x - x0

            if self.accelisthere:

                self.formula = (vel0 * t
                                + (accel * t**2)
                                / 2)
            if self.accelisthere and self.velisthere and self.tisthere:
                self.formula = vel*t - ((accel*t**2) / 2)

            if self.velisthere and self.vel0isthere and self.tisthere:
                self.formula = (vel0+vel)*t / 2

            if not self.accelisthere:

                self.formula = vel0 * t

        if index=='V0':

            if not self.accelisthere and self.xisthere and self.x0isthere and self.tisthere:
                self.formula = ((x - x0)
                                / t)

                # Velocity = (x - x0) / time

            if self.accelisthere and self.velisthere and self.tisthere:
                self.formula = (vel -
                                (accel * t))

                # Velocity = Velocity - (Acceleration * time)

            if not self.accelisthere and self.velisthere:
                self.formula = vel

            if self.accelisthere and self.velisthere and self.xisthere and self.x0isthere:
                self.formula = sqrt(vel**2 - 2*accel*(x-x0))

            if not self.accelisthere and (self.velisthere or self.vel0isthere):
                if self.vel0isthere:
                    self.formula = vel0
                if self.velisthere:
                    self.formula = vel
                # Velocity - const

        if index=='V':
            if self.xisthere and self.x0isthere and self.tisthere and not self.accelisthere:
                self.formula = ((x - x0)
                                / t)

                # Velocity = (x - x0) / time

            if self.accelisthere:
                self.formula = (vel0 +
                                (accel * t))

                # Velocity = Velocity + (Acceleration * time)

            if self.accelisthere and self.vel0isthere and self.xisthere and self.x0isthere:
                self.formula = sqrt(vel0**2 + 2*accel*(x-x0))

            if not self.accelisthere and (self.velisthere or self.vel0isthere):
                if self.vel0isthere:
                    self.formula = vel0
                if self.velisthere:
                    self.formula = vel

                # Velocity - const

        if index=='A':
            if self.tisthere and self.vel0isthere and self.velisthere:
                self.formula = (
                        (vel - vel0)
                        /
                        t)

            if self.tisthere and self.xisthere and self.vel0isthere and self.x0isthere:
                self.formula = 2*((x-x0) - vel0*t) / t**2


            if self.tisthere and self.xisthere and self.velisthere and self.x0isthere:
                self.formula = 2 * (vel*t - (x - x0)) / t ** 2

        if index=='X':
            if self.vel0isthere and self.accelisthere and self.tisthere:
                self.formula = x0 + vel0*t + accel*t**2/2

            if self.tisthere and self.x0isthere and (self.vel0isthere or self.velisthere) and not self.accelisthere:
                if self.vel0isthere:
                    self.formula = x0 + vel0*t
                if self.velisthere:
                    self.formula = x0 + vel*t

        if index=='X0':
            if self.xisthere and self.vel0isthere and self.tisthere and self.accelisthere:
                self.formula = x - vel0*t - accel*t**2/2
            if self.tisthere and self.x0isthere and (self.vel0isthere or self.velisthere) and not self.accelisthere:
                if self.vel0isthere:
                    self.formula = x - vel0*t
                if self.velisthere:
                    self.formula = x - vel*t

        if index=='T':
            if self.accelisthere and self.velisthere and self.vel0isthere:
                self.formula = (vel - vel0)/accel

            if self.xisthere and self.x0isthere and self.velisthere and not self.accelisthere:
                self.formula = (x - x0) / vel

            if self.vel0isthere and self.accelisthere and self.x0isthere and self.xisthere:
                self.formula = (-vel0 + sqrt(vel0**2 + 2*accel*(x-x0))) / accel
                if self.formula<0:
                    self.formula = (-vel0 - sqrt(vel0 ** 2 + 2 * accel * (x - x0))) / accel
            if self.velisthere and self.accelisthere and self.x0isthere and self.xisthere:
                self.formula = (vel + sqrt(vel**2 + 2*accel*(x-x0))) / accel
                if self.formula<0:
                    self.formula = (vel - sqrt(vel ** 2 - 2 * accel * (x - x0))) / accel

        return self.formula






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

    def bracketo(self):
        self.nextnum('bo')

    def bracketc(self):
        self.nextnum('bc')

    def equal(self):
        tempnum=[0]
        c=0
        chk=[]
        if 'bo' in self.yournumber:
            self.Bracket = True
        else:
            self.Bracket = False
        if not self.Bracket:
            for i in self.yournumber:
                if i not in self.op and not self.Bracket:
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
        self.displayresult=''
        for i in self.result:
            self.displayresult+=i

    def ac(self):
        self.yournumber=['']
        self.result=0
        self.currnumber=0
        self.Bracket=False
        self.eq=False

    def nextnum(self, operation):
        self.yournumber.append(operation)
        self.yournumber.append('')
        self.currnumber+=2

    def floatf(self):
        self.addup('.')