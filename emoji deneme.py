import Tkinter as tk


def add_image():
    text.image_create(tk.END, image=img)  # Example 1
    text.window_create(tk.END, window=tk.Label(text, image=img))  # Example 2


root = tk.Tk()
frame1 = tk.Frame(root)
frame1.pack(padx=5, pady=5, side="top")
frame2 = tk.Frame(root)
frame2.pack(padx=5, pady=5, side="bottom")
frame3 = tk.Frame(root)
frame3.pack(padx=5, pady=5, side="bottom")

# text = tk.Text(frame1)
# text.pack(padx=20, pady=20)

photo = tk.PhotoImage(file="emojiler/rsz_unamused_face_emoji.png", width=20, height=20)
angry = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")
angry2 = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")
angry3 = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")
angry4 = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")
angry5 = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")
angry6 = tk.Button(frame1, text="Insert", command=add_image, image =photo, relief="flat").pack(side="left")


photo2 = tk.PhotoImage(file="emojiler/rsz_very_angry_emoji.png", width=20, height=20)
happy = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")
happy2 = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")
happy3 = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")
happy4 = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")
happy5 = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")
happy6 = tk.Button(frame2, text="Insert", command=add_image, image =photo2, relief="flat").pack(side="left")


photo3 = tk.PhotoImage(file="emojiler/rsz_tears_of_joy_emoji.png", width=20, height=20)
face = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")
face2 = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")
face3 = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")
face4 = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")
face5 = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")
face6 = tk.Button(frame3, text="Insert", command=add_image, image =photo3, relief="flat").pack(side="left")



img = tk.PhotoImage(file="emojiler/Alien_Emoji.png")

root.mainloop()
