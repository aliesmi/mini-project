import random
import tkinter as tk 
from tkinter import messagebox

def start():
    global secret
    secret = random.randint(1,10)
    entry.delete(0,tk.END)
    result_label.config(text="Please enter a number within 1 to 10",fg="white")

def get_guess():
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Warning","Please enter a number!")
        return

    if guess == secret:
        result_label.config(text=f"congelatulations! secret number is {secret}." , fg="green" , bg="white", font="bold")
        play_again = messagebox.askyesno("Finish" , "play again?")
        if play_again:
            start()
        else:
            window.destroy()
    elif guess > secret:
        result_label.config(text="too low! try again.")  
    else:
        result_label.config(text="too high! try again.")


window = tk.Tk()
window.title("game")
window.geometry("300x200")
window.configure(bg="blue")

label = tk.Label(window, text="Please Enter a Number within 1 to 10" , bg="blue" , fg="white" , font="bold")
label.pack(pady=15)

entry = tk.Entry(window, justify="center" , bg="white" , fg="black" , width=30 , border=4)
entry.pack(pady=5)

button = tk.Button(window, text="Enter" , bg="white" , fg="black" ,activebackground="black" , activeforeground="white", command=get_guess)
button.pack(pady=10)

result_label = tk.Label(window, text="" , bg="blue" , fg="orange")
result_label.pack(pady=10)


start()
window.mainloop()
