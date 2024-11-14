#quize game
#Quiz Questions:
q = (
  "In The Witcher 3: Wild Hunt, what is the name of Geralt’s trusted horse?",
  "In Overwatch, which character has the ability to “rewind” time to regain health and return to a previous position?",
  "What is the name of the princess in The Legend of Zelda series who often needs rescuing?",
  "In Final Fantasy VII, what iconic weapon does Cloud Strife wield?",
  "In Dark Souls, what item allows players to regain health and is a staple throughout the series?"
)
#Answers:
a = (
  "B",
  "C",
  "A",
  "D",
  "C"
  )
#multiple-choice options 
c = (
  ("A) Shadow", "B) Roach", "C) Shadowfax", "D) Dapple"),
  ("A) Mercy", "B) Reaper", "C) Tracer", "D) Genji"),
  ("A) Zelda","B) Peach", "C) Midna", "D) Tetra"),
  ("A) Masamune", "B) Gunblade", "C) Excalibur", "D) Buster Sword"),
  ("A) Healing Potion", "B) Mana Flask", "C) Estus Flask", "D) Vitality Gem")
)
# reponds 
r = []
s = 0
f = []
t = []
#Game loop
for i in range(len(q)):
  print("--------------------------------------")
  print(f"Question {i+1} : {q[i]}")
  for j in range(len(c[i])):
    print(c[i][j])
  valeu = input("your answer: ")
  valeu.upper()
  r.append(valeu)
for i in range(len(r)):
  if r[i] == a[i]:
    s += 1
    t.append(r[i])
  else:
    f.append(r[i])
s = ( s / 5 ) * 100
print(f"Your score: {s}")
print("-------------------The end-------------------")
for i in range(len(r)):
  print(f"The correct answer is : {a[i]}")
  print(f"Your answer: {r[i]}")


for i in range(len(t)):
    print(f"Your answer is correct: {t[i]}")
for i in range(len(f)):
    print(f"The False answer is : {f[i]}")
  
 