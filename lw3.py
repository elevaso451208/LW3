import tkinter as tk
import random 
import winsound

def creator(size):
    #INTERVAL [10,20]
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sm = 0
    pas = ''
    for i in range(size):
        t = random.randint(0, 35)
        sm += t + 1
        pas += alf[t]
    if sm / size <= 20 and sm / size >= 10: return pas
    else: return creator(size)

def gen():
    block1 = creator(5)
    block2 = creator(4)
    block3 = creator(4)
    password = f"{block1}-{block2}-{block3}"
    lbl.config(text=password) 

root = tk.Tk()
root.geometry("960x540")
root.title("Key generator")

winsound.PlaySound("music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

anim = [
    tk.PhotoImage(file='anim1.gif'),
    tk.PhotoImage(file='anim2.gif'),
    tk.PhotoImage(file='anim3.gif'),
    tk.PhotoImage(file='anim4.gif'),
    tk.PhotoImage(file='anim5.gif')
]
canvas = tk.Canvas(root)
canvas.pack(fill='both', expand=True)
bg_id = canvas.create_image(0, 0, image=anim[0], anchor="nw")

current_frame = 0

def animate_background(**kwargs):
    print(type(kwargs))
    global current_frame
    
    current_frame = (current_frame + 1) % len(anim)
    
    canvas.itemconfig(bg_id, image=anim[current_frame])

    root.after(1000, animate_background)

animate_background(l=1, k=2, m=3)

lbl = tk.Label(canvas, text=" "*15, font=("", 16), bg="#FFAA00")
lbl.place(relx=3/10, rely=1/2, anchor="center")

btn = tk.Button(canvas, text="Generate a key", font=("",14), bg="#FFAA00", activebackground="#432F24", command=lambda: gen())
btn.place(relx=3/10, rely=6/10, anchor="center")

root.mainloop() 