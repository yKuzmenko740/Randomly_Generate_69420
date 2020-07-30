import random
import csv
import pandas as pd
import matplotlib.pyplot as plt

FILE = "CSVs/loops_100_3.csv"


def save_file(items, path):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['Loop', 'Tries', "Average"])
        for item in items:
            writer.writerow([item["loop"], item["tries"], item['average']])


def randomize(number, repeats):
    info = []
    count = 0
    cool_number = number

    while count <= repeats:
        count += 1
        tries = 0
        number = random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0,9)
        number = int(''.join(map(str, number)))
        while int(number) != cool_number:
            number = random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0,9), random.randint(0, 9)
            number = int(''.join(map(str, number)))
            tries += 1
        info.append({
            "loop": count,
            "tries": tries,

        })
    return info


randomized_info = randomize(69420, 99)
save_file(randomized_info, FILE)


df = pd.DataFrame(randomized_info)
print(df)
df.plot(kind="bar", x="loop", y="tries")
plt.show()
