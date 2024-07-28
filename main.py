import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

prices = {
    "Fried Rice": 900,
    "Nasi Goreng": 1000,
    "Cheese Kottu": 950,
    "Deviled Prawns": 1000,
    "Seafood Platter": 3000,
    "Crab Curry": 2000,
}

root = Tk()
root.title("Online Food Ordering System")


# -----------------FUNCTIONS----------------------------- #
# region ADD to Order Button
def add():
    #updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + ": " + "Rs." + str(prices[displayLabel.cget("text")])
    updated_order = current_order + "\n" + added_dish
    orderTransaction.configure(text=updated_order)

    #updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("Rs.", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + "Rs." + str(updated_total))


#endregion

#region Remove Button Function

def remove():
    dish_to_remove = displayLabel.cget("text") + ": " + "Rs." + str(prices[displayLabel.cget("text")])
    transaction_text = orderTransaction.cget("text")

    # Check if the dish to remove is in the transaction text
    if dish_to_remove in transaction_text:
        # Split the transaction text by newline
        transaction_list = transaction_text.split("\n")

        # Remove the dish from the transaction list
        transaction_list.remove(dish_to_remove)

        # Construct the updated transaction text
        updated_order = "\n".join(transaction_list)
        orderTransaction.configure(text=updated_order)

        # Update the total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "").replace("Rs.", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : Rs." + str(updated_total))


# region Display button Functions
def displayFriedrice():
    friedRiceDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    nasiGorengDishFrame.configure(style="DishFrame.TFrame")
    cheeseKottuDishFrame.configure(style="DishFrame.TFrame")
    deviledPrawnsDishFrame.configure(style="DishFrame.TFrame")
    seafoodPlatterDishFrame.configure(style="DishFrame.TFrame")
    crabCurryDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=friedRiceImage,
        text="Fried Rice",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3)
    )


def displayNasiGoreng():
    nasiGorengDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    friedRiceDishFrame.configure(style="DishFrame.TFrame")
    cheeseKottuDishFrame.configure(style="DishFrame.TFrame")
    deviledPrawnsDishFrame.configure(style="DishFrame.TFrame")
    seafoodPlatterDishFrame.configure(style="DishFrame.TFrame")
    crabCurryDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=nasiGorengImage,
        text="Nasi Goreng",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3),
    )


def displayCheeseKottu():
    cheeseKottuDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    friedRiceDishFrame.configure(style="DishFrame.TFrame")
    nasiGorengDishFrame.configure(style="DishFrame.TFrame")
    deviledPrawnsDishFrame.configure(style="DishFrame.TFrame")
    seafoodPlatterDishFrame.configure(style="DishFrame.TFrame")
    crabCurryDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=cheeseKottuImage,
        text="Cheese Kottu",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3),
    )


def displayDeviledPrawns():
    deviledPrawnsDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    friedRiceDishFrame.configure(style="DishFrame.TFrame")
    nasiGorengDishFrame.configure(style="DishFrame.TFrame")
    cheeseKottuDishFrame.configure(style="DishFrame.TFrame")
    seafoodPlatterDishFrame.configure(style="DishFrame.TFrame")
    crabCurryDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=deviledPrawnsImage,
        text="Deviled Prawns",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3),
    )


def displaySeafoodPlatter():
    seafoodPlatterDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    friedRiceDishFrame.configure(style="DishFrame.TFrame")
    nasiGorengDishFrame.configure(style="DishFrame.TFrame")
    cheeseKottuDishFrame.configure(style="DishFrame.TFrame")
    deviledPrawnsDishFrame.configure(style="DishFrame.TFrame")
    crabCurryDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=seafoodPlatterImage,
        text="Seafood Platter",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3),
    )


def displayCrabCurry():
    crabCurryDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    friedRiceDishFrame.configure(style="DishFrame.TFrame")
    nasiGorengDishFrame.configure(style="DishFrame.TFrame")
    cheeseKottuDishFrame.configure(style="DishFrame.TFrame")
    deviledPrawnsDishFrame.configure(style="DishFrame.TFrame")
    seafoodPlatterDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=crabCurryImage,
        text="Crab Curry",
        font=("Helvetica", 13, "bold"),
        foreground="white",
        compound="bottom",
        padding=(3, 3, 3, 3),
    )


