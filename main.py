# Writing a program which accepts 2 numbers
# and displays answer in the third box.

import tkinter
import tkinter as tk


# Creating a window
window= tk.Tk()
window.title("Adding Two Numbers")
window.geometry("500x250")
label1 = tk.Label(window, text="Please enter first number: ")
label1.grid(row=0, column=0)
label2 = tk.Label(window, text="Please enter second number: ")
label2.grid(row=1, column=0)
label3 = tk.Label(window, text="Answer: ")
label3.grid(row=2, column=0)


# A function to clear the numbers added
def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)


button2 = tk.Button(window, text="CLEAR", command = clear)
button2.grid(row=4, column=1)
button3 = tk.Button(window, text="EXIT", command = exit)
button3.grid(row=4, column=2)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)
entry3 = tk.Entry(window)
entry3.grid(row= 2, column=1)


#A Function to add the two numbers
def addNumbers():
    sum=int(entry1.get())+int(entry2.get())
    entry3.insert(0,str(sum))
button1 = tk.Button(window, text="ADD", command=addNumbers)
button1.grid(row=4, column=0)

window.mainloop()
