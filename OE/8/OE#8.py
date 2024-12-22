import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg = "navy")

name = tk.Entry(root)
name.grid(row=0 , column=0, padx=20)
calculate = 1
def display_text():
    global calculate
    print(f"{calculate}. {name.get()}")
    calculate += 1
button_print = tk.Button(root , text="Submit",command=display_text)
button_print.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
