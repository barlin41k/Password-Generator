from os import system
import random
import string
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
except:
    system("pip install tkinter")
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

def generate_password(length, use_lower, use_upper, use_digits, use_punctuation, use_spaces):
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if use_spaces:
        characters += ' '

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_button_clicked(event=None):
    try:
        length = int(entry_Dann.get())
        if length <= 0:
            entry_Dann.delete(0, END)
            messagebox.showwarning(title="Ошибка", message="Пожалуйста, выберите положительное значение для длины пароля.")
            return
    except ValueError:
        entry_Dann.delete(0, END)
        messagebox.showwarning(title="Ошибка", message="Пожалуйста, введите числовое значение для длины пароля.")
        return

    use_lower = lowercase_var.get()
    use_upper = uppercase_var.get()
    use_digits = digits_var.get()
    use_punctuation = punctuation_var.get()
    use_spaces = spaces_var.get()
    
    if use_lower or use_upper or use_digits or use_punctuation or use_spaces:
        password = generate_password(length, use_lower, use_upper, use_digits, use_punctuation, use_spaces)
        messagebox.showinfo(title="Сгенерированный пароль", message=password)
    else:
        messagebox.showwarning(title="Ошибка", message="Пожалуйста, выберите хотя бы одну опцию для составления пароля.")

root = Tk()
root.geometry("420x250")
root.title("Password Generator")
root.iconbitmap("Key.ico")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10), foreground="blue")
style.configure("TCheckbutton", font=("Arial", 10), foreground="black")
style.configure("TButton", font=("Arial", 10), foreground="black", background="black")


entry_Label = ttk.Label(text="Длина пароля:")
entry_Label.grid(column=0, row=0, padx=20, pady=10)
entry_Dann = ttk.Entry(width=10, font=("Arial", 12))
entry_Dann.grid(column=1, row=0, padx=20, pady=10)
entry_Button = ttk.Button(text="Сгенерировать", command=generate_button_clicked)
entry_Button.grid(column=0, row=1, columnspan=2, padx=20, pady=10)
entry_Button.bind("<Return>", generate_button_clicked)
entry_Dann.bind("<Return>", generate_button_clicked)
root.bind("<Return>", generate_button_clicked)

lowercase_var = IntVar()
lowercas = ttk.Checkbutton(text="Нижний регистр", variable=lowercase_var)
lowercas.grid(column=2, row=0, padx=20, pady=10)

uppercase_var = IntVar()
uppercas = ttk.Checkbutton(text="Верхний регистр", variable=uppercase_var)
uppercas.grid(column=2, row=1, padx=20, pady=10)

digits_var = IntVar()
digits = ttk.Checkbutton(text="Цифры", variable=digits_var)
digits.grid(column=2, row=2, padx=20, pady=10)

punctuation_var = IntVar()
punctuation = ttk.Checkbutton(text="Пунктуация", variable=punctuation_var)
punctuation.grid(column=2, row=3, padx=20, pady=10)

spaces_var = IntVar()
spaces = ttk.Checkbutton(text="Пробелы", variable=spaces_var)
spaces.grid(column=2, row=4, padx=20, pady=10)

root.mainloop()
