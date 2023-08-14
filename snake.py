from tkinter import *
from settings import *
from PIL import Image, ImageTk
import random


window = Tk()
icon = PhotoImage(file='images\dragon-snake.png')
# create image
bg_image = Image.open('images/Snake Wallpapers Best Wallpapers.png')
bg_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
bg = ImageTk.PhotoImage(bg_image)

canvas = Canvas(window, width=new_width,
                height=new_height, bg='black', highlightthickness=0)

# set parameters
window.geometry('800x600+450+0')
window.resizable(False, False)
window.title('The snake')
window.iconphoto(True, icon)
window.config(background='black')
canvas.pack()


def hide_menu_bar():
    play_button.place_forget()  # Hide the button
    escape_menu_bar.place_forget()  # Hide the menu bar
    menu_bar_visible = False


def close_the_window():
    window.destroy()


mebu_options_bar_visible = False


def open_options_bar():
    global mebu_options_bar_visible

    if not mebu_options_bar_visible:
        options_menu_bar.place(relx=0, rely=0, width=800, height=600)
        mebu_options_bar_visible = True
    else:
        options_menu_bar.destroy()
        mebu_options_bar_visible = False


menu_bar_visible = False


def open_menu_bar(event):
    global menu_bar_visible

    if not menu_bar_visible:
        escape_menu_bar.place(relx=0, rely=0, width=800, height=600)

        play_button.pack()
        options_button.pack(pady=20)
        exit_button.pack()
        menu_bar_visible = True
    else:
        play_button.place_forget()
        escape_menu_bar.place_forget()  # Hide the menu bar
        menu_bar_visible = False


# adding functionality to existing parameters
canvas.create_image(0, 0, image=bg, anchor="nw")
escape_menu_bar = Label(window, font='bold', bg='gray')
options_menu_bar = Label(window, font='bold', bg='gray')
play_button = Button(escape_menu_bar, text='Play',
                     width=10, height=2, command=hide_menu_bar)
options_button = Button(escape_menu_bar, text='Options',
                        width=10, height=2, command=open_options_bar)
exit_button = Button(escape_menu_bar, text='Exit',
                     width=10, height=2, command=close_the_window)
window.bind("<Escape>", open_menu_bar, open_options_bar)


class Food:
    def __init__(self):
        random_x = random.randint(0, SCREEN_WIDTH)
        random_y = random.randint(0, SCREEN_HEIGHT)

        self.x = random_x
        self.y = random_y


food = Food()

food = canvas.create_rectangle(
    food.x, food.y, food.x + 20, food.y + 20, fill='red')


class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0


snake = Snake()


snake = canvas.create_rectangle(
    snake.x, snake.y, snake.x + 20, snake.y + 20, fill='green')


window.mainloop()


# if need add value to scope
#  global score
#     score += 1
#     lable = Label(window, text=f'Score: {score}')
#     lable.place(relx=1,
#                 rely=0,
#                 anchor='ne')
