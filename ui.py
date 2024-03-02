from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = {"Arial", 20, "italic"}
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_l = Label(text="Score: 0", bg=THEME_COLOR, foreground="white")
        self.score_l.grid(row=0, column=1)

        self.question_c = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_c.create_text(
            150, 125,
            width=280,
            text="some question",
            fill=THEME_COLOR,
            font=FONT
        )
        self.question_c.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.correct_b = Button(image=true_img, highlightthickness=0)
        self.correct_b.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.correct_b = Button(image=false_img, highlightthickness=0)
        self.correct_b.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_c.itemconfig(self.question_text, text=q_text)
