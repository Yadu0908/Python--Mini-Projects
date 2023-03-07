
from tkinter import *

root= Tk()              #tkinter started

#these are for title and other primary properties...

root.title("Calculator")
root.iconbitmap('calculator.ico')
root.geometry('440x670')
root.config(bg="#17161b")
root.resizable(False, False)
root.wm_attributes("-transparentcolor","gray")

#first variable

equation=""


#this is show function which shows the number, operation and result


def show(value):
    global equation 
    equation=equation+value
    label_result.config(text=equation)

#this is clear function which remove the variable from screen or label


def clear():
    global equation
    equation= ""
    label_result.config(text=equation)


#this is calculate function which calculate our number 
  
  
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result= "error"
            equation= ""
        
    label_result.config(text=result)


#this is label which is used to show the output and number operation choose



label_result= Label(root, width=21, height=2, text="",
                    font=("arial",30),
                    bg="#222222",
                    fg="#FFF")
label_result.pack()


#Button............


Button(root, text="C", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold") , bg="#3697f5", command=lambda:clear()).place(x=15,y=150)

Button(root, text="/", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("/")).place(x=120,y=150)

Button(root, text="%", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("%")).place(x=225,y=150)

Button(root, text="X", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("*")).place(x=330,y=150)


Button(root, text="7", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("7")).place(x=15,y=250)

Button(root, text="8", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("8")).place(x=120,y=250)

Button(root, text="9", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("9")).place(x=225,y=250)

Button(root, text="-", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("-")).place(x=330,y=250)



Button(root, text="4", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("4")).place(x=15,y=350)

Button(root, text="5", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("5")).place(x=120,y=350)

Button(root, text="6", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("6")).place(x=225,y=350)

Button(root, text="+", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("+")).place(x=330,y=350)



Button(root, text="1", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("1")).place(x=15,y=450)

Button(root, text="2", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("2")).place(x=120,y=450)

Button(root, text="3", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("3")).place(x=225,y=450)

Button(root, text="0", width=9, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show("0")).place(x=15,y=550)



Button(root, text=".", width=4, height=1, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#2a2d36", command=lambda:show(".")).place(x=225,y=550)

Button(root, text="=", width=4, height=4, bd=0,fg="#fff", font=("arial",26,"bold"), bg="#fe9037", command=lambda:calculate()).place(x=330,y=450)


#out tkinter screen end here


root.mainloop()