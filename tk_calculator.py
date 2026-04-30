import tkinter as tk
from tkinter import messagebox
import math   # NEW: for square root


def calculate(op):
    try:
        n1 = float(entry1.get())

        # For operations needing 2 numbers
        if op in ["+", "-", "*", "/"]:
            n2 = float(entry2.get())

        if op == "+":
            res = n1 + n2

        elif op == "-":
            res = n1 - n2

        elif op == "*":
            res = n1 * n2

        elif op == "/":
            if n2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            res = n1 / n2

        # NEW: Square
        elif op == "square":
            res = n1 ** 2

        # NEW: Square Root
        elif op == "sqrt":
            if n1 < 0:
                messagebox.showerror("Error", "Cannot find square root of negative number")
                return
            res = math.sqrt(n1)

        result_var.set(str(res))

    except:
        messagebox.showerror("Error", "Enter valid numbers")


root = tk.Tk()
root.title("Calculator")
root.geometry("350x350")  # slightly increased height


tk.Label(root, text=" Calculator", font=("Arial", 16, "bold")).pack(pady=10)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1, padx=5, pady=5)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+", width=8, command=lambda: calculate("+")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="-", width=8, command=lambda: calculate("-")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="*", width=8, command=lambda: calculate("*")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="/", width=8, command=lambda: calculate("/")).grid(row=1, column=1, padx=5, pady=5)

# NEW BUTTONS
tk.Button(btn_frame, text="x²", width=8, command=lambda: calculate("square")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="√x", width=8, command=lambda: calculate("sqrt")).grid(row=2, column=1, padx=5, pady=5)


result_var = tk.StringVar()

result_frame = tk.Frame(root)
result_frame.pack(pady=15)

tk.Label(result_frame, text="Result:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5)

result_entry = tk.Entry(result_frame, textvariable=result_var, font=("Arial", 12), width=20, state="readonly")
result_entry.grid(row=0, column=1, padx=5)


# Run
root.mainloop()