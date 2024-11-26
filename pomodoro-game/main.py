from tkinter import *
from pygame import mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = NONE

# ---------------------------- RING SOUND ------------------------------- #
def play_ring_sound():
    mixer.init()
    mixer.music.load("ring_sound.mp3")
    mixer.music.play()
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        play_ring_sound()
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        play_ring_sound()
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    if count > 0:
        minutes = count//60
        seconds = count - minutes*60
        canvas.itemconfig(timer_text, text= f"{minutes:02}:{seconds:02}")
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔ "
        check_mark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 20, "normal"), command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 16, "normal"), command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark_label = Label(text="", fg=GREEN ,bg=YELLOW, font=(FONT_NAME, 16, "normal"))
check_mark_label.grid(column=1, row=3)







window.mainloop()
