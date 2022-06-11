from tkinter import *

window=Tk()
window.title("first program")
window.minsize(width=100,height=100)

window.config(padx=10,pady=10)

def button_click():
    km=int(input.get())
    mile.config(text=f"Miles is equal to {km*1.6} Km")

input=Entry(width=10)
input.grid(column=0,row=0)

mile=Label(text=f"Miles is equal to 0 Km")
mile.grid(column=1,row=0)

calculate=Button(text="calculate", command=button_click)
calculate.grid(column=1,row=2)




window.mainloop()