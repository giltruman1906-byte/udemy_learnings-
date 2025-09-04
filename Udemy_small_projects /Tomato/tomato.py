import tkinter as tk
import time 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =  25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lable.config(text="Timer")
    lb_v.config(text="")
    global reps 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1 
    if reps % 8  == 0 :
        count_down ( LONG_BREAK_MIN * 60)
        timer_lable.config (text = "Break" , fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
    elif reps % 2 == 0 :
        count_down (SHORT_BREAK_MIN * 60) 
        timer_lable.config(text ="Short Break" , fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down (WORK_MIN * 60)
        timer_lable.config(text = "Work" , fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60 
    canvas.itemconfig(timer_text , text = f"{minutes:02d}:{seconds:02d}")
    if count> 0 :
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = "✅" 
        work_sessions = math.floor(reps/2)
        for n in  range (work_sessions):
            marks += "✅" 
        lb_v.config(text=marks) 
        timer_count_lb.config(text="work_sessions")  

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# canvas 

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# label 
timer_lable = tk.Label( text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_lable.grid(row=0, column=1)
lb_v = tk.Label( text = " ")
lb_v.grid(row=3, column=1)

timer_count_lb = tk.Label( text = "0" , fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_count_lb.grid(row=0, column=2)   
# button 
start_b = tk.Button(text="Start" , command = start_timer,   bg=YELLOW, highlightthickness = 0 )
start_b.grid(row=2, column=0)
reset_b = tk.Button(text="Reset" , command = reset_timer , bg=YELLOW, highlightthickness = 0 )
reset_b.grid(row=2, column=2 )   


window.mainloop() 