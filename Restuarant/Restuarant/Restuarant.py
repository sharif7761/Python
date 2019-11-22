from tkinter import *
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restuarent")



Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#==================time===================
localtime=time.asctime(time.localtime(time.time()))
#==================info===================
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Restuarant Management System",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',15,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==================Calculator===================
text_input=StringVar()
operator=""
 
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set(operator)

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
     

txtDisplay=Entry(f2,font=('arial',15,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify='right')
txtDisplay.grid(columnspan=4)


btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)
#------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)

#------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)


#------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="C",bg="powder blue",command=btnClear).grid(row=5,column=1)

btnEqual=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="=",bg="powder blue",command=btnEqual).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)

#==========================Restuarent INfo 1====================================================
ref=StringVar()
fries=StringVar()
burger=StringVar()
chicken=StringVar()
cheese=StringVar()
drinks=StringVar()
mealCost=StringVar()
survice=StringVar()
tax=StringVar()
sub=StringVar()
total=StringVar()
ref.set("Auto Generatable")
fries.set("0")
burger.set("0")
chicken.set("0")
cheese.set("0")
drinks.set("0")
mealCost.set("0")
survice.set("2$")
tax.set("2% Of Meal Cost")
sub.set("0")
total.set("0")


def Ref():
    x=random.randint(1202,500332)
    randRef=str(x)
    ref.set(randRef)


    coF=float(fries.get())*1.5
    coB=float(burger.get())*2.5
    coChi=float(chicken.get())*0.5
    coChee=float(cheese.get())*1.0
    coDri=float(drinks.get())*2.0
    totalMeal=str(coF+coB+coChi+coChee+coDri)
    mealCost.set(totalMeal)

    totalTax=float(totalMeal)*0.02
    toTax=str(totalTax)
    tax.set(toTax)

    subto=float(tax.get())+float(mealCost.get())
    suvtotal=str(subto)
    sub.set(suvtotal)

    tota=float(sub.get())+2.0
    tot=str(tota)
    total.set(tot)

def qExit():
    root.destroy()

def Reset():
    ref.set("Auto Generatable")
    fries.set("0")
    burger.set("0")
    chicken.set("0")
    cheese.set("0")
    drinks.set("0")
    mealCost.set("0")
    survice.set("2$")
    tax.set("2% Of Meal Cost")
    sub.set("0")
    total.set("0")


lblRef=Label(f1,font=('arial',16,'bold'),text="  Reference  ",bd=16,anchor='w')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1,font=('arial',16,'bold'),textvariable=ref,bd=16,insertwidth=4,bg='powder blue',justify="right")
txtRef.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="  Large Fries  ",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=16,insertwidth=4,bg='powder blue',justify="right")
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="  Burger  ",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=burger,bd=16,insertwidth=4,bg='powder blue',justify="right")
txtBurger.grid(row=2,column=1)

lblChicken=Label(f1,font=('arial',16,'bold'),text="Chicken Meal",bd=16,anchor='w')
lblChicken.grid(row=3,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=chicken,bd=16,insertwidth=4,bg='powder blue',justify="right")
txtChicken.grid(row=3,column=1)

lblCheese=Label(f1,font=('arial',16,'bold'),text="Cheese Meal",bd=16,anchor='w')
lblCheese.grid(row=4,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=cheese,bd=16,insertwidth=4,bg='powder blue',justify="right")
txtCheese.grid(row=4,column=1)

#==========================Restuarent INfo 2====================================================


lbldrinks=Label(f1,font=('arial',16,'bold'),text="  Drinks  ",bd=16,anchor='w')
lbldrinks.grid(row=0,column=2)
txtdrinks=Entry(f1,font=('arial',16,'bold'),textvariable=drinks,bd=16,insertwidth=4,justify="right")
txtdrinks.grid(row=0,column=3)

lblmealCost=Label(f1,font=('arial',16,'bold'),text="  Cost of Meal  ",bd=16,anchor='w')
lblmealCost.grid(row=1,column=2)
txtmealCost=Entry(f1,font=('arial',16,'bold'),textvariable=mealCost,bd=16,insertwidth=4,justify="right")
txtmealCost.grid(row=1,column=3)

lblsurvice=Label(f1,font=('arial',16,'bold'),text="  Survice Charge  ",bd=16,anchor='w')
lblsurvice.grid(row=2,column=2)
txtsurvice=Entry(f1,font=('arial',16,'bold'),textvariable=survice,bd=16,insertwidth=4,justify="right")
txtsurvice.grid(row=2,column=3)

lbltax=Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
lbltax.grid(row=3,column=2)
txttax=Entry(f1,font=('arial',16,'bold'),textvariable=tax,bd=16,insertwidth=4,justify="right")
txttax.grid(row=3,column=3)

lblsub=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w')
lblsub.grid(row=4,column=2)
txtsub=Entry(f1,font=('arial',16,'bold'),textvariable=sub,bd=16,insertwidth=4,justify="right")
txtsub.grid(row=4,column=3)

lbltotal=Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lbltotal.grid(row=5,column=2)
txttotal=Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=16,insertwidth=4,bg='green',justify="right")
txttotal.grid(row=5,column=3)

#=================  Buttons  ============================================================

btnTotal=Button(f1,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
btnExit=Button(f1,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=2)
btnReset=Button(f1,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=3)



#=======================================

root.mainloop()
