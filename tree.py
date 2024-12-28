import os, random, time
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
RESET = "\033[0m"
size = int(input("Größe (auch wenn es nicht auf die Größe ankommt (alles über ~25 buggt)): "))
tree = []
for i in range(size):
    spaces = " " * (size - i - 1)
    leaves = "*" * (2 * i + 1)
    tree.append(spaces + leaves + spaces)
trunk_width = max(3, size // 3)
trunk_height = max(2, size // 5)
trunk_spaces = " " * (size - trunk_width // 2 - 1)
trunk = [trunk_spaces + "|" * trunk_width + trunk_spaces for _ in range(trunk_height)]
tree += trunk
try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        decorated_tree = []
        for row in tree:
            decorated_row = ""
            for char in row:
                if char == "*" and random.random() > 0.8:
                    decorated_row += random.choice(COLORS) + "O" + RESET
                else:
                    decorated_row += char
            decorated_tree.append(decorated_row)
        for row in decorated_tree:
            print(row)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nFrohe Scheißnachten (uwu)!")
