from tkinter import *
from settings import *

window = Tk()
icon = PhotoImage(file='dragon-snake.png')
lable = Label(window, text=f'Score: {score}')


def presing_the_button_full_screen():
    if window.attributes('-fullscreen'):
        window.attributes('-fullscreen', False)

    else:
        window.attributes('-fullscreen', True)


full_screen = Button(window, text='Full Screen', command=presing_the_button_full_screen,
                     font=('Comic Sans', 10), fg='gray')


window.geometry('420x420+640+0')
window.title('The dragon-snake')
window.iconphoto(True, icon)
window.config(background='black')
lable.place(relx=1,
            rely=0,
            anchor='ne')
full_screen.pack()
window.mainloop()


# if need add value to scope
#  global score
#     score += 1
#     lable = Label(window, text=f'Score: {score}')
#     lable.place(relx=1,
#                 rely=0,
#                 anchor='ne')
