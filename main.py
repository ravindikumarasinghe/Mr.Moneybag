import requests
import tkinter as tk
from tkinter import *
from datetime import datetime


def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    # print(response)
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text="Welcome to Bitcoin World\nCurrent Bitcoin Value : " + str(price) + "$ ")
    labelTime.config(text="Updated at : " + time + "\nThis value will update at every 5s")

    canvas.after(1000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Mr.Moneybag")
canvas = tk.Canvas(bg="black")
canvas.pack(expand=True, fill="both")
gif = PhotoImage(file="bitcoin1.png")
canvas.create_image(60, 20, image=gif, anchor="nw")

f1 = ("Open Sans", 16, "bold")
f2 = ("Open Sans", 25, "bold")
f3 = ("Open Sans", 16, "normal")

# label = tk.Label(canvas, text="Bitcoin Price", font=f1)
# label.pack(pady=150)

labelPrice = tk.Label(canvas, font=f2, bg="black", fg="#B2BEB5")
labelPrice.pack(pady=200)

labelTime = tk.Label(canvas, font=f3, bg="black", fg="#6A6C6D")
labelTime.pack()

trackBitcoin()

canvas.mainloop()
