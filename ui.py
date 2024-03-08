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
        self.correct_b = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.correct_b.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.correct_b = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.correct_b.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_c.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_c.itemconfig(self.question_text, text=q_text)
        else:
            self.question_c.itemconfig(self.question_text, text="You've reached the end  of the quiz.")
            self.true_press.config(state="disabled")
            self.false_press.config(state="disabled")


    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.score_l.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.question_c.config(bg="green")
        else:
            self.question_c.config(bg="red")
        self.window.after(1000, self.get_next_question)



