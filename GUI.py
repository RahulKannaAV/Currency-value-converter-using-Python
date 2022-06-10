from tkinter import *
from Currencyvalue import One_USD
from tkinter import messagebox
from tkinter import font as fk
h = Tk()
h.title('Real Time Currency Converter')

val = StringVar()
exp = StringVar()
fro = StringVar()

cb = OptionMenu(h,val, *One_USD.keys())
val_entry = Entry(h, textvariable=fro, width=40, font=('Helvetica','20'))
ce = OptionMenu(h,exp, *One_USD.keys())
cb.config(width=40, font=fk.Font(family = 'Helvetica', size=20))
ce.config(width=40, font=fk.Font(family = 'Helvetica', size=20))

def value():
    if val.get() == exp.get() and val.get() != '' and exp.get() != '':
        in_usd = round(float(fro.get())/(float(One_USD[val.get()])),2)
        messagebox.showinfo(message=f"Both values are same and {fro.get()} {val.get()} = {in_usd} USD", title='Same Values')
    elif val.get()=='' or exp.get()=='' or (val.get()=='' and exp.get()=='') or fro.get()=='':
        messagebox.showwarning(message=f"One of the fields is Empty. Try Again", title='Empty Field')

    else:
        in_usd = round(float(fro.get()) / (float(One_USD[val.get()])), 2)
        result = round(in_usd * float(One_USD[exp.get()]),2)
        Res = Label(h, text=f"{float(fro.get())} {val.get()} = {result} {exp.get()}")
        Res.config(width=40, font=fk.Font(family = 'Helvetica', size=20))
        Res.pack()

sub = Button(text='Submit',command=value)

exit = Button(text='Quit', command= lambda:quit())

cb.pack()
val_entry.pack()
ce.pack()
sub.pack()
exit.pack()



h.mainloop()