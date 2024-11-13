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
m = (
  ("A) Shadow", "B) Roach", "C) Shadowfax", "D) Dapple"),
  ("A) Mercy", "B) Reaper", "C) Tracer", "D) Genji"),
  ("A) Zelda","B) Peach", "C) Midna", "D) Tetra"),
  ("A) Masamune", "B) Gunblade", "C) Excalibur", "D) Buster Sword"),
  ("A) Healing Potion", "B) Mana Flask", "C) Estus Flask", "D) Vitality Gem")
)
# reponds 
r = []
#Game loop
for choice in range(5):
    print(q[choice])
    print(m[choice])
    
    repond= input("Enter your reponde : ")
    r.append(repond)
print(r)   