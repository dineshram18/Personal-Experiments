import tkinter as tk

def greet():
    name = entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Simple Greeting App")

# Create an input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to trigger the greeting
greet_button = tk.Button(root, text="Greet Me", command=greet)
greet_button.pack(pady=5)

# Label to display the greeting
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
