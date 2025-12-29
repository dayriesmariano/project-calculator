import tkinter as tk

def press(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(num))
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 20),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
display.pack(fill="both", padx=10, pady=10)
buttons_frame = tk.Frame(window)
buttons_frame.pack()

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('0', 3, 1)
]

for (text, row, col) in buttons:
    tk.Button(
        buttons_frame,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda t=text: press(t)
    ).grid(row=row, column=col, padx=5, pady=5)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
tk.Button(buttons_frame, text="+", width=5, height=2,
          command=lambda: press("+")).grid(row=0, column=3)

tk.Button(buttons_frame, text="-", width=5, height=2,
          command=lambda: press("-")).grid(row=1, column=3)

tk.Button(buttons_frame, text="*", width=5, height=2,
          command=lambda: press("*")).grid(row=2, column=3)

tk.Button(buttons_frame, text="/", width=5, height=2,
          command=lambda: press("/")).grid(row=3, column=3)

tk.Button(buttons_frame, text="=", width=5, height=2,
          command=calculate).grid(row=3, column=2)

tk.Button(buttons_frame, text="C", width=5, height=2,
          command=clear).grid(row=3, column=0)

                    

window.mainloop()
