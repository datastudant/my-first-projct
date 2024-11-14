# Quiz Questions
q = (
    "In The Witcher 3: Wild Hunt, what is the name of Geralt’s trusted horse?",
    "In Overwatch, which character has the ability to “rewind” time to regain health and return to a previous position?",
    "What is the name of the princess in The Legend of Zelda series who often needs rescuing?",
    "In Final Fantasy VII, what iconic weapon does Cloud Strife wield?",
    "In Dark Souls, what item allows players to regain health and is a staple throughout the series?"
)

# Correct Answers
a = ("B", "C", "A", "D", "C")

# Multiple-choice options
c = (
    ("A) Shadow", "B) Roach", "C) Shadowfax", "D) Dapple"),
    ("A) Mercy", "B) Reaper", "C) Tracer", "D) Genji"),
    ("A) Zelda", "B) Peach", "C) Midna", "D) Tetra"),
    ("A) Masamune", "B) Gunblade", "C) Excalibur", "D) Buster Sword"),
    ("A) Healing Potion", "B) Mana Flask", "C) Estus Flask", "D) Vitality Gem")
)

# Response storage and score
responses = []
correct_responses = []
incorrect_responses = []
score = 0

# Game loop
for i in range(len(q)):
    print("--------------------------------------")
    print(f"Question {i + 1}: {q[i]}")
    for option in c[i]:
        print(option)
    
    response = input("Your answer: ").upper()
    responses.append(response)
    
    if response == a[i]:
        score += 1
        correct_responses.append(response)
    else:
        incorrect_responses.append(response)

# Calculate and display score as a percentage
score_percentage = (score / len(q)) * 100
print(f"\nYour score: {score_percentage}%")
print("-------------------The End-------------------")

# Display each question, correct answer, and the user's answer
for i in range(len(q)):
    print(f"\nQuestion {i + 1}: {q[i]}")
    print(f"Correct answer: {a[i]}")
    print(f"Your answer: {responses[i]}")

# Summary of correct and incorrect answers
print("\nCorrect answers:")
for ans in correct_responses:
    print(ans)

print("\nIncorrect answers:")
for ans in incorrect_responses:
    print(ans)
