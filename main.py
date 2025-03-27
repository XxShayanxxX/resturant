import tkinter as tk

from tkinter import ttk, messagebox

class ROM:
    def __init__(self, root):
        self.root = root
        self.root.title("Resturant Management System")

        self.menu_items = {
            
            "burger meal" : 3,
            "chicken meal" : 4,
            "pizza meal" : 5,
            "cheeseburger meal" : 6,
            "burger" : 2,
            "fries" : 1,
            "drink" : 1,
        }

        #self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        ttk.Label(frame, text = "Resturant Management System", font = ("Arial", 20)).grid(row = 0, columnspan = 2,padx=10 , pady=10)

        self.menu_label = {}    
        self.menu_entry = {}

        for i, (item,price) in enumerate(self.menu_items.items()):
            label = ttk.Label(frame, text = f'{item}  ${price}')   
            label.grid(row = i, column=0 , padx=10, pady=10)

            entry = ttk.Entry(frame, width= 5)
            entry.grid(row = i, column=1, padx=10, pady=10)




if __name__ == '__main__':
    root = tk.Tk()
    app = ROM(root)
    root.geometry("800x600")    
    root.mainloop()
