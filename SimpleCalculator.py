from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
root = Tk()
root.title("Advanced Calculator")
root.geometry("600x700")
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

memory = 0
history = []
last_result="0"

light_theme = {"bg": "white", "fg": "black"}
dark_theme = {"bg": "#2e2e2e", "fg": "white"}
current_theme = light_theme

entry = Entry(root, width=18, font=('Arial', 28), bd=10, borderwidth=4, relief='ridge')
entry.grid(row=0, column=0, columnspan=6)

history_box = Text(root, width=30, height=6, font=('Arial', 10))
history_box.grid(row=1, column=0, columnspan=5)

def update_theme():
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    root.config(bg=current_theme["bg"])
    entry.config(bg=current_theme["bg"], fg=current_theme["fg"])
    history_box.config(bg=current_theme["bg"], fg=current_theme["fg"])

def click(number):
    entry.insert(END, str(number))



def update_history():
    history_box.delete("1.0", END)
    for item in history[-5:]:
        history_box.insert(END, item + "\n")

def percentage():
    try:
        result = str(float(entry.get()) / 100)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def absolute_value():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(abs(value)))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def factorial():
    try:
        value = int(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.factorial(value)))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, END)
        entry.insert(0, str(result))
        history.append(f"√{value} = {result}")
        update_history()
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

def sin_func():
    try:
        expression = entry.get()
        value = float(eval(expression))  
        result = math.sin(math.radians(value))
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def cos_func():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        
def tan_func():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.tan(math.radians(value))))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def log_func():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def pi_func():
    entry.insert(END, str(math.pi))

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    entry.delete(0, END)
    entry.insert(0, str(memory))

def memory_add():
    global memory
    try:
        memory += float(entry.get())
    except:
        pass       
def memory_subtract():
    global memory
    try:
        memory -= float(entry.get())
    except:
        pass
def square():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(value ** 2))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def cube():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(value ** 3))
    except:
        entry.delete(0, END)
        entry.insert(0,"Error")
def exp_func():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.exp(value)))
    except:
        entry.delete(0, END)
        entry.insert(0,"Error")
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def plot_graph():
    try:
        expression = entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(expression)
        plt.plot(x, y)
        plt.title(f'Graph of {expression}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
def clear():
    entry.delete(0, END)
def equal():
     try:
            result = str(eval(entry.get().replace("^", "")))
            history.append(entry.get() + " = " + result)
            update_history()
            entry.delete(0, END)
            entry.insert(0, result)
     except:
            entry.delete(0, END)
            entry.insert(0, "Error")

def recall_ans():
    entry.insert(END, last_result)
def clear_history():
    history.clear()
    history_box.delete("1.0", END)
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3), ('MC', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('MR', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3), ('M+', 4, 4),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('/', 5, 3), ('M-', 5, 4),
    ('%', 6, 0), ('.', 6, 1), ('√', 6, 2), ('⌫', 6, 3), ('|x|', 6, 4),
    ('^', 7, 0), ('n!', 7, 1), ('sin', 7, 2), ('cos', 7, 3), ('tan', 7, 4),
    ('log', 8, 0), ('π', 8, 1), ('Theme', 8, 2), ('(', 8, 3), (')', 8, 4),
    ('x', 9, 0), ('x²', 9, 1), ('x³', 9, 2),('eˣ', 9, 3), ('e', 9, 4),
    ('Graph', 10, 0), ('Ans', 10, 1), ('clear history', 10, 2)
]

for (text, row, col) in buttons: 
    cmd=lambda t=text:click(t)
    
    if text == '%': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=percentage).grid(row=row, column=col, sticky="nsew")
    elif text == 'sqrt': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=square_root).grid(row=row, column=col, sticky="nsew") 
    elif text == '⌫': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=backspace).grid(row=row, column=col, sticky="nsew") 
    elif text == '|x|': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=absolute_value).grid(row=row, column=col, sticky="nsew") 
    elif text == '^': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda: click('^')).grid(row=row, column=col, sticky="nsew") 
    elif text == 'n!':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=factorial).grid(row=row, column=col, sticky="nsew") 
    elif text == 'sin': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=sin_func).grid(row=row, column=col, sticky="nsew") 
    elif text == 'cos': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=cos_func).grid(row=row, column=col, sticky="nsew") 
    elif text == 'tan':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=tan_func).grid(row=row, column=col, sticky="nsew") 
    elif text == 'log': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=log_func).grid(row=row, column=col, sticky="nsew") 
    elif text == 'π': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=pi_func).grid(row=row, column=col, sticky="nsew")
    elif text == 'MC':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=memory_clear).grid(row=row, column=col, sticky="nsew")
    elif text == 'MR':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=memory_recall).grid(row=row, column=col, sticky="nsew")
    elif text == 'M+':
             Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=memory_add).grid(row=row, column=col, sticky="nsew")
    elif text == 'M-':
             Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=memory_subtract).grid(row=row, column=col, sticky="nsew")
    elif text == 'Theme':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=update_theme).grid(row=row, column=col, sticky="nsew")
    elif text == '(':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda: click('(')).grid(row=row, column=col, sticky="nsew")
    elif text == ')':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda: click(')')).grid(row=row, column=col, sticky="nsew")
    elif text == 'x²':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=cube).grid(row=row, column=col, sticky="nsew")
    elif text == 'x³':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=square).grid(row=row, column=col, sticky="nsew")
    elif text == 'eˣ':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=exp_func).grid(row=row, column=col, sticky="nsew")
    elif text == 'Graph':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=plot_graph).grid(row=row, column=col, sticky="nsew")
    elif text == 'C': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=clear).grid(row=row, column=col, sticky="nsew")
    elif text == '=': 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=equal).grid(row=row, column=col, sticky="nsew") 
    elif text == 'Ans':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=recall_ans).grid(row=row, column=col, sticky="nsew")
    elif text == 'clear history':
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=clear_history).grid(row=row, column=col, sticky="nsew")
    else: 
            Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: click(t)).grid(row=row, column=col, sticky="nsew")
for i in range(11):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)
root.mainloop()