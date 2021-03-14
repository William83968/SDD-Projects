import tkinter as tk
from tkinter import *

wn = Tk(className="Pirate trading game")
wn.geometry("900x500")
wn.attributes('-alpha',0.95)

gold_amount = 0
health_amount = 0
gold_number = "Gold amount:{}".format(gold_amount)
health_number = "Ship health:{}".format(health_amount)

bg_image = tk.PhotoImage(file="old_paper.png")
background_label = tk.Label(wn, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

gold_image = tk.PhotoImage(file="gold_button.png")
wood_image = tk.PhotoImage(file="wood_button.png")

class Button(tk.Button):
    def __init__(self, command, width, height, color, row, column, padx=0, pady=0):
        tk.Button.__init__(self, width=width, height=height, image=gold_image,bg=color, command=command)
        self.grid(row=row, column=column, padx=padx, pady=pady)
    
class Label(tk.Label):
    def __init__(self, text, width, background, row, column, padx):
        tk.Label.__init__(self, text=text, width=width, bg=background)
        self.grid(row=row, column=column, padx=padx)

def change_value(value):
    global gold_amount 
    gold_amount += value
    gold_number = "Gold amount:{}".format(gold_amount)
    gold.configure(text=gold_number)
    
button1_label = Label("TRADE", 50, None, 1, 0, 20)
button1 = Button(lambda: change_value(0), 74, 20,'grey', 1, 0, 30, 30)


gold = tk.Label(wn, text=gold_number, height = 2, bg='grey')
gold.grid(row=0, column=0, padx=60)

ship_health = tk.Label(wn, text=health_number, height = 2)
ship_health.grid(row=0, column=1, padx=90)

wn.wm_attributes("-transparent")
wn.mainloop()