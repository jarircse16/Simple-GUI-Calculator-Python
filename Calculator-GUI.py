import tkinter as tk

# Function to perform addition
def add():
    try:
        num1 = float(entry_num1.get())  # Get the value entered in the first entry field and convert it to a float
        num2 = float(entry_num2.get())  # Get the value entered in the second entry field and convert it to a float
        result = num1 + num2  # Perform the addition operation
        label_result.config(text="Result: " + str(result))  # Update the result label with the computed result
    except ValueError:
        label_result.config(text="Error: Invalid input")  # Handle the case where the input is not a valid number

# Function to perform subtraction
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Function to perform division
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            result = num1 / num2
            label_result.config(text="Result: " + str(result))
        else:
            label_result.config(text="Error: Cannot divide by zero")
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input entry fields
entry_num1 = tk.Entry(window)  # Create an entry field for the first number
entry_num1.pack()  # Display the entry field in the window

entry_num2 = tk.Entry(window)  # Create an entry field for the second number
entry_num2.pack()  # Display the entry field in the window

# Create buttons for each operation
button_add = tk.Button(window, text="Add", command=add)  # Create an "Add" button that calls the add() function
button_add.pack()  # Display the "Add" button in the window

button_subtract = tk.Button(window, text="Subtract", command=subtract)  # Create a "Subtract" button that calls the subtract() function
button_subtract.pack()  # Display the "Subtract" button in the window

button_multiply = tk.Button(window, text="Multiply", command=multiply)  # Create a "Multiply" button that calls the multiply() function
button_multiply.pack()  # Display the "Multiply" button in the window

button_divide = tk.Button(window, text="Divide", command=divide)  # Create a "Divide" button that calls the divide() function
button_divide.pack()  # Display the "Divide" button in the window

# Create a label to display the result
label_result = tk.Label(window)  # Create an empty label for displaying the result
label_result.pack()  # Display the label in the window

# Start the main event loop
window.mainloop()
