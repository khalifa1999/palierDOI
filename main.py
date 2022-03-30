import tkinter as tk
from tkinter import *
import sys

root = tk.Tk()


# exit function
def get_out():
    sys.exit()


# titre root
# sf = "value is %s" % var.get()
root.title("Calcul balance")


# initial value

# This function is linked to a dropdown list
# Of operators and will be called everytime the user
def afficher(choice):
    choice = var.get()
    global ven_default
    global volume_engage
    dict_operateurs = {
        'wind': 0,
        'lyca': 1000000,
        'free': 0,
        'libon': 1000000,
        'sima': 0,
        'lebara': 0,
        'USA retail': 0,
        'reptel': 0,
        'byt': 0,
        'ofr': 864000,
        'us/canada': 0,
        'gap': 0
    }

    for x, y in dict_operateurs.items():
        if choice == x:
            # ==> for testing purposes
            # print(y)
            ven_default = IntVar(root, value=y)
            volume_engage.destroy()
            volume_engage = Entry(root, textvariable=ven_default, bg="white", font=8, width=8)
            volume_engage.grid(row=4, column=1)


var = StringVar(root)
choices = ['wind', 'lyca', 'free', 'libon', 'sima', 'lebara', 'USA retail', 'reptel', 'byt', 'ofr', 'us/canada', 'gap']
option = tk.OptionMenu(root, var, *choices, command=afficher)
var.set(choices[0])
option.grid(row=0, column=1)

# use command to call a function => select
# button = tk.Button(root, text="check value selected", command=select)


# text field
# default values
fill1 = IntVar(root, value=0)
fill2 = IntVar(root, value=0)
fill3 = IntVar(root, value=0)
ven_default = IntVar(root, value=0)

# paliers
palierI = tk.Label(root, text="Palier I", bg='orange', fg='white')
palierI.grid(row=1, column=0)

fill_palierI = tk.Entry(root, textvariable=fill1, bg="white", font=8, width=8)
fill_palierI.grid(row=2, column=0)

palierII = tk.Label(root, text="Palier II", bg='orange', fg='white')
palierII.grid(row=1, column=1)

fill_palierII = tk.Entry(root, textvariable=fill2, bg="white", font=8, width=8)
fill_palierII.grid(row=2, column=1)

palierIII = tk.Label(root, text="Palier III", bg='orange', fg='white')
palierIII.grid(row=1, column=2)

fill_palierIII = tk.Entry(root, textvariable=fill3, bg="white", font=8, width=8)
fill_palierIII.grid(row=2, column=2)

# Volumes
label_vengage = Label(root, text='Volume Engage', bg='orange')
volume_engage = Entry(root, textvariable=ven_default, bg="white", font=8, width=8)

label_vengage.grid(row=3, column=1)
volume_engage.grid(row=4, column=1)

label_vreel = Label(root, text='Volume reel', bg='orange')
volume_reel = Entry(root, bg="white", font=8, width=8)

label_vreel.grid(row=5, column=1)
volume_reel.grid(row=6, column=1)

# buttons
quitter = Button(root, text='quitter', command=get_out, bg='green', fg='white', font=6, width=5)
quitter.grid(columnspan=4, rowspan=15)

root.mainloop()
