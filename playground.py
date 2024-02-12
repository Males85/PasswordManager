# from tkinter import *
#
# window = Tk()
#
# button = Button(text="Obrad")
# button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # padx and pady for padding, sticky="ew" for horizontal expansion
#
# entry = Entry()
# entry.insert(END, string="Napisi nesto")
# entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)

# window.mainloop()
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

pass_letters = [random.choice(letters) for _ in range(nr_letters)]
pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = pass_letters + pass_symbols + pass_numbers

print(password_list)