from tkinter import *
from settings import *

# functions


def close_the_window(event):
    event.widget.destroy()


def presing_the_button_full_screen():
    if window.attributes('-fullscreen'):
        window.attributes('-fullscreen', False)
    else:
        window.attributes('-fullscreen', True)


# create variebls
window = Tk()
icon = PhotoImage(file='images\dragon-snake.png')
lable = Label(window, text=f'Score: {score}', font='bold', bg='red')
bg = PhotoImage(file='images\dragon-snake.png')
canvas = Canvas(window, width=1000, height=1000, bg='gray')
full_screen = Button(window, text='Full Screen', command=presing_the_button_full_screen,
                     font=('Comic Sans', 10), fg='gray')

# set parameters
window.geometry('800x600+450+0')
window.title('The dragon-snake')
window.iconphoto(True, icon)
window.config(background='gray')
lable.place(relx=1,
            rely=0,
            anchor='ne')
full_screen.pack()
canvas.pack()

# adding functionality to existing parameters
canvas.create_image(0, 0, image=bg, anchor="nw")
window.bind("<Escape>", close_the_window)


window.mainloop()


# if need add value to scope
#  global score
#     score += 1
#     lable = Label(window, text=f'Score: {score}')
#     lable.place(relx=1,
#                 rely=0,
#                 anchor='ne')
