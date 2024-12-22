import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg = "navy")

Anime_title = "Dragon Ball"

def display_text(): 
    print(f"My favorite anime is {Anime_title}!")
button_print = tk.Button(root , text="Anime Character",command=display_text)
button_print.grid(row=10, column=10, padx=200, pady=100)

root.mainloop()
