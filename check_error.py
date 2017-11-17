import tkinter
import tkinter.messagebox

def error_msg():
    tkinter.messagebox.showinfo("Error", "One of the entries do not have correct datatype.")

def int_check(s):
    if s.isnumeric():
        return True

    return False

def float_check(s):
    if(int_check(s)):
        return True;
    try:
        b = float(s)
        if '.' in s:
            return True
        return False
    except ValueError:
        return False

def string_check(s):
    if s.isalpha():
        return True
    return False
