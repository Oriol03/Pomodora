from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    window.after_cancel(count_time)
    title_time.config(text="Timer", fg=GREEN)
    canvas.itemconfig(txt_time, text="00:00")
    reps = 0
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_machine(long_break)
        title_time.config(text="Long break", fg=PINK)
    elif reps % 2 == 0:
        count_machine(short_break)
        title_time.config(text="Break", fg=RED)
    else:
        count_machine(work_time)
        title_time.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_machine(count):
    global reps, count_time
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count >= 0:
        if count_min < 10 and count_sec < 10:
            canvas.itemconfig(txt_time, text=f"0{count_min}:0{count_sec}")
        elif count_sec < 10:
            canvas.itemconfig(txt_time, text=f"{count_min}:0{count_sec}")
        elif count_min < 10:
            canvas.itemconfig(txt_time, text=f"0{count_min}:{count_sec}")
        else:
            canvas.itemconfig(txt_time, text=f"{count_min}:{count_sec}")
        count_time = window.after(1000, count_machine, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pamodora")

# create
canvas = Canvas()
canvas.config(width=200, height=223, bg=YELLOW, highlightthickness=0)
img_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=img_tomato)
txt_time = canvas.create_text(100, 140, text=f"00:00", font=(FONT_NAME, 40, "bold"), fill="white")
canvas.grid(row=1, column=1)

# create the buttons
start_but = Button(text="Start", highlightthickness=0, command=start_timer)
start_but.config(width=7)
start_but.grid(row=2, column=0)

reset_but = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_but.config(width=7)
reset_but.grid(row=2, column=2)

# create labels
title_time = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title_time.grid(row=0, column=1)

check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check.grid(row=3, column=1)

window.mainloop()
