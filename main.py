print("Welcome to Quiz!")
#ask user name
name= input("Enter your name: ")

#greeting message
print(f"Hello {name}!")

#score
score = 0
question_num = 0

#list of question
questions =[
    
    {
        "question": "Capital city of Georgia?",
        "options": ["A. London", "B. Paris", "C. Tbilisi", "D. Baku"],
        "answer": "C"
    },
    {
        "question": "What is the official currency of South Korea?",
        "options": ["A. Yen", "B. Won", "C. Yuan", "D. Dollar"],
        "answer": "B"
    },
    {
        "question": "What color do you get when you mix blue and yellow?",
        "options": ["A. Purple", "B. Orange", "C. Red", "D. Green"],
        "answer": "D"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What is the freexing point of water?",
        "options": ["A. 0C", "B. 10C", "C. 50C", "D. 100C"],
        "answer": "A"
    },
    {
        "question": "Capital city of France?",
        "options": ["A. London", "B. Paris", "C. Tbilisi", "D. Baku"],
        "answer": "B"
    },

]

#loop through questions
for i, q in enumerate(questions, start=1):
    question_num +=1
    print(f"Question {question_num}: {q['question']}")

    #show options
    for option in q['options']:
        print(option)
    
    #get user answer
    user_answer = input("Your answer (A,B,C,D): ").strip().upper()

    #check answer
    if user_answer == q['answer']:
        print("Correct!\n")
        score +=1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")
#show final result
total_questions = len(questions)
percentage = (score / total_questions) * 100

print("Quiz finished!")
print(f"Your score: {score} / {total_questions}")
print(f"Persentage: {percentage:.2f}%")
