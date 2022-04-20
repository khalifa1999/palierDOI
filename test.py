from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import sys


# exit function
def get_out():
    sys.exit()


class Widget1:
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg='#fff5cc')
            self.w1.geometry('570x560')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg='#ffb218')
            self.w1.place(x=0, y=0, width=570, height=560)
        # text field
        # default values variables
        Vfill1 = IntVar(self.w1, value=0)
        Vfill2 = IntVar(self.w1, value=0)
        fill1 = IntVar(self.w1, value=0)
        fill2 = IntVar(self.w1, value=0)
        fill3 = IntVar(self.w1, value=0)
        ven_default = IntVar(self.w1, value=0)
        vreel_default = IntVar(self.w1, value=0)
        tarif_normaldefault = IntVar(self.w1, value=0)
        # Scroll list
        self.combo1 = Combobox(self.w1, font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow",
                               state="normal")
        self.combo1.place(x=190, y=30, width=180, height=22)
        # Volume palier label
        self.VpalierI = Label(self.w1, text="Palier 1 volume", bg="#fff5cc", fg="#000000",
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.VpalierI.place(x=150, y=100, width=90, height=22)
        self.VpalierII = Label(self.w1, text="Palier 2 volume", bg="#fff5cc", fg="#000000",
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.VpalierII.place(x=340, y=100, width=90, height=22)

        self.Vfill_palierI = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=Vfill1,
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.Vfill_palierI.place(x=137, y=130, width=110, height=22)
        self.Vfill_palierII = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=Vfill2,
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.Vfill_palierII.place(x=332, y=130, width=110, height=22)
        # Label for rate and the rates
        self.palierI = Label(self.w1, text="Tarif Palier 1", bg="#fff5cc", fg="#000000",
                             font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.palierI.place(x=50, y=220, width=90, height=22)

        self.palierII = Label(self.w1, text="Tarif Palier 2", bg="#fff5cc", fg="#000000",
                             font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.palierII.place(x=240, y=220, width=90, height=22)

        self.palierIII = Label(self.w1, text="Tarif Palier 3", bg="#fff5cc", fg="#000000",
                             font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.palierIII.place(x=430, y=220, width=90, height=22)

        self.fill_palierI = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=fill1,
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.fill_palierI.place(x=35, y=250, width=110, height=22)

        self.fill_palierII = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=fill2,
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.fill_palierII.place(x=225, y=250, width=110, height=22)

        self.fill_palierIII = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=fill3,
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.fill_palierIII.place(x=425, y=250, width=110, height=22)
        # Reel volume and engaged
        self.label_vengage = Label(self.w1, text="Volume engagé", bg="#fff5cc", fg="#4d3d00",
                              font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.label_vengage.place(x=240, y=330, width=90, height=22)

        self.label_vreel = Label(self.w1, text="Volume reel", bg="#fff5cc", fg="#000000",
                            font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.label_vreel.place(x=50, y=330, width=90, height=22)
        self.volume_engage = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=ven_default,
                             font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.volume_engage.place(x=225, y=360, width=110, height=22)

        self.label_vreel = Entry(self.w1, bg="#00e64d", fg="#4d3d00", textvariable=vreel_default,font=tkinter.font.Font(family="MS Shell Dlg 2", size=8),
                           cursor="arrow", state="normal")
        self.label_vreel.place(x=35, y=360, width=110, height=22)

        # Upload button
        self.upload = Button(self.w1, text="Upload", bg="#ffdb4d",
                             font=tkinter.font.Font(family="MS Shell Dlg 2", size=8), cursor="arrow", state="normal")
        self.upload.place(x=425, y=360, width=60, height=22)
        # Exit button
        self.button1 = Button(self.w1, text="Quitter", bg="#ffdb4d", command=get_out,
                              font=tkinter.font.Font(family="MS Shell Dlg 2", size=8),
                              cursor="arrow", state="normal")
        self.button1.place(x=240, y=470, width=90, height=22)


a = Widget1(0)
a.w1.mainloop()
