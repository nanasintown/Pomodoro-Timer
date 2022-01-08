from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#515e63"
CORAL = "#f9baa3"
DEEPBLUE = '#005065'
FONT_NAME = "Courier"
WORK_MIN_1 = 25
WORK_MIN_2 = 50
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    title_label.config(text='Timer', fg=DEEPBLUE)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER SESSIONS ------------------------------- # 


def start_time1():
    global reps
    reps += 1
    work_sec = WORK_MIN_1 * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=GREY)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=DEEPBLUE)


def start_time2():
    global reps
    reps += 1
    work_sec = WORK_MIN_2 * 60
    short_break = SHORT_BREAK_MIN * 2 * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down2(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down2(short_break)
        title_label.config(text="Break", fg=GREY)
    else:
        count_down2(work_sec)
        title_label.config(text="Work", fg=YELLOW)

# ---------------------------- COUNTDOWN FUNCTION ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_time1()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


def count_down2(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_time2()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=10, pady=10, bg=CORAL)

# Labels

title_label = Label(text="Timer", fg=DEEPBLUE, bg=CORAL, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)
session1 = Label(text="25-5 Session", fg=DEEPBLUE, bg=CORAL, font=(FONT_NAME, 20))
session1.grid(column=0, row=3)
session2 = Label(text="50-10 Session", fg=DEEPBLUE, bg=CORAL, font=(FONT_NAME, 20))
session2.grid(column=2, row=3)

# buttons
session1 = Button(text="Session 1", highlightthickness=0, command=start_time1)
session1.grid(column=0, row=4)
session2 = Button(text="Session 2", highlightthickness=0, command=start_time2)
session2.grid(column=2, row=4)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=1, row=5)

check_mark = Label(bg=CORAL, fg=GREEN)
check_mark.grid(column=1, row=3)

# Setting up canvas
canvas = Canvas(width=200, height=225, bg=CORAL, highlightthickness=0)
canvas.grid(column=1, row=1)
img = PhotoImage(file="itsclock.png")
canvas.create_image(100, 100, image=img)
timer_text = canvas.create_text(100, 100, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))



window.mainloop()
# References: Angela Yu: 100 Days Python bootcamp