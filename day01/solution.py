
with open("input.txt", "r") as input:
    chunks = input.read().split("\n\n")
    max_calories = 0
    for chunk in chunks:
        lines = chunk.split("\n")
        calories = sum(map(int,lines))
        max_calories = max(max_calories,calories)
    print(max_calories)
    calories = [sum(map(int,chunk.split("\n"))) for chunk in chunks]
    calories.sort()
    top_three = sum(calories[-3:])
    print(top_three)
