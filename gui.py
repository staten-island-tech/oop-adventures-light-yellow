# import tkinter as tk

# root = tk.Tk()
# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# # Setting some window properties
# root.title("Tk Example")
# root.configure(background="yellow")
# root.minsize(200, 200)
# root.maxsize(1000, 1000)
# root.geometry("300x300+50+50")

# root.mainloop()

import tkinter as tk

# Create the window
# root = tk.Tk()
# root.title("My GUI")
# root.geometry("300x200")

# # Function that runs when button is clicked
# def say_hello():
#     label.config(text="Button clicked!")

# # Create a label
# label = tk.Label(root, text="Press the button")
# label.pack(pady=20)

# # Create a button
# button = tk.Button(
#     root,
#     text="Click Me",
#     command=say_hello
# )

# button.pack()

# # Start the GUI loop
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Function for button click
def clicked():
    print("Image button clicked!")

# Load image
image = tk.PhotoImage(file="button-24843_1280.png")

# Create button with image
button = tk.Button(
    root,
    image=image,
    command=clicked,
    borderwidth=0
)

button.pack(pady=20)

root.mainloop()