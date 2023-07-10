import tkinter as tk

window = tk.Tk()
window.title("GUI Calculator")

# Create an entry widget to display the result
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

def clear():
  # Clear the entry widget
  entry.delete(0, tk.END)

def append(char):
  # Append a character to the entry widget
  global entry
  entry.insert(tk.END, char)
  if char == "=":
    evaluate()

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
  ["0", ".", "=", ""]
]

# Add buttons to the window using a loop
for i in range(len(buttons)):
  for j in range(len(buttons[i])):
    # Get the text of the button
    text = buttons[i][j]
    # Create a lambda function for the command
    command = lambda char=text: append(char) if char != "=" else evaluate()
    # Create a button widget
    button = tk.Button(window, text=text, width=5, command=command)
    # Add the button to the window
    button.grid(row=i+1, column=j)

# Add a special button for clearing the entry widget
clear_button = tk.Button(window, text="Clear", width=22, command=clear)
clear_button.grid(row=6, column=0, columnspan=4)

# Make the window resizable
window.resizable(True, True)

# Start the main loop of the window
window.mainloop()
