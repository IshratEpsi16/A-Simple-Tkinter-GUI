from tkinter import *	#importing all tkinter functions from tkinter library
window=Tk()             #Starting. window is an instance of TK() class.window is a variable
def kg():
    gram=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounce=float(e1_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,gram)
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

#All display buttons
b1=Button(window,text="Kg",command=kg)
b1.grid(row=0,column=0)
b2=Button(window,text="Convert",command=kg)
b2.grid(row=0,column=2)
b3=Button(window,text="Converted Output",command=kg)
b3.grid(row=1,column=1)

#Converted results
b4=Button(window,text="Grams",command=kg)
b4.grid(row=2,column=0)
b5=Button(window,text="Pounds",command=kg)
b5.grid(row=2,column=1)
b6=Button(window,text="Ounces",command=kg)
b6.grid(row=2,column=2)

#Input
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#Output
t1=Text(window,height=3,width=20)
t1.grid(row=3,column=0)

t2=Text(window,height=3,width=20)
t2.grid(row=3,column=1)

t3=Text(window,height=3,width=20)
t3.grid(row=3,column=2)

window.mainloop()   #ending of GUI logic block

