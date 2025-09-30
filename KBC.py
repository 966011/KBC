import random

questions = [
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A. Subhash Chandra Bose", "B. Bhagat Singh", "C. Mahatma Gandhi", "D. Jawaharlal Nehru"],
        "answer": "C"
    },
    {
        "question": "Which of these is the largest ocean in the world?",
        "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "In computers, what does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Control Program Utility", "C. Central Power Unit",
                    "D. Computer Processing Utility"],
        "answer": "A"
    }
]

prizes = [5000000, 10000000, 30000000, 70000000]
total = 0
lifeline_used = False

print("🎉 Welcome to Kaif Chouhan KBC 🎉")
print("You have 1 lifeline: 50-50 (type '5050' to use it once)")

for i, q in enumerate(questions):
    print(f"\nQuestion {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)

    choice = input("Your answer (A/B/C/D or 5050): ").upper()

    if choice == "5050":
        if not lifeline_used:
            lifeline_used = True
            correct = q['answer']
            wrong_options = [opt[0] for opt in q['options'] if opt[0] != correct]
            remove_wrong = random.choice(wrong_options)
            new_options = [opt for opt in q['options'] if opt[0] in (correct, remove_wrong)]
            print("\n50-50 Lifeline Applied! Remaining options:")
            for opt in new_options:
                print(opt)
            choice = input("Your answer (A/B/C/D): ").upper()
        else:
            print("You already used your lifeline!")
            choice = input("Your answer (A/B/C/D): ").upper()

    if choice == q['answer']:
        print("✅ Correct!")
        total += prizes[i]
        print(f"You won ₹{prizes[i]}")
    else:
        print("❌ Wrong answer!")
        break

print(f"\n🎯 Your total winnings: ₹{total}")
print("Thanks for playing KBC!")
