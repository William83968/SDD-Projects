import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""
# Create functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
            expression = str(result)
        except:
            result = "error"
            expression = ""
    label_result.configure(text=result)



# Create GUI
label_result = tkinter.Label(root, text="", height = 2)
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1", command=lambda: add("1"),width = 5, height = 4)
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"),width = 5, height = 4)
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"),width = 5, height = 4)
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", command=lambda: add("/"),width = 5, height = 4)
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", command=lambda: add("4"),width = 5, height = 4)
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"),width = 5, height = 4)
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"),width = 5, height = 4)
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*", command=lambda: add("*"),width = 5, height = 4)
button_multiply.grid(row=2, column=3)

button_7 = tkinter.Button(root, text="7", command=lambda: add("7"),width = 5, height = 4)
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"),width = 5, height = 4)
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"),width = 5, height = 4)
button_9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text="-", command=lambda: add("-"),width = 5, height = 4)
button_subtract.grid(row=3, column=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear(),width = 5, height = 4)
button_clear.grid(row=4, column=0)

button_4 = tkinter.Button(root, text="0", command=lambda: add("0"),width = 5, height = 4)
button_4.grid(row=4, column=1)
 
button_dot = tkinter.Button(root, text=".", command=lambda: add("."),width = 5, height = 4)
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", command=lambda: add("+"),width = 5, height = 4)
button_add.grid(row=4, column=3)


button_equals = tkinter.Button(root, text="=", command=lambda: calculate(),width = 22, height = 2)
button_equals.grid(row=5, column=0, columnspan=4)




root.mainloop()