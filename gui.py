import tkinter as tk

# create window
root = tk.Tk()
root.title("Image Button Example")
root.attributes('-fullscreen',True)

# Load image (must be .png or .gif for standard PhotoImage)
bg_image = tk.PhotoImage(file="schoolbackground.webp")

# Create label and 'place' it to fill the whole window
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)



# Load image
photo = tk.PhotoImage(file="button.png")
small_image = photo.subsample(5,5)
# Function when button is clicked
def on_click():
    print("Button clicked!")

# Create image button
button = tk.Button(root, image=small_image, command=on_click, borderwidth=0)
button.pack(pady=20)
button.place(x=100, y=700)

# Run app
root.mainloop()

# this code above is an example of how we'll interact with the game. the def function is gonna run certain parts of our game which will be referenced with command. our different buttons will interact with the game