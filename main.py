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

def deleteProduct():
    print(NameEntry.get())
    print(websiteDropDownValue.get())
    print("Stock = " + StockEntry.get())

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

# Label for "Price range from: "
RatingVar = StringVar()
RatingLabel = Label(searchFrame, textvariable=RatingVar)
RatingVar.set("  Rating: ")
RatingLabel.pack(side=LEFT)

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
PriceRangeVariableFrom.set("  Price range from: ")
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
lineFrame = Frame(root, bg='black')
lineFrame.pack(fill=BOTH)

################################################################################

# Data will be shown in this frame
dataFrame = Frame(root, bg='red')
dataFrame.pack(fill=BOTH,expand=True)

################################################################################

# Data will be shown in this frame
lineFrame = Frame(root, bg='black')
lineFrame.pack(fill=BOTH)

################################################################################
addFrame = Frame(root)
addFrame.pack(pady=(padding,padding), padx=(padding, 0))

row_num = 0

# Label for "Add Product Stock: "
AddProductVar = StringVar()
AddProductLabel = Label(addFrame, textvariable=AddProductVar)
AddProductVar.set("Add Product Stock: ")
AddProductLabel.grid(row = row_num, column=2)

# Label for "Enter Product Name: "
ProductNameVar = StringVar()
ProductNameLabel = Label(addFrame, textvariable=ProductNameVar)
ProductNameVar.set("Enter Product Name: ")
ProductNameLabel.grid(row = row_num+1, column=0)

# Product Name entry
NameEntry = Entry(addFrame)
NameEntry.grid(row=row_num+1, column=3)

# Label for "Enter Product Price: "
ProductPriceVar = StringVar()
ProductPriceLabel = Label(addFrame, textvariable=ProductPriceVar)
ProductPriceVar.set("Enter Price of the Product: ")
ProductPriceLabel.grid(row = row_num+2, column=0)

# Product Name entry
PriceEntry = Entry(addFrame)
PriceEntry.grid(row=row_num+2, column=3)

# Label for "Enter Product Rating: "
ProductRatingVar = StringVar()
ProductRatingLabel = Label(addFrame, textvariable=ProductRatingVar)
ProductRatingVar.set("Enter Rating of the Product: ")
ProductRatingLabel.grid(row = row_num+3, column=0)

# Product Name entry
RatingEntry = Entry(addFrame)
RatingEntry.grid(row=row_num+3, column=3)

# Label for "Enter Product Stock: "
ProductStockVar = StringVar()
ProductStockLabel = Label(addFrame, textvariable=ProductStockVar)
ProductStockVar.set("Enter Stock of the Product: ")
ProductStockLabel.grid(row = row_num+4, column=0)

# Product Name entry
StockEntry = Entry(addFrame)
StockEntry.grid(row=row_num+4, column=3)

# Label for "Enter Product Stock: "
ProductTypeVar = StringVar()
ProductTypeLabel = Label(addFrame, textvariable=ProductTypeVar)
ProductTypeVar.set("Enter the type of Product: ")
ProductTypeLabel.grid(row = row_num+5, column=0)

# Product Name entry
TypeEntry = Entry(addFrame)
TypeEntry.grid(row=row_num+5, column=3)

# Website dropdown
DropDownDict2 = {"Amazon" : 1, "Flipkart" : 2, "Snapdeal" : 3, "Shopclues" : 4}
websiteDropDownValue = StringVar(addFrame)
websiteDropDownValue.set("Amazon") # default value
websiteDropDown = OptionMenu(addFrame,
                    websiteDropDownValue,
                    *DropDownDict2.keys())
websiteDropDown.grid(row=row_num+6, column=0)

# Add Product button
Button(addFrame, text="Add Product", command=addProduct).grid(row=row_num+6,column=3)

################################################################################

# Data will be shown in this frame
lineFrame = Frame(root, bg='black')
lineFrame.pack(fill=BOTH)

################################################################################
deleteFrame = Frame(root)
deleteFrame.pack(pady=(padding,padding), padx=(padding, 0))

row_num = 0

# Label for "Delete Product Stock: "
DeleteProductVar = StringVar()
DeleteProductLabel = Label(deleteFrame, textvariable=DeleteProductVar)
DeleteProductVar.set("Delete Product Stock: ")
DeleteProductLabel.grid(row = row_num, column=2)

# Label for "Enter Product Name: "
ProductNameVar = StringVar()
ProductNameLabel = Label(deleteFrame, textvariable=ProductNameVar)
ProductNameVar.set("Enter Product Name: ")
ProductNameLabel.grid(row = row_num+1, column=0)

# Product Name entry
NameEntry = Entry(deleteFrame)
NameEntry.grid(row=row_num+1, column=3)

# Label for "Enter Product Stock: "
ProductStockVar = StringVar()
ProductStockLabel = Label(deleteFrame, textvariable=ProductStockVar)
ProductStockVar.set("Enter Stock to be deleted: ")
ProductStockLabel.grid(row = row_num+2, column=0)

# Product Name entry
StockEntry = Entry(deleteFrame)
StockEntry.grid(row=row_num+2, column=3)

# Website dropdown
websiteDropDownValue = StringVar(deleteFrame)
websiteDropDownValue.set("Amazon") # default value
websiteDropDown = OptionMenu(deleteFrame,
                    websiteDropDownValue,
                    *DropDownDict2.keys())
websiteDropDown.grid(row=row_num+3, column=0)

# Add Product button
Button(deleteFrame, text="Delete Product", command=deleteProduct).grid(row=row_num+3,column=3)

root.mainloop()
