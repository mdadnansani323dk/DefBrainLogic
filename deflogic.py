import time
import random

print("\n===============================")
print("        DEF LOGiC")
print("   A Mind & Perception Game")
print("===============================\n")

name = input("Enter your name: ")

print("\nInitializing psychological scan...")
time.sleep(2)

score = 0
personality = []

print("\nWelcome", name)
print("Your mind will now face a series of perception and logic tests.\n")
time.sleep(2)

# -----------------------------
# Level 1 - Animal instinct
# -----------------------------

print("LEVEL 1 : INSTINCT TEST\n")
print("Choose the animal that represents you most:\n")
print("1. Lion")
print("2. Wolf")
print("3. Eagle")
print("4. Snake")

a = input("\nYour choice: ")

if a == "1":
    score += 2
    personality.append("Leader")
elif a == "2":
    score += 1
    personality.append("Strategist")
elif a == "3":
    score += 2
    personality.append("Visionary")
else:
    personality.append("Mysterious")

# -----------------------------
# Level 2 - Perception
# -----------------------------

print("\nLEVEL 2 : PERCEPTION TEST\n")
print("You enter a room. What do you notice first?\n")
print("A. People's faces")
print("B. The exit door")
print("C. The objects")
print("D. The window")

b = input("\nYour choice: ").upper()

if b == "A":
    personality.append("Social Reader")
    score += 2
elif b == "B":
    personality.append("Survivor Mind")
elif b == "C":
    personality.append("Logical Observer")
    score += 2
else:
    personality.append("Dream Thinker")

# -----------------------------
# Level 3 - Logic puzzle
# -----------------------------

print("\nLEVEL 3 : LOGIC CHALLENGE\n")

print("What number comes next?")
print("2  6  12  20  30  ?\n")

c = input("Answer: ")

if c == "42":
    print("Correct. Your pattern recognition is strong.")
    score += 3
else:
    print("Interesting answer. The correct answer was 42.")

# -----------------------------
# Level 4 - Mind reaction
# -----------------------------

print("\nLEVEL 4 : DECISION TEST\n")

print("A team project suddenly fails.")
print("What do you do first?\n")

print("1. Take control")
print("2. Calm everyone")
print("3. Analyze what went wrong")
print("4. Observe silently")

d = input("\nChoice: ")

if d == "3":
    score += 3
    personality.append("Analytical Mind")
elif d == "1":
    personality.append("Dominant Leader")
elif d == "2":
    personality.append("Peacemaker")
else:
    personality.append("Silent Strategist")

# -----------------------------
# Final Result
# -----------------------------

print("\nProcessing results...")
time.sleep(3)

print("\n===============================")
print("        DEF LOGiC RESULT")
print("===============================\n")

print("Mind Score:", score)

print("\nDominant Traits:")
for p in personality:
    print("-", p)

print("\nFinal Mind Type:")

if score >= 7:
    print("STRATEGIC MASTER 🧠")
elif score >= 4:
    print("BALANCED THINKER ⚖️")
else:
    print("INTUITIVE MIND 🌙")

print("\nGame Complete.")
print("Your mind has been analyzed.\n")