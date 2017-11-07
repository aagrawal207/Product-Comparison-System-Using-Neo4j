from neo4j.v1 import GraphDatabase, basic_auth
try:
    from Tkinter import *
    from Tkinter import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "neo4j"))
session = driver.session()

# Window is created here
root = Tk()
root.title("Product-Comparison-System-Using-Neo4j")

searchFrame = Frame(root)
searchFrame.pack()

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
searchBar = Entry(searchFrame, width=50, fg = "gray")
searchBar.bind("<Button-1>", callback)   # Bind a mouse-click to the callback function.
searchBar.insert(0, 'Search for a product...')
searchBar.pack(side=LEFT, fill=Y)

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
fromEntry = Entry(searchFrame, width=5)
fromEntry.pack(side=LEFT)

# Label for "to: "
PriceRangeVariableTo = StringVar()
PriceRangeLabelTo = Label(searchFrame, textvariable=PriceRangeVariableTo)
PriceRangeVariableTo.set(" to: ")
PriceRangeLabelTo.pack(side=LEFT)

# To entry
toEntry = Entry(searchFrame, width=5)
toEntry.pack(side=LEFT)

# This method is called when button is clicked
def go():
    result = session.run("MATCH (a:Book)-[:PUBLISHED_BY]->(b:Publishing_House) return a.title as a,b.name as b")
    for record in result:
        print("%s %s" % (record["a"], record["b"]))
        PriceRangeVariableTo.set(record["a"])
        time.sleep(1)
    print(searchBar.get())
    print(ratingDropDownValue.get())
    print(fromEntry.get())
    print(toEntry.get())

# Submit button for searching
Button(searchFrame, text="Go!", command=go).pack(side=LEFT)

# Data will be shown in this frame
dataFrame = Frame(root)
dataFrame.pack(side=BOTTOM)

# Footer starts here
footer = Frame(root)
footer.pack(side = BOTTOM)
searchRow = 0

# Label for "For admin: "
ForAdminVariable = StringVar()
ForAdminLabel = Label(footer, textvariable=ForAdminVariable)
ForAdminVariable.set("For admin: ")
ForAdminLabel.pack(side=LEFT)

# Add Product button
Button(footer, text="Add Product").pack(side=LEFT)

# DELETE PRODUCT button
Button(footer, text="Delete Product").pack(side=LEFT)

root.mainloop()
