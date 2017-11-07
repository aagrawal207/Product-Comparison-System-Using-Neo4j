try:
    from Tkinter import *
    from Tkinter import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk

# Window is created here
root = Tk()
root.title("Product-Comparison-System-Using-Neo4j")

searchRow = 0

# Search bar
# Use this as a flag to indicate if the box was clicked.
global clicked
clicked = False

# Delete the contents of the Entry widget. Use the flag
# so that this only happens the first time.
def callback(event):
    global clicked
    if (clicked == False):
        searchBar.delete(0, END)
        searchBar.config(fg = "black")   # Change the colour of the text here.
        clicked = True

searchBar = Entry(root, width=50, fg = "gray")
searchBar.bind("<Button-1>", callback)   # Bind a mouse-click to the callback function.
searchBar.insert(0, 'Search for a product...')
searchBar.grid(row=searchRow, column=0, sticky=W, pady=4)

# Rating dropdown
DropDownDict = {"Above 1" : 1, "Above 2" : 2, "Above 3" : 3, "Above 4" : 4}
ratingDropDownValue = StringVar(root)
ratingDropDownValue.set("Above 1") # default value
ratingDropDown = OptionMenu(root,
                    ratingDropDownValue,
                    *DropDownDict.keys())
ratingDropDown.grid(row=searchRow, column=7, sticky=E, pady=4)

# Label for "Price range from: "
PriceRangeVariableFrom = StringVar()
PriceRangeLabelFrom = Label(root, textvariable=PriceRangeVariableFrom)
PriceRangeVariableFrom.set("Price range from: ")
PriceRangeLabelFrom.grid(row=searchRow, column=8, sticky=E, pady=4)

# From entry
fromEntry = Entry(root, width=5)
fromEntry.grid(row=searchRow, column=9, sticky=W, pady=4)

# Label for "to: "
PriceRangeVariableTo = StringVar()
PriceRangeLabelTo = Label(root, textvariable=PriceRangeVariableTo)
PriceRangeVariableTo.set(" to: ")
PriceRangeLabelTo.grid(row=searchRow, column=10, sticky=E, pady=4)

# To entry
toEntry = Entry(root, width=5)
toEntry.grid(row=searchRow, column=11, sticky=W, pady=4)

# This method is called when button is clicked
def go():
    print(searchBar.get())
    print(ratingDropDownValue.get())
    print(fromEntry.get())
    print(toEntry.get())

# Submit button for searching
Button(root, text="Go!", command=go).grid(row=searchRow, column=12, sticky=E, pady=4)

root.mainloop()
