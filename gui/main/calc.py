from tkinter import *

root = Tk()
root.title("Reaperpy0's Scientific Calculator (GUI)")

num1_input = Entry(width=50)
num2_input = Entry(width=50)

num1 = int(num1_input.get())
num2 = (num2_input.get())
result = 0

def addClick():
  result = num1 + num2
  resultLabel = Label(text=result)
  resultLabel.grid(row=3, column=0)


addButton = Button(padx=20, pady=20, text="+", command=addClick)

num1_input.grid(row=0, column=0)
num2_input.grid(row=1, column=0)
addButton.grid(row=2, column=0)


root.mainloop()