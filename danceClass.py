from tkinter import *
import os

def submit1(stuName,add,phone):
    with open("danceData.txt","a") as f:
        f.write(stuName.get()+" "+add.get()+" "+phone.get()+"\n")
    stuName.set("")
    add.set("")
    phone.set("")


root =Tk()
root.geometry("500x300")
root.title("My Dance Class Admission --using tkinter_practise")

stuName=StringVar()
stuAddress=StringVar()
stuPhone=StringVar()

name = Label(root, text="Your Name : ", font=('calibre',11, 'bold'))
address = Label(root, text="Address : ", font=('calibre',11, 'bold'))
phone = Label(root, text="Phone : ", font=('calibre',11, 'bold'))

name_entry = Entry(root, textvariable = stuName,justify=CENTER,fg="#FF7F50")
address_entry = Entry(root, textvariable = stuAddress,justify=CENTER)
phone_entry = Entry(root, textvariable = stuPhone,justify=CENTER)

name.grid(row=0, pady=15)
address.grid(row=1,  pady=15)
phone.grid(row=2, pady=15)
name_entry.grid(row=0, column=1, pady=15)
address_entry.grid(row=1, column=1, pady=15)
phone_entry.grid(row=2, column=1, pady=15)

btn=Button(root,text = 'Submit', command = lambda: submit1(stuName, stuAddress, stuPhone),bg="green")
btn.grid(row=4, column=0)

root.mainloop()