# endregion

# -----------------STYLING AND IMAGES------------------- #
# region style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background="#2B2B28")
s.configure('MenuFrame.TFrame', background="#4A4A48")
s.configure('DisplayFrame.TFrame', background="#0F1110")
s.configure('OrderFrame.TFrame', background="#B7C4CF")
s.configure('DishFrame.TFrame', background="#4A4A48", relief="raised")
s.configure('MenuLabel.TLabel',
            background="#ff6347",
            font=("Arial", 13, "italic"),
            foreground="white",
            padding=(5, 5, 5, 5),
            width=21
            )
s.configure('orderTotalLabel.TLabel',
            background="#0F1110",
            font=("Arial", 10, "bold"),
            foreground="white",
            padding=(2, 2, 2, 2),
            anchor="w"
            )
s.configure('orderTransaction.TLabel',
            background="#4A4A48",
            font=('Helvetica', 12),
            foreground="white",
            wraplength=180,
            anchor="nw",
            padding=(3, 3, 3, 3)
            )

# endregion

# region Images
# Top Banner images
LogoImageObject = Image.open("Images/logo.jpeg").resize((200, 200))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/banner.jpeg").resize({600, 200})
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu Images
displayDefaultImageObject = Image.open("Images/display1.jpeg").resize((250, 328))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

friedRiceImageObject = Image.open("Images/friedRice.jpg").resize({240, 298})
friedRiceImage = ImageTk.PhotoImage(friedRiceImageObject)

nasiGorengImageObject = Image.open("Images/nasiGoreng.jpg").resize({240, 298})
nasiGorengImage = ImageTk.PhotoImage(nasiGorengImageObject)

cheeseKottuImageObject = Image.open("Images/cheeseKottu.jpg").resize({240, 298})
cheeseKottuImage = ImageTk.PhotoImage(cheeseKottuImageObject)

deviledPrawnsImageObject = Image.open("Images/deviledPrawns.jpg").resize({240, 298})
deviledPrawnsImage = ImageTk.PhotoImage(deviledPrawnsImageObject)

seafoodPlatterImageObject = Image.open("Images/seafoodPlatter.jpg").resize({240, 298})
seafoodPlatterImage = ImageTk.PhotoImage(seafoodPlatterImageObject)

crabCurryImageObject = Image.open("Images/crabCurry.jpg").resize({240, 298})
crabCurryImage = ImageTk.PhotoImage(crabCurryImageObject)

# endregion

# ----------------- WIDGETS ------------------------------ #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width=1000, height=800, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

# Dish Frames
friedRiceDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
friedRiceDishFrame.grid(row=1, column=0, sticky="NSEW")

nasiGorengDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
nasiGorengDishFrame.grid(row=2, column=0, sticky="NSEW")

cheeseKottuDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
cheeseKottuDishFrame.grid(row=3, column=0, sticky="NSEW")

deviledPrawnsDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
deviledPrawnsDishFrame.grid(row=4, column=0, sticky="NSEW")

seafoodPlatterDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
seafoodPlatterDishFrame.grid(row=5, column=0, sticky="NSEW")

crabCurryDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
crabCurryDishFrame.grid(row=6, column=0, sticky="NSEW")

# endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image=LogoImage, background="#4CAF50")
LogoLabel.grid(row=0, column=0, sticky="W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image=TopBannerImage, background="#FF5722")
RestaurantBannerLabel.grid(row=0, column=1, sticky="NSEW")

# endregion

# region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text="MENU", style="MenuLabel.TLabel")
MainMenuLabel.grid(row=0, column=0, sticky="WE")
MainMenuLabel.configure(
    anchor="center",
    font=("Helvetica", 14, "bold")
)
friedRiceDishLabel = ttk.Label(friedRiceDishFrame, text="Fried Rice: Rs:900", style="MenuLabel.TLabel")
friedRiceDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

nasiGorengDishLabel = ttk.Label(nasiGorengDishFrame, text="Nasi goreng: Rs:1000", style="MenuLabel.TLabel")
nasiGorengDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

cheeseKottuDishLabel = ttk.Label(cheeseKottuDishFrame, text="Cheese kottu: Rs:950", style="MenuLabel.TLabel")
cheeseKottuDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

deviledPrawnsDishLabel = ttk.Label(deviledPrawnsDishFrame, text="Deviled Prawns: Rs:1000", style="MenuLabel.TLabel")
deviledPrawnsDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

seafoodPlatterDishLabel = ttk.Label(seafoodPlatterDishFrame, text="Seafood Platter: Rs:3000", style="MenuLabel.TLabel")
seafoodPlatterDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

crabCurryDishLabel = ttk.Label(crabCurryDishFrame, text="Crab Curry: Rs:2000", style="MenuLabel.TLabel")
crabCurryDishLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

# Buttons
friedRiceDisplayButton = ttk.Button(friedRiceDishFrame, text="Display", command=displayFriedrice)
friedRiceDisplayButton.grid(row=0, column=1, padx=10)

nasiGorengDisplayButton = ttk.Button(nasiGorengDishFrame, text="Display", command=displayNasiGoreng)
nasiGorengDisplayButton.grid(row=0, column=1, padx=10)

cheeseKottuDisplayButton = ttk.Button(cheeseKottuDishFrame, text="Display", command=displayCheeseKottu)
cheeseKottuDisplayButton.grid(row=0, column=1, padx=10)

deviledPrawnsDisplayButton = ttk.Button(deviledPrawnsDishFrame, text="Display", command=displayDeviledPrawns)
deviledPrawnsDisplayButton.grid(row=0, column=1, padx=10)

seafoodPlatterDisplayButton = ttk.Button(seafoodPlatterDishFrame, text="Display", command=displaySeafoodPlatter)
seafoodPlatterDisplayButton.grid(row=0, column=1, padx=10)

crabCurryDisplayButton = ttk.Button(crabCurryDishFrame, text="Display", command=displayCrabCurry)
crabCurryDisplayButton.grid(row=0, column=1, padx=10)

# endregion

# region Order Section
orderTitleLabel = ttk.Label(orderFrame, text="ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor="center",
    padding=(5, 5, 5, 5),
)
orderTitleLabel.grid(row=0, column=0, sticky="EW")

orderIDLabel = ttk.Label(orderFrame, text="ORDER ID : ")
orderIDLabel.configure(
    background="black",
    foreground="white",
    font=("Helvetica", 11, "italic"),
    anchor="center",
)
orderIDLabel.grid(row=1, column=0, sticky="EW", pady=1)

orderTransaction = ttk.Label(orderFrame, style='orderTransaction.TLabel')
orderTransaction.grid(row=2, column=0, sticky="NSEW")

orderTotalLabel = ttk.Label(orderFrame, text="TOTAL : Rs.0", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=3, column=0, sticky="EW")

orderButton = ttk.Button(orderFrame, text="ORDER")
orderButton.grid(row=4, column=0, sticky="EW")

# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image=displayDefaultImage)
displayLabel.grid(row=0, column=0, sticky="NSEW", columnspan=2)
displayLabel.configure(background="black")

addOrderButton = ttk.Button(displayFrame, text="ADD TO ORDER", command=add)
addOrderButton.grid(row=1, column=0, padx=2, sticky="NSEW")

removeOrderButton = ttk.Button(displayFrame, text="REMOVE", command=remove)
removeOrderButton.grid(row=1, column=1, padx=2, sticky="NSEW")

# ------------------- GRID CONFIGURATION---------------#
mainFrame.columnconfigure(2, weight=1)
mainFrame.rowconfigure(1, weight=1)
menuFrame.columnconfigure(2, weight=1)
menuFrame.rowconfigure(1, weight=1)
menuFrame.rowconfigure(2, weight=1)
menuFrame.rowconfigure(3, weight=1)
menuFrame.rowconfigure(4, weight=1)
menuFrame.rowconfigure(5, weight=1)
menuFrame.rowconfigure(6, weight=1)
orderFrame.columnconfigure(0, weight=1)
orderFrame.rowconfigure(2, weight=1)
removeOrderButton.rowconfigure(2, weight=1)
removeOrderButton.columnconfigure(0, weight=1)

root.mainloop()
