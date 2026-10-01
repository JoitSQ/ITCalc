import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self, window):
        from functions import F
        self.func = F(self)

        self.title = 'PhysCalc'
        self.versionindex = 'B'
        self.version = '0.7.1'

        self.win = window
        self.win.title(f'{self.title} {self.versionindex}{self.version}')
        self.win.geometry('550x600')
        self.win.resizable(False, False)

        self.allFrame = tk.Frame(self.win)
        self.bFrame1 = tk.Frame(self.allFrame)
        self.bFrame2 = tk.Frame(self.allFrame)
        self.bFrame3 = tk.Frame(self.allFrame) # Title
        self.bFrame4 = tk.Frame(self.allFrame) # Inject values
        self.bFrame5 = tk.Frame(self.allFrame) # Results
        self.bFrame6 = tk.Frame(self.allFrame) # Checkboxes

        self.calculate = ttk.Button(self.bFrame5, text='Вычислить', command=self.func.initparser)

        self.tofind = ttk.Label(self.bFrame6, text='Найти:')

        self.warning = ttk.Label(self.bFrame3, text='В связи с техническими неполадками различные частные случаи не учитываются. \nВписаны исключительно формулы из моей тетради. Новых формул выведено не было.')

        self.accelcheckbox = ttk.Checkbutton(
            self.bFrame6,
            text='Ускорение (a)',
            command=lambda:self.func.updater('a')
        )
        self.velcheckbox = ttk.Checkbutton(
            self.bFrame6,
            text='Конечная скорость (V)',
            command=lambda:self.func.updater('v')
        )
        self.vel0checkbox = ttk.Checkbutton(
            self.bFrame6,
            text='Начальная скорость (V₀)',
            command=lambda:self.func.updater('v0')
        )
        self.xcheckbox = ttk.Checkbutton(
            self.bFrame6,
            text='Конечная позиция (X)',
            command=lambda:self.func.updater('x')
        )
        self.x0checkbox = ttk.Checkbutton(
            self.bFrame6,
            text='Начальна позиция (X₀)',
            command=lambda:self.func.updater('x0')
        )
        self.distancecheckbox = ttk.Checkbutton(
            self.bFrame6,
            text='Перемещение (S)',
            command=lambda:self.func.updater('s')
        )
        self.timecheckbox = ttk.Checkbutton(
            self.bFrame6,
            text='Время (t)',
            command=lambda:self.func.updater('t')
        )

        self.warning.pack(pady=25)

        self.vel0=ttk.Entry(self.bFrame4, width=25)

        self.vel=ttk.Entry(self.bFrame4, width=25)

        self.accel=ttk.Entry(self.bFrame4, width=25)

        self.x=ttk.Entry(self.bFrame4, width=25)

        self.x0=ttk.Entry(self.bFrame4, width=25)

        self.t=ttk.Entry(self.bFrame4, width=25)

        self.acceltooltip = ttk.Label(self.bFrame4, text='Ускорение (a): м/с²')
        self.veltooltip = ttk.Label(self.bFrame4, text='Конечная скорость (V): м/с')
        self.vel0tooltip = ttk.Label(self.bFrame4, text='Начальная скорость (V₀): м/с')
        self.xtooltip = ttk.Label(self.bFrame4, text='Конечная координата (X): м')
        self.x0tooltip = ttk.Label(self.bFrame4, text='Начальная координата (X₀): м')
        self.Tooltip=ttk.Label(self.bFrame4, text='Время (t): с')

        self.tofind.pack()
        self.accelcheckbox.pack(pady=5)
        self.distancecheckbox.pack(pady=5)
        self.velcheckbox.pack(pady=5)
        self.vel0checkbox.pack(pady=5)
        self.xcheckbox.pack(pady=5)
        self.x0checkbox.pack(pady=5)
        self.timecheckbox.pack(pady=5)

        self.acceltooltip.pack(anchor='sw')
        self.accel.pack(pady=5)
        self.veltooltip.pack(anchor='sw')
        self.vel.pack(pady=5)
        self.vel0tooltip.pack(anchor='sw')
        self.vel0.pack(pady=5)
        self.xtooltip.pack(anchor='sw')
        self.x.pack(pady=5)
        self.x0tooltip.pack(anchor='sw')
        self.x0.pack(pady=5)
        self.Tooltip.pack(anchor='sw')
        self.t.pack(pady=5)

        self.calculate.pack()

        self.number = tk.Label(self.bFrame5, text=self.func.a, font=("Arial", 11))
        self.number.pack(side='top', anchor='nw', pady=25, padx=25)

        self.bFrame3.pack(anchor='nw') # Title
        self.bFrame6.pack(side = 'right', anchor='ne', padx=25) # Checkboxes
        self.bFrame5.pack(side = 'bottom', anchor='s', padx=25) # Results
        self.bFrame4.pack(side = 'left', anchor='nw', padx=25) # Inject values

        self.allFrame.pack(side='left', anchor='sw', pady=0, padx=5)


    def Numberupdater(self):
        self.func.displayassistant()
#        self.number.configure(text=f'{self.func.yournumberdisplay} = {str(self.func.result)}')
        self.number.configure(text=self.func.displayresult)
        self.win.after(10, self.Numberupdater)