from tkinter import messagebox

class BadChar(Exception): 
    def __init__(self):
        super().__init__(self)
        messagebox.showinfo("Error","Mozna wprowadzać tylko cyfry")  
        
class BadSize(Exception):
    def __init__(self,temp):
        super().__init__(self)
        if temp == 1:
            messagebox.showinfo("Error","Wprowadzono za malo liczb")  
        else:
            messagebox.showinfo("Error","Wprowadzono za duzo liczb")
