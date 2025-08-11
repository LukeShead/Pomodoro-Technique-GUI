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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    tick.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS

    work_sec = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN

    if REPS % 2 == 0:
        if REPS == 8:
            REPS = 0
            title.config("Take a big break")
            count_down(long_break)
        else:
            REPS += 1
            title.config(text="Work Time")
            tick.config(text="✔")
            count_down(work_sec)
    else:
        REPS += 1
        title.config(text="Take a small break")
        count_down(short_break)

    # count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    minute_count = math.floor(count / 60)
    second_count = math.floor(count % 60)
    if second_count < 10:
        second_count = f"0{second_count}"


    canvas.itemconfig(timer_text, text=f"{minute_count}:{second_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        num_ticks = int(REPS / 2)
        tick.config(text="✔" * num_ticks)
    print(count)

# ---------------------------- UI SETUP ------------------------------- #
#Setting up the window and background of window
window = Tk()
window.title("Pomodoro Technique")
window.config(padx= 100, pady=50, background=PINK)





#fg=GREEN
#Setting up the Canvas to which the tomato will be displayed on
canvas = Canvas(width=206, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
#Creating the text onto the canvas for the timer
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column= 1 , row= 1)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=PINK)
title.grid(row=0, column=1)

start_but = Button(text="Start", command=start_timer)
start_but.grid(row=3, column=0)

reset_but = Button(text="Reset", command=reset_timer)
reset_but.grid(row=3, column=2)

tick = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 15, "bold"))
tick.grid(row=4, column=1)

window.mainloop()