import tkinter as tk

root = tk.Tk()
root.title("Image Button Example")
root.attributes('-fullscreen',True)
bg_image = tk.PhotoImage(file="1200.png")
bg2 = bg_image.zoom(2)
bg_label = tk.Label(root, image=bg2)
bg_label.place(relwidth=1, relheight=1)
# this above code is the background of the game, should be on always


# photo = tk.PhotoImage(file="button.png")
# small_image = photo.subsample(5,5)

# def on_click():
#     print("Button clicked!")


# button = tk.Button(root, image=small_image, command=on_click, borderwidth=0)
# button.pack(pady=20)
# button.place(x=100, y=700)

root.mainloop()

# # this code above is an example of how we'll interact with the game. the def function is gonna run certain parts of our game which will be referenced with command. our different buttons will interact with the game