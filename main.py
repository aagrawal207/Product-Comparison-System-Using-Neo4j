from tkinter import *
from tkinter import ttk
from queries import *

################################################################################
def addProduct():
    name = (NameEntry.get()).lower()
    website = (websiteDropDownValue.get()).lower()
    add_queries(name, website, PriceEntry.get(), StockEntry.get(), float(RatingEntry.get()), (TypeEntry.get()).lower())

def deleteProduct():
    name = (NameEntry2.get()).lower()
    website =(websiteDropDownValue2.get()).lower()
    delete_queries(name, website, StockEntry2.get())

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

################################################################################
# Data will be shown in this frame
lineFrame = Frame(root, bg='black')
lineFrame.pack(fill=BOTH)
################################################################################

global dataFrame
dataFrame = Frame(root)
dataFrame.pack(fill=BOTH,expand=True)

def show_all():
    result = show_all_queries()
    # for record in result:
        # print(record["name"],record["type"],record["rating"],record["website"],record["price"], record["type"])
    global dataFrame
    for widget in dataFrame.winfo_children():
        widget.grid_forget()
    pad = 60
    NameVar = StringVar()
    NameLabel = Label(dataFrame, textvariable=NameVar, font='Helvetica 14 bold')
    NameVar.set("Name")
    NameLabel.grid(row=0, column=0, sticky=NSEW, padx=(pad, pad))
    TypeVar = StringVar()
    TypeLabel = Label(dataFrame, textvariable=TypeVar, font='Helvetica 14 bold')
    TypeVar.set("Type")
    TypeLabel.grid(row=0, column=1, sticky=NSEW, padx=(pad, pad))
    result1 = show_all_queries()
    i = 1
    col = 0
    for record in result1:
        pad = 60
        NameVar = StringVar()
        NameLabel = Label(dataFrame, textvariable=NameVar)
        NameVar.set(record["name"])
        NameLabel.grid(row=i, column=2*col, sticky=NSEW, padx=(pad, pad))
        TypeVar = StringVar()
        TypeLabel = Label(dataFrame, textvariable=TypeVar)
        TypeVar.set(record["type"])
        TypeLabel.grid(row=i, column=2*col+1, sticky=NSEW, padx=(pad, pad))
        i += 1
        if(i >= 15):
            col += 1
            i = 1
            NameVar = StringVar()
            NameLabel = Label(dataFrame, textvariable=NameVar, font='Helvetica 14 bold')
            NameVar.set("Name")
            NameLabel.grid(row=0, column=2*col, sticky=NSEW, padx=(pad, pad))
            TypeVar = StringVar()
            TypeLabel = Label(dataFrame, textvariable=TypeVar, font='Helvetica 14 bold')
            TypeVar.set("Type")
            TypeLabel.grid(row=0, column=2*col+1, sticky=NSEW, padx=(pad, pad))

def go():
    prod = searchBar.get().lower()
    rating = ratingDropDownValue.get().lower()
    rating = int(rating[-1])
    result1, result2 = go_queries(prod, fromEntry.get(), toEntry.get(), rating)
    if result1 == False and result2 == False:
        return False
    count = 0
    for record in result1:
        if prod in record["name"]:
            count += 1
            # print("%s %s %s %s %s" % (record["name"],record["price"], record["rating"], record["website"], record["type"]))
    for record in result2:
        count += 1
        # print("%s %s %s %s %s" % (record["name"],record["price"], record["rating"], record["website"], record["type"]))
    global dataFrame
    for widget in dataFrame.winfo_children():
        widget.grid_forget()
    if count > 0:
        pad = 60
        NameVar = StringVar()
        NameLabel = Label(dataFrame, textvariable=NameVar, font='Helvetica 14 bold')
        NameVar.set("Name")
        NameLabel.grid(row=0, column=0, sticky=NSEW, padx=(pad, pad))
        PriceVar = StringVar()
        PriceLabel = Label(dataFrame, textvariable=PriceVar, font='Helvetica 14 bold')
        PriceVar.set("Price")
        PriceLabel.grid(row=0, column=1, sticky=NSEW, padx=(pad, pad))
        RatingVar = StringVar()
        RatingLabel = Label(dataFrame, textvariable=RatingVar, font='Helvetica 14 bold')
        RatingVar.set("Rating")
        RatingLabel.grid(row=0, column=2, sticky=NSEW, padx=(pad, pad))
        WebsiteVar = StringVar()
        WebsiteLabel = Label(dataFrame, textvariable=WebsiteVar, font='Helvetica 14 bold')
        WebsiteVar.set("Website")
        WebsiteLabel.grid(row=0, column=3, sticky=NSEW, padx=(pad, pad))
        TypeVar = StringVar()
        TypeLabel = Label(dataFrame, textvariable=TypeVar, font='Helvetica 14 bold')
        TypeVar.set("Type")
        TypeLabel.grid(row=0, column=4, sticky=NSEW, padx=(pad, pad))
        result1, result2 = go_queries(prod, fromEntry.get(), toEntry.get(), rating)
        i = 1
        for record in result1:
            if prod in record["name"]:
                pad = 60
                NameVar = StringVar()
                NameLabel = Label(dataFrame, textvariable=NameVar)
                NameVar.set(record["name"])
                NameLabel.grid(row=i, column=0, sticky=NSEW, padx=(pad, pad))
                PriceVar = StringVar()
                PriceLabel = Label(dataFrame, textvariable=PriceVar)
                PriceVar.set(record["price"])
                PriceLabel.grid(row=i, column=1, sticky=NSEW, padx=(pad, pad))
                RatingVar = StringVar()
                RatingLabel = Label(dataFrame, textvariable=RatingVar)
                RatingVar.set(record["rating"])
                RatingLabel.grid(row=i, column=2, sticky=NSEW, padx=(pad, pad))
                WebsiteVar = StringVar()
                WebsiteLabel = Label(dataFrame, textvariable=WebsiteVar)
                WebsiteVar.set(record["website"])
                WebsiteLabel.grid(row=i, column=3, sticky=NSEW, padx=(pad, pad))
                TypeVar = StringVar()
                TypeLabel = Label(dataFrame, textvariable=TypeVar)
                TypeVar.set(record["type"])
                TypeLabel.grid(row=i, column=4, sticky=NSEW, padx=(pad, pad))
                i += 1
        for record in result2:
            pad = 60
            NameVar = StringVar()
            NameLabel = Label(dataFrame, textvariable=NameVar)
            NameVar.set(record["name"])
            NameLabel.grid(row=i, column=0, sticky=NSEW, padx=(pad, pad))
            PriceVar = StringVar()
            PriceLabel = Label(dataFrame, textvariable=PriceVar)
            PriceVar.set(record["price"])
            PriceLabel.grid(row=i, column=1, sticky=NSEW, padx=(pad, pad))
            RatingVar = StringVar()
            RatingLabel = Label(dataFrame, textvariable=RatingVar)
            RatingVar.set(record["rating"])
            RatingLabel.grid(row=i, column=2, sticky=NSEW, padx=(pad, pad))
            WebsiteVar = StringVar()
            WebsiteLabel = Label(dataFrame, textvariable=WebsiteVar)
            WebsiteVar.set(record["website"])
            WebsiteLabel.grid(row=i, column=3, sticky=NSEW, padx=(pad, pad))
            TypeVar = StringVar()
            TypeLabel = Label(dataFrame, textvariable=TypeVar)
            TypeVar.set(record["type"])
            TypeLabel.grid(row=i, column=4, sticky=NSEW, padx=(pad, pad))
            i += 1
    else:
        pad = 60
        InfoVar = StringVar()
        InfoLabel = Label(dataFrame, textvariable=InfoVar)
        InfoVar.set("No results to show.")
        InfoLabel.grid(row=0, column=0, padx=(pad, pad))

# Submit button for searching
Button(searchFrame, text="Go!", command=go).pack(side=LEFT, padx=(10,0))
# Show All button
Button(searchFrame, text="Show All", command=show_all).pack(side=LEFT, padx=(10,0))
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
ProductNameVar2 = StringVar()
ProductNameLabel2 = Label(deleteFrame, textvariable=ProductNameVar2)
ProductNameVar2.set("Enter Product Name: ")
ProductNameLabel2.grid(row = row_num+1, column=0)
# Product Name entry
NameEntry2 = Entry(deleteFrame)
NameEntry2.grid(row=row_num+1, column=3)
# Label for "Enter Product Stock: "
ProductStockVar2 = StringVar()
ProductStockLabel2 = Label(deleteFrame, textvariable=ProductStockVar2)
ProductStockVar2.set("Enter Stock to be deleted: ")
ProductStockLabel2.grid(row = row_num+2, column=0)
# Product Name entry
StockEntry2 = Entry(deleteFrame)
StockEntry2.grid(row=row_num+2, column=3)
# Website dropdown
websiteDropDownValue2 = StringVar(deleteFrame)
websiteDropDownValue2.set("Amazon") # default value
websiteDropDown2 = OptionMenu(deleteFrame,
                    websiteDropDownValue2,
                    *DropDownDict2.keys())
websiteDropDown2.grid(row=row_num+3, column=0)
# Add Product button
Button(deleteFrame, text="Delete Product", command=deleteProduct).grid(row=row_num+3,column=3)

show_all()

root.mainloop()
