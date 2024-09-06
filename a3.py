import random

class FruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red","banana":"yellow","orange":"orange","watermelon":"green"}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}")
            user_answer = input()
            if (user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option = int(input("Enter 1 if you want to play again, otherwise enter 0: "))
            if option:
                break
print("welcome")
fq = FruitQuiz()
fq.quiz()