import tkinter as tk

your_name = "JohnRey_Camacho"
your_section = "BSIT-2A"
root = tk.Tk()
root.title(f"OOP")
root.geometry("500x500")
root.configure(bg = "#000080")


label = tk.Label(text=f"OOP LA29 {your_name} {your_section}")
label.grid(row=10, column=10, padx=140 , pady=100)


root.mainloop()
