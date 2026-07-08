"""
Multiple Choice Quiz
Practices: lists of lists, functions, loops, input validation, break
"""

def ask_question(question):
    prize_money = 0
    for q in question:
        print(q[0])
        print(q[1])
        print(q[2])
        print(q[3])
        print(q[4])
        answer = int(input("Enter your answer: "))

        if answer < 1 or answer > 4:
            print("Invalid input. Please enter a number between 1 and 4.")
            break

        if answer == q[-1]:
            print("Correct!")
            prize_money += 1000
        else:
            print("Incorrect. The correct answer is:", q[-1])
            print("Game Over!")
            break

    print(f"Total prize money won: Rs {prize_money}")


ask_question([
    ["Which nucleotide pairs with Adenine?", "1. Cytosine", "2. Guanine", "3. Thymine", "4. Uracil", 3],
    ["Who is the father of Computers?", "1. James Gosling", "2. Charles Babbage", "3. Dennis Ritchie", "4. Bjarne Stroustrup", 2]
])
