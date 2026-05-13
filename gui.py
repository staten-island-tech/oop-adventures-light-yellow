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

# import tkinter as tk

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

# Create window
root = tk.Tk()
root.title("Image Button Example")

# Load image
photo = tk.PhotoImage(file="button.png")
small_image = photo.subsample(2,2)
# Function when button is clicked
def on_click():
    print("Button clicked!")

# Create image button
button = tk.Button(root, image=small_image, command=on_click, borderwidth=0)
button.pack(pady=20)

# Run app
root.mainloop()