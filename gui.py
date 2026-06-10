import tkinter as tk

root = tk.Tk()
root.title("Vote Me!")
root.attributes('-fullscreen',True)
bg_image = tk.PhotoImage(file="1200.png")
bg2 = bg_image.zoom(2)
bg_label = tk.Label(root, image=bg2)
bg_label.place(relwidth=1, relheight=1)
# this above code is the background of the game, should be on always


# textbox = tk.PhotoImage(file="textboxneutral.png")
# textboxplace = tk.Label(root, image=textbox)
# textboxplace.place(relwidth=1, relheight=1)


# photo = tk.PhotoImage(file="button.png")

# def on_click():
#     print("Button clicked!")


# button = tk.Button(root,  command=on_click, borderwidth=0)
# button.place(x=100, y=700)
# button.pack(pady=20)

def show_sprite(filename):
    sprite = tk.PhotoImage(file=filename)

    sprite = sprite.zoom(2, 2)
    root.current_sprite = sprite

    sprite_label = tk.Label(root, image=sprite, borderwidth=0)
    sprite_label.place(relx=0.5, rely=0.5, anchor="center")

    return sprite_label




root.mainloop()
