lines = []
with open('input', 'r') as f:
    for line in f:
        lines.append(int(line.strip()))

for line in lines:
    for line2 in lines:
        for line3 in lines:
            if line + line2 + line3 == 2020:
                print(line * line2 * line3)
