import sys
import random

question_database=[]
answer_database=[]
with open('questions.tsv','r') as f:
    data = f.readlines()
    for line in data:
        question_database.append(line.split('\t')[0])
        answer_database.append(line.split('\t')[1][0:-1]
    del(data)
                               
def get_valid_input(prompt, input_type=str, allow_empty=False):
    while True:
        user_input = input(prompt).strip()
        if not allow_empty and user_input == "":
            print("Input cannot be empty. Please try again.")
            continue
        if input_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a valid number.")
        else:
            return user_input

def get_quiz_content():
    questions = []
    answers = []
    n_questions=0
    while n_questions<1:
        try :
            n_questions=int(input("Please enter the number of questions(it should be an integer greater than 0 and less): "))
            n_questions=n_questions if n_questions>0 else 0
        except ValueError:
            print("Incorrect number inserted, number of questions set to 10")
            n_questions=10
    print(f"Please enter {n_questions} questions and their corresponding answers.")
    questions_numbers = random.sample(range(0,len(question_database),n_questions)
    for i in questions_numbers:
        questions.append(question_database[i])
        answers.append(answer_database[i])
    return questions, answers

def run_quiz(questions, answers):
    name = get_valid_input("Enter your name: ")
    score = 0
    num_questions=len(questions)
    print(f"\nWelcome, {name}! Let's start the quiz.\n")
    question_order = random.sample(range(0,num_questions),num_questions)
    correct = []
    wrong = []
    for i, question_num in enumerate(question_order, 1):
        print(f"Question {i}: {questions[question_num]}")
        user_answer = get_valid_input("Your answer: ")
        
        if user_answer.lower() == answers[question_num].lower():
            # print("Correct!")
            correct.append(question_num)
            score += 1
        else:
            # print(f"Sorry, the correct answer is: {answers[i-1]}")
            wrong.append(question_num)
        print()
    percentage = (score / len(questions)) * 100
    print(f"Quiz completed! Your score: {score}/{len(questions)} ({percentage:.2f}%)")
    if len(correct):
        print('Questions correctly answered')
        for question_num in correct:
            print(questions[question_num])
    if len(wrong):
        print('Questions failed and qnswers')
        for question_num in wrong:
            print(f'{questions[question_num]} : {answers[question_num]}')
    
    return name, score

def main():
    print("Welcome to the Quiz Program!")
    questions, answers = get_quiz_content()
    
    scores = []
    while True:
        name, score = run_quiz(questions, answers)
        scores.append((name, score))
        
        play_again = get_valid_input("Would anyone else like to take the quiz? (yes/no): ")
        if play_again.lower() != "yes":
            break
    
    if scores:
        print("\nFinal Results:")
        max_score = max(scores, key=lambda x: x[1])
        avg_score = sum(score for _, score in scores) / len(scores)
        
        for name, score in scores:
            print(f"{name}: {score}/{len(questions)}")
        
        print(f"\nHighest score: {max_score[0]} with {max_score[1]}/{len(questions)}")
        print(f"Average score: {avg_score:.2f}/{len(questions)}")
    else:
        print("No quizzes were completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuiz terminated by user.")
        sys.exit(0)
