import random

a = random.randint(1, 6)
b = random.randint(1, 6)
print(f"punteggio Alice: {a}")
print(f"punteggio Bob: {b}")

if a > b:
    print(f"Alice vince con un punteggio di: {a}")
else:
    print(f"Bob vince con un punteggio di: {b}")