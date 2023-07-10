import tkinter as tk

window = tk.Tk()
window.title("Scientific Calculator")

# Create an entry widget to display the result
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

def clear():
  # Clear the entry widget
  entry.delete(0, tk.END)

def append(char):
  # Append a character to the entry widget
  global entry
  if callable(char):
    char(entry.get())
  else:
    entry.insert(tk.END, char)

def evaluate():
  # Evaluate the expression in the entry widget
  try:
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)
  except:
    entry.delete(0, tk.END)
    entry.insert(0, "Error")

# Create buttons for digits and operators
buttons = [
  ["C", "/", "*", "-"],
  ["7", "8", "9", "+"],
  ["4", "5", "6", "("],
  ["1", "2", "3", ")"],
  ["0", ".", "=", "exp"],
  ["pi", "sin", "cos", "tan"],
  ["log", "ln", "sqrt", "pow"],
  ["sin-1", "cos-1", append, "cosec"],
  ["sec", "cot", "cosec-1", "sec-1"],
  ["sinh", "cosh", "tanh", "coth"],
  ["sech", "csch", "tanh-1", "coth-1"],
  ["+", "-", "*", "/"],
  ["Clear"],
]

# Add buttons to the window using a loop
for i in range(len(buttons)):
  for j in range(len(buttons[i])):
    # Get the text of the button
    text = buttons[i][j]
    # Create a lambda function for the command
    command = lambda char=text: append(char) if char != "=" else evaluate()
    # Set the command attribute of the button
    button = tk.Button(window, text=text, width=5, command=command)
    # Add the button to the window
    button.grid(row=i+1, column=j)

# Remove the extra button
for i in range(len(buttons)):
  for j in range(len(buttons[i])):
    if buttons[i][j] == "90752<":
      button = tk.Button(window, text="", width=5, command=None)
      button.grid(row=i+1, column=j)

# Make the window resizable
window.resizable(True, True)

# Start the main loop of the window
window.mainloop()
import tkinter as tk

window = tk.Tk()
window.title("Scientific Calculator")

# Create an entry widget to display the result
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

def clear():
  # Clear the entry widget
  global entry
  entry.delete(0, tk.END)

def append(char):
  # Append a character to the entry widget
  global entry
  if callable(char):
    char(entry.get())
  else:
    entry.insert(tk.END, char)

def evaluate():
  # Evaluate the expression in the entry widget
  try:
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)
  except:
    entry.delete(0, tk.END)
    entry.insert(0, "Error")

# Create buttons for digits and operators
buttons = [
  ["C", "/", "*", "-"],
  ["7", "8", "9", "+"],
  ["4", "5", "6", "("],
  ["1", "2", "3", ")"],
  ["0", ".", "=", "exp"],
  ["pi", "sin", "cos", "tan"],
  ["log", "ln", "sqrt", "pow"],
  ["sin-1", "cos-1", append, "cosec"],
  ["sec", "cot", "cosec-1", "sec-1"],
  ["sinh", "cosh", "tanh", "coth"],
  ["sech", "csch", "tanh-1", "coth-1"],
  ["+", "-", "*", "/"],
  ["Clear"],
]

# Add buttons to the window using a loop
for i in range(len(buttons)):
  for j in range(len(buttons[i])):
    # Get the button text
    button = buttons[i][j]

    # Create a button widget
    button = tk.Button(window, text=str(button[0]), width=5, command=button[0])

    # Add the button to the window
    button.grid(row=i+1, column=j)

# Make the window resizable
window.resizable(True, True)

# Start the main loop of the window
window.mainloop()
