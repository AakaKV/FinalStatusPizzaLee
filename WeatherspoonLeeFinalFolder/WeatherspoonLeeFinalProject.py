from cProfile import label
from sqlite3 import Row
from tkinter import *
root = Tk()
#Never figure out how to remove this without losing Ico File access in program
iconic = "C:/Users/wowza/Documents/Ivy Tech/SDEV140/Wk  (8)/Assignment docs/WeatherspoonLeeFinalFolder/Media/faviconFinal.ico"
root.iconbitmap(iconic)
#These set the toppings
TOPPINGS = ["Pepperoni","Sausage","Extra cheese","Peppers","Mushrooms","Onion","Tomato"]#list of toppings
checkYes = []#Which toppings are checked
checkofToppings = []#Here I am creating the list that will be parallel to toppings to filter out unchecked toppings

#This will write the items in the cart to a txt file called receipt
def receiptWriteTop():#Writing checked toppings to receipt
    print("Start receptWriteTop")
    checkSet = {}
    for topping, markCheck in zip(TOPPINGS, checkofToppings):
        checkSet[topping]=markCheck.get()
        print("Running if statement")
        if checkSet[topping] == 1:# If the topping is marked as yes then the program labels it in the window
            checkYes.append(topping)
            #Trying to at least print the selected topping values here in the first window
            print("Try label")
            selectedTop = Label(root,text=topping)#Testing label remove after fstring text is created
            print("After Label")
        else:
            print("Not selected")
def win1op():
    print("pizzaCart")
    pizzaCart = Toplevel()
    pizzaCart.iconbitmap(iconic)
    for topping in checkYes:# trying to print label in pizza cart window
        topped = Label(pizzaCart, text=topping).grid()
    if PoD.get() == 1:
        HereGo = label(pizzaCart,text="Pickup").grid()
    elif PoD.get() == 2:
        HereGo = label(pizzaCart,text="Delivery").grid()
    else:
        print("ERROR IN RADIOBUTTON")

PoD = IntVar()
PoD.set(2)
Radiobutton(root, text="Pickup", variable=PoD, value=1).grid()
Radiobutton(root, text="Delivery", variable=PoD, value=2).grid()
for topName in TOPPINGS: #uses a for loop to create a check list of toppings
    pizzaTop = IntVar()
    toppingNames = Checkbutton(root, text= topName, variable=pizzaTop) 
    toppingNames.deselect()
    toppingNames.grid()
    checkofToppings.append(pizzaTop)
#Button for confirm toppings, only selecting and displaying one topping regardless of it's selection
checkConfirm = Button(root, text="Confirm Toppings", command = receiptWriteTop)#using check of toppings as function variable
checkConfirm.grid()
#Open window 1(the Cart)
win1button= Button(root, text="Window 1 open",  command= win1op, pady=5).grid()

    



root.mainloop()