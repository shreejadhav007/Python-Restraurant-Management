import random
import time
from tkinter import *
import string

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1500, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))
# -----------------INFO TOP------------
info = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg="steel blue", bd=10,
                anchor='w')
info.grid(row=0, column=0)
info = Label(Tops, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
info.grid(row=1, column=0)






rand = StringVar()
Fries = StringVar()
lunch = StringVar()
Burger = StringVar()
Pizza = StringVar()
Subtotal1 = StringVar()
Total1 = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost1= StringVar()
Cheese_burger = StringVar()


lreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.",fg="steel blue", bd=10, anchor='w')
lreference.place(x=130,y=150)
reference = Entry(f1, font=('ariel', 16, 'bold'),  state='disabled' ,textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                     justify='right')
reference.place(x=300,y=150)

lfries = Label(f1, font=('aria', 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
lfries.place(x=130,y=230)
fries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')
fries.place(x=300,y=230)

llunch = Label(f1, font=('aria', 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
llunch.place(x=130,y=310)
lunch = Entry(f1, font=('ariel', 16, 'bold'), textvariable=lunch, bd=6, insertwidth=4, bg="powder blue",
                      justify='right')
lunch.place(x=300,y=310)
#
lburger = Label(f1, font=('aria', 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
lburger.place(x=130,y=380)
burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')
burger.place(x=300,y=380)

lpizza = Label(f1, font=('aria', 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
lpizza.place(x=130,y=450)
pizza = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Pizza, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')
pizza.place(x=300,y=450)

lCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
lCheese_burger.place(x=650,y=150)
Cheese_burger1 = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                         bg="powder blue", justify='right')
Cheese_burger1.place(x=850,y=150)
#
# --------------------------------------------------------------------------------------
lDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
lDrinks.place(x=650,y=230)
Drinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')
Drinks.place(x=850,y=230)

lcost = Label(f1, font=('aria', 16, 'bold'), text="cost", fg="steel blue", bd=10, anchor='w')
lcost.place(x=650,y=310)
cost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost1, bd=6, insertwidth=4, bg="powder blue",
                justify='right')
cost.place(x=850,y=310)

lService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="steel blue", bd=10, anchor='w')
lService_Charge.place(x=650,y=380)
Service_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                          bg="powder blue", justify='right')
Service_Charge.place(x=850,y=380)
#
lTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
lTax.place(x=650,y=450)
Tax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue", justify='right')
Tax.place(x=850,y=450)
#
Subtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
Subtotal.place(x=130,y=530)
Subtotal = Entry(f1, font=('ariel', 16, 'bold'),  textvariable=Subtotal1, bd=6, insertwidth=4, bg="powder blue",
                    justify='right')
Subtotal.place(x=300,y=530)

Total = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
Total.place(x=650,y=530)
Total = Entry(f1, font=('ariel', 16, 'bold') , textvariable=Total1, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')
Total.place(x=850,y=530)


def total():
    friesMeal = 25
    burgerMeal = 35
    lunchmeal = 40
    pizzaMeal = 50
    Cheese_burger = 30
    drinks = 35

    friesg= (Fries.get())
    lunchg = (lunch.get()  )
    burgerg =(Burger.get())
    pizzag = (Pizza.get())
    cBurgerg = (Cheese_burger1.get())
    drinkg = (Drinks.get())

    nums = list(string.digits)
    pas = []
    for i in range(5):
        pas.append(random.choice(nums))

    a = ''.join(pas)
    PRN = f'OD{a}'
    print(PRN)
    reference.configure(state='normal')
    reference.insert(END,PRN)
    reference.configure(state='disabled')


   
    cost2=  (friesMeal*int(friesg)) + (burgerMeal*int(burgerg))  + (lunchmeal*int(lunchg))  + (pizzaMeal*int(pizzag))  + (Cheese_burger*int(cBurgerg))  + (drinks*int(drinkg))
    cost.insert(END, cost2)
    cost.configure(state='disabled')
    tax = (2/100)*cost2
    Tax.insert(END, tax )
    Tax.configure(state='disabled')
    scharge = 20
    Service_Charge.insert(END,scharge)
    Service_Charge.configure(state='disabled')
    stotal = tax + scharge
    Subtotal.insert(END, stotal)
    Subtotal.configure(state='disabled')
    totals = cost2 +stotal
    Total.insert(END,totals)
    Total.configure(state='disabled')

def clear():

    pass
def quite():
    pass

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)






btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                  bg="powder blue", command=total)
btnTotal.place(x=300,y=600)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                  bg="powder blue", command=clear)
btnreset.place(x=580,y=600)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                 bg="powder blue", command=quite)
btnexit.place(x=850,y=600)

btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Price",
                 bg="powder blue", command=price)
btnprice.place(x=1300,y=600)





root.mainloop()