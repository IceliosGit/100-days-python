from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2cd406"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
countdown = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    timer_text.config(text="Timer", fg="green")
    checkmark["text"] = ""
    canvas.itemconfig(timer, text=f'25:00')
    window.after_cancel(countdown)
    start_button.config(state="normal", bg="white")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_countdown():
    global reps
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:  # Work
        timer_text.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN*60)
    if reps == 1 or reps == 3 or reps == 5:  # Break
        timer_text.config(text="Break Time", fg=PINK)
        checkmark["text"] = "✓" * round(reps/2 + 0.1)  # formula to get right amount of checkmark
        count_down(SHORT_BREAK_MIN*60)
    if reps == 7:
        timer_text.config(text="Long break", fg=RED)
        checkmark["text"] = "✓" * 4
        count_down(LONG_BREAK_MIN*60)  # Long Break
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global countdown
    if count > 0:
        countdown = window.after(1000, count_down, count - 1)
    else:
        start_countdown()

    if count % 60 == 0:
        count_m = round(count/60)
        count_s = 0
    else:
        count_s = count % 60
        count_m = count//60
    if len(str(count_m)) == 1:  # Add the "0" if single digit for m
        count_m = "0" + str(count_m)
    if len(str(count_s)) == 2:  # Add the "0" if single digit for s (another method)
        canvas.itemconfig(timer, text=f'{count_m}:{count_s}')
    else:
        canvas.itemconfig(timer, text=f'{count_m}:0{count_s}')

# ----------------------------UI SETUP ------------------------------- #


def block_start():
    start_button.config(state="disabled", bg="gray")


window = Tk()
window.title("pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# tomato with time
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Timer text
timer_text = Label(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg="green")
timer_text.grid(column=1, row=0)

# Button
start_button = Button(text="start", highlightthickness=0,
                      bg="white", command=lambda: [start_countdown(), block_start()])
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, bg="white", command=reset)
reset_button.grid(column=2, row=2)

# checkmark
checkmark = Label(text="", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg="green")
checkmark.grid(column=1, row=3)

window.mainloop()
