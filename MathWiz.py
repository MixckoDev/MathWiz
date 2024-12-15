import random

def generate_question():
    operations = ["+", "-", "*", "/"]
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

   
    if operation == "/":
        num1 = num1 * num2  

    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    return question, correct_answer

def main():
    print("Welcome to MathWiz: The Math Quiz Game!")
    num_questions = int(input("How many questions would you like to attempt? "))
    correct = 0

    for i in range(1, num_questions + 1):
        print(f"\nQuestion {i}:")
        question, correct_answer = generate_question()
        print(question)
        try:
            user_answer = float(input("Your answer: "))
            if abs(user_answer - correct_answer) < 0.01: 
                print("Correct!")
                correct += 1
            else:
                print(f"Incorrect! The correct answer is {correct_answer:.2f}")
        except ValueError:
            print("Invalid input! Moving to the next question.")

    print("\nQuiz Completed!")
    print(f"You answered {correct} out of {num_questions} questions correctly.")
    print(f"Your score: {correct / num_questions * 100:.2f}%")

if __name__ == "__main__":
    main()
