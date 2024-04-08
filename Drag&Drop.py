from tkinter import *

def drag_start(left_click):
    active_widget = left_click.widget
    active_widget.startX = left_click.x
    active_widget.startY = left_click.y

def drag_motion(left_clicked_motion):
    active_widget = left_clicked_motion.widget
    x = active_widget.winfo_x() - active_widget.startX + left_clicked_motion.x
    y = active_widget.winfo_y() - active_widget.startY + left_clicked_motion.y
    # Boundary checks
    if x < 0:
        x = 0
    elif x > window.winfo_width() - active_widget.winfo_width():
        x = window.winfo_width() - active_widget.winfo_width()
    if y < 0:
        y = 0
    elif y > window.winfo_height() - active_widget.winfo_height():
        y = window.winfo_height() - active_widget.winfo_height()
    active_widget.place(x=x, y=y)

window = Tk()

window.geometry("854x480")
window.config(bg="light pink")

red_label = Label(
    window,
    bg="red",
    width=10,
    height=5,
)

blue_label = Label(
    window,
    bg="blue",
    width=10,
    height=5,
)

red_label.place(x=0, y=0)
red_label.bind("<Button-1>", drag_start)
red_label.bind("<B1-Motion>", drag_motion)

blue_label.place(x=100, y=100)
blue_label.bind("<Button-1>", drag_start)
blue_label.bind("<B1-Motion>", drag_motion)

window.mainloop()
