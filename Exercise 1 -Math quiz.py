import tkinter as tk
import random

# Function to display the difficulty menu
def displayMenu():
    menu_frame.pack(fill="both", expand=True)
    quiz_frame.pack_forget()
    result_frame.pack_forget()

# Function to generate random integers based on difficulty
def randomInt(difficulty):
    if difficulty == 1:  # Easy: Single-digit numbers
        return random.randint(1, 9)
    elif difficulty == 2:  # Moderate: Double-digit numbers
        return random.randint(10, 99)
    elif difficulty == 3:  # Advanced: Four-digit numbers
        return random.randint(1000, 9999)

# Function to randomly decide whether the problem is addition or subtraction
def decideOperation():
    return random.choice(["+", "-"])

# Function to set up the next problem or retry the same problem
def displayProblem(new_problem=True):
    global num1, num2, operation, correct_answer

    if new_problem:
        # Generate a new question only if needed
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        
        # Ensure subtraction does not result in negative answers
        if operation == "-" and num1 < num2:
            num1, num2 = num2, num1

        correct_answer = eval(f"{num1} {operation} {num2}")
    
    problem_label.config(text=f"Question {question_count + 1}: {num1} {operation} {num2} = ?")
    answer_entry.delete(0, tk.END)

# Function to check if the user's answer is correct
def checkAnswer():
    global score, question_count, first_attempt

    user_input = answer_entry.get()
    
    if not user_input.isdigit():
        error_label.config(text="Error: Please enter a valid number.", fg="red")
        return
    
    user_answer = int(user_input)

    if user_answer == correct_answer:
        # Correct answer handling
        score += 10 if first_attempt else 5
        score_label.config(text=f"Score: {score}")
        question_count += 1  # Move to the next question
        first_attempt = True  # Reset attempt flag for the next question
        error_label.config(text="Correct!", fg="green")

        # Check if the quiz is complete
        if question_count < 10:
            displayProblem(new_problem=True)  # Generate a new problem
        else:
            displayResults()  # Show final results
    else:
        # Incorrect answer handling
        if first_attempt:
            first_attempt = False  # Allow one more attempt
            error_label.config(text="Incorrect! Try again.", fg="orange")
            displayProblem(new_problem=False)  # Retry the same question
        else:
            error_label.config(text=f"Wrong! The correct answer was {correct_answer}.", fg="red")
            question_count += 1  # Move to the next question

            # Check if the quiz is complete
            if question_count < 10:
                displayProblem(new_problem=True)  # Generate a new problem
            else:
                displayResults()  # Show final results

# Function to display results and rank the user
def displayResults():
    rank = "F"
    if score > 90:
        rank = "A+"
    elif score > 80:
        rank = "A"
    elif score > 70:
        rank = "B"
    elif score > 60:
        rank = "C"
    elif score > 50:
        rank = "D"
    
    summary_label.config(text=f"Your score: {score}/100\nRank: {rank}")
    quiz_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)

# Function to start the quiz
def startQuiz():
    global difficulty, score, question_count, first_attempt
    difficulty = difficulty_var.get()
    if difficulty == 0:
        error_label.config(text="Error: Please select a difficulty level.", fg="red")
        return
    score = 0
    question_count = 0
    first_attempt = True
    score_label.config(text="Score: 0")
    displayProblem()
    menu_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

# Function to reset the game
def resetGame():
    global score, question_count
    score = 0
    question_count = 0
    score_label.config(text="Score: 0")
    displayMenu()

# Function to exit the application
def exitApp():
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Math Quiz Challenge")
root.geometry("500x400")
root.config(bg="#F0F8FF")  # Light blue background for the whole window

# Variables
difficulty_var = tk.IntVar(value=0)
difficulty = 0
score = 0
question_count = 0
first_attempt = True
correct_answer = None

# Frames for different pages
menu_frame = tk.Frame(root, bg="#ADD8E6")  # Light blue background for menu frame
quiz_frame = tk.Frame(root, bg="#ADD8E6")  # Light blue background for quiz frame
result_frame = tk.Frame(root, bg="#ADD8E6")  # Light blue background for result frame

# --- Menu Frame ---
menu_title_label = tk.Label(menu_frame, text="Math Quiz Challenge", font=("Arial", 20, "bold"), fg="black", bg="#ADD8E6")
menu_title_label.pack(pady=10)

difficulty_label = tk.Label(menu_frame, text="Select Difficulty Level:", font=("Arial", 14), fg="black", bg="#ADD8E6")
difficulty_label.pack(pady=10)

difficulty_frame = tk.Frame(menu_frame, bg="#ADD8E6")
difficulty_frame.pack(pady=10)

difficulties = [
    ("Easy", 1),
    ("Moderate", 2),
    ("Advanced", 3),
]

for text, value in difficulties:
    tk.Radiobutton(difficulty_frame, text=text, variable=difficulty_var, value=value, font=("Arial", 12), bg="#ADD8E6").pack(anchor="w")

start_button = tk.Button(menu_frame, text="Start Quiz", font=("Arial", 12), command=startQuiz, fg="black", bg="green")
start_button.pack(pady=20)

# --- Quiz Frame ---
problem_label = tk.Label(quiz_frame, text="Problem", font=("Arial", 18), fg="black", bg="#ADD8E6")
problem_label.pack(pady=10)

answer_entry = tk.Entry(quiz_frame, font=("Arial", 14), width=10)
answer_entry.pack(pady=10)

submit_button = tk.Button(quiz_frame, text="Submit Answer", font=("Arial", 14), command=checkAnswer, fg="black", bg="#7BD3EA")
submit_button.pack(pady=10)

error_label = tk.Label(quiz_frame, text="", font=("Arial", 12), fg="red", bg="#ADD8E6")
error_label.pack()

score_label = tk.Label(quiz_frame, text="Score: 0", font=("Arial", 14), fg="black", bg="#ADD8E6")
score_label.pack(pady=10)

# --- Result Frame ---
summary_label = tk.Label(result_frame, text="Your score: 0/100\nRank: F", font=("Arial", 16), fg="black", bg="#E0FFFF")
summary_label.pack(pady=20)

play_again_button = tk.Button(result_frame, text="Play Again", font=("Arial", 14), command=resetGame, fg="black", bg="#FA812F")
play_again_button.pack(pady=10)

exit_button = tk.Button(result_frame, text="Exit", font=("Arial", 14), command=exitApp, fg="black", bg="#FA4032")
exit_button.pack(pady=10)

# Start with Menu Frame
displayMenu()

# Run the GUI loop
root.mainloop()




