from neo4j.v1 import GraphDatabase, basic_auth
try:
    from Tkinter import *
    from Tkinter import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk

driver = GraphDatabase.driver("bolt://localhost:7687",
                                auth=basic_auth("neo4j", "neo4j"))
session = driver.session()

################################################################################
# All the methods are here
def go():
    # result = session.run("""MATCH (a:Book)-[:PUBLISHED_BY]->(b:Publishing_House)
    # return a.title as a,b.name as b""")
    # for record in result:
    #     print("%s %s" % (record["a"], record["b"]))
    print(searchBar.get())
    print(ratingDropDownValue.get())
    print(fromEntry.get())
    print(toEntry.get())

def addProduct():
    print(NameEntry.get())
    print(websiteDropDownValue.get())
    print("Price = " + PriceEntry.get())
    print("Stock = " + StockEntry.get())
    print("Rating = " + RatingEntry.get())

################################################################################
# Window is created here
root = Tk()
root.title("Product-Comparison-System-Using-Neo4j")

padding = 20
searchFrame = Frame(root, height=100)
searchFrame.pack(pady=(padding,padding), padx=(padding, padding))

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
searchBar = Entry(searchFrame, fg = "gray")
searchBar.bind("<Button-1>", callback)   # Bind a mouse-click to the callback function.
searchBar.insert(0, 'Search for a product...')
searchBar.pack(side=LEFT, fill=X)

# Rating dropdown
DropDownDict = {"Above 1" : 1, "Above 2" : 2, "Above 3" : 3, "Above 4" : 4}
ratingDropDownValue = StringVar(searchFrame)
ratingDropDownValue.set("Above 1") # default value
ratingDropDown = OptionMenu(searchFrame,
                    ratingDropDownValue,
                    *DropDownDict.keys())
ratingDropDown.pack(side=LEFT)

# Label for "Price range from: "
PriceRangeVariableFrom = StringVar()
PriceRangeLabelFrom = Label(searchFrame, textvariable=PriceRangeVariableFrom)
PriceRangeVariableFrom.set("Price range from: ")
PriceRangeLabelFrom.pack(side=LEFT)

# From entry
fromEntry = Entry(searchFrame, width=7)
fromEntry.insert(0, '0')
fromEntry.pack(side=LEFT)

# Label for "to: "
PriceRangeVariableTo = StringVar()
PriceRangeLabelTo = Label(searchFrame, textvariable=PriceRangeVariableTo)
PriceRangeVariableTo.set(" to: ")
PriceRangeLabelTo.pack(side=LEFT)

# To entry
toEntry = Entry(searchFrame, width=7)
toEntry.insert(0, 100000)
toEntry.pack(side=LEFT)

# Submit button for searching
Button(searchFrame, text="Go!", command=go).pack(side=LEFT, padx=(10,0))

################################################################################

# Data will be shown in this frame
dataFrame = Frame(root, bg='red')
dataFrame.pack(fill=BOTH,expand=True)

################################################################################
addFrame = Frame(root)
addFrame.pack(pady=(padding,padding), padx=(padding, 0))

# Label for "Enter Product Name: "
ProductNameVar = StringVar()
ProductNameLabel = Label(addFrame, textvariable=ProductNameVar)
ProductNameVar.set("Enter Product Name: ")
ProductNameLabel.grid(row = 0, column=0)

# Product Name entry
NameEntry = Entry(addFrame)
NameEntry.grid(row=0, column=3)

# Label for "Enter Product Price: "
ProductPriceVar = StringVar()
ProductPriceLabel = Label(addFrame, textvariable=ProductPriceVar)
ProductPriceVar.set("Enter Price of the Product: ")
ProductPriceLabel.grid(row = 1, column=0)

# Product Name entry
PriceEntry = Entry(addFrame)
PriceEntry.grid(row=1, column=3)

# Label for "Enter Product Rating: "
ProductRatingVar = StringVar()
ProductRatingLabel = Label(addFrame, textvariable=ProductRatingVar)
ProductRatingVar.set("Enter Rating of the Product: ")
ProductRatingLabel.grid(row = 2, column=0)

# Product Name entry
RatingEntry = Entry(addFrame)
RatingEntry.grid(row=2, column=3)

# Label for "Enter Product Stock: "
ProductStockVar = StringVar()
ProductStockLabel = Label(addFrame, textvariable=ProductStockVar)
ProductStockVar.set("Enter Stock of the Product: ")
ProductStockLabel.grid(row = 3, column=0)

# Product Name entry
StockEntry = Entry(addFrame)
StockEntry.grid(row=3, column=3)

# Website dropdown
DropDownDict2 = {"Amazon" : 1, "Flipkart" : 2, "Snapdeal" : 3, "Shopclues" : 4}
websiteDropDownValue = StringVar(addFrame)
websiteDropDownValue.set("Amazon") # default value
websiteDropDown = OptionMenu(addFrame,
                    websiteDropDownValue,
                    *DropDownDict2.keys())
websiteDropDown.grid(row=4, column=0)

# Add Product button
Button(addFrame, text="Add Product", command=addProduct).grid(row=4,column=3)

root.mainloop()
