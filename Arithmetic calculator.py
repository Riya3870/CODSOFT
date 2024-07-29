#Arithmetic calculator
from tkinter import*
window=Tk()
window.title("CALCULATOR")
window.geometry('1200x1000')

l1=Label(window,text="Number1: ")
l1.grid(row=0,column=0)
l2=Label(window,text="Number2: ")
l2.grid(row=1,column=0)

a=IntVar()
b=IntVar()

E1=Entry(window,textvariable=a,bg="pink",fg="black")
E2=Entry(window,textvariable=b,bg="pink",fg="black")
E1.grid(row=0,column=1)
E2.grid(row=1,column=1)

def calculate():
    operation=operation_var.get()
    if operation=="+":
        result=a.get()+b.get()
    elif operation=="-":
        result=a.get()-b.get()
    elif operation=="*":
        result=a.get()*b.get()
    elif operation=="/":
        if b.get()==0:
            label.config(text="cannot divide by zero.")
            return
        result=a.get()/b.get()
    elif operation=="%":
        if b.get()==0:
            label.config(text="cannot divide by zero.")
            return
        result=a.get()%b.get()
    elif operation=="**":
        result=a.get()**b.get()
    else:
        label.config(text="please select an operation.")
        return
    label.config(text=f"Result:{result}")    
        
operation_var=StringVar()
operation_var.set("+")

l3=Label(window,text="Operation:")
l3.grid(row=2,column=1)

frame=Frame(window)
frame.grid(row=2,column=3,padx=10,pady=5)

radio_add=Radiobutton(frame,text="+",variable=operation_var,value="+")
radio_add.pack(side=LEFT)

radio_subtract=Radiobutton(frame,text="-",variable=operation_var,value="-")
radio_subtract.pack(side=LEFT)

radio_multiply=Radiobutton(frame,text="*",variable=operation_var,value="*")
radio_multiply.pack(side=LEFT)

radio_divide=Radiobutton(frame,text="/",variable=operation_var,value="/")
radio_divide.pack(side=LEFT)

radio_modulus=Radiobutton(frame,text="%",variable=operation_var,value="%")
radio_modulus.pack(side=LEFT)

radio_exponent=Radiobutton(frame,text="**",variable=operation_var,value="**")
radio_exponent.pack(side=LEFT)

b1=Button(window,text="calculate",command=calculate)  
b1.grid(row=3,column=1)

label=Label(window,text="Result: ")
label.grid(row=4,column=1)

window.mainloop()
