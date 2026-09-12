import tkinter as tk


def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def calculate():
    expression = display.get()

    if not expression:
        return

    try:
        result = eval(expression, {"__builtins__": None}, {})
        clear_display()
        display.insert(0, result)
    except (SyntaxError, TypeError, ZeroDivisionError):
        clear_display()
        display.insert(0, "Error")


def button_click(value):
    if value == "C":
        clear_display()
    elif value == "=":
        calculate()
    else:
        if display.get() == "Error":
            clear_display()

        value = value.replace("×", "*").replace("÷", "/")
        add_to_display(value)


window = tk.Tk()
window.title("Python Calculator")
window.geometry("350x500")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=0
)

display.pack(
    padx=15,
    pady=20,
    fill="x",
    ipady=15
)

buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    [".", "0", "C", "+"],
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(
        expand=True,
        fill="both"
    )

    for value in row:
        tk.Button(
            frame,
            text=value,
            font=("Arial", 18),
            command=lambda v=value: button_click(v)
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )

tk.Button(
    window,
    text="=",
    font=("Arial", 20),
    command=calculate
).pack(
    fill="both",
    padx=15,
    pady=10,
    ipady=8
)

window.mainloop()