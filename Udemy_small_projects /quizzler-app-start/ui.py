from tkinter import * 
from data import get_questions

THEME_COLOR = "#375362"
FONT_NAME = "Courier"
class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        #----stat 
        self.score = 0 
        self.reps = 0                           
        #--canvas
        self.canvas = Canvas(self.window, width=300, height=250, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.canvas.create_rectangle(10, 10, 240, 210, fill="white", outline="")
        self.question_text = self.canvas.create_text(
            150, 125, width=220, text="Question goes here",
            font=("Arial", 16, "italic"), fill=THEME_COLOR, justify="center"
        )
        #buttons
        true_image  = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button( image=true_image,highlightthickness=0,
                                  bg=THEME_COLOR, activebackground=THEME_COLOR,command = lambda: self.check_answer(True)
                                  )
        self.false_button = Button(image=false_image,highlightthickness=0,
                                   bg=THEME_COLOR, activebackground=THEME_COLOR, command= lambda: self.check_answer(False)
                                   )

        self.true_button.grid(column =0 , row = 2)
        self.false_button.grid(column =1 , row = 2)
        #lable 
        self.score_label = Label(text = f"score:{self.score}" , bg=THEME_COLOR,  )
        self.score_label.grid(row=1, column=1, sticky="e", pady=(6, 0))

        # Place buttons ON the canvas
     


        self.show_question()
        
        self.window.mainloop() 


    def show_question(self):
        if self.reps < len (get_questions()):
         q = get_questions()[self.reps]["question"]
         self.canvas.itemconfig(self.question_text, text=q)
        else:
         self.canvas.itemconfig(self.question_text, text="No questions.")

    def check_answer(self , user_answer):
        correct_answer =  str(get_questions()[self.reps]["is true"]).lower()
        if user_answer.lower() == correct_answer:
            self.score +=1 
            self.score_label.config(text=f"Score: {self.score}")
        self.reps += 1
        self.show_question() 

        