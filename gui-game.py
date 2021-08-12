import tkinter as tk


def initial(event):
    print("Well %s... I am thinking of a number between 1 and 100.\n" % (name.get()))
    print('I want you to guess the number.')
    print('You have 8 guesses\n')


window = tk.Tk()
window.title("Number guessing game")
window.geometry('650x300')

welcome_msg = tk.Label(window, text="Hey there! What is your name?", font=("Adobe Garamond Pro", 12))
welcome_msg.pack()
welcome_msg.grid(row=0, column=0)

name = tk.Entry(window)
name.grid(row=1, column=0)
name.bind('<Return>', initial)

window.mainloop()
