line = 'abdjwawk'


line_new = line[0]
line_uniques = []
print(line[1:])
print(line_new)
for c in line[1:]:
    print(c)
    if c in line_new:
        line_uniques.append(line_new)
    else:
        line_new += c
line_uniques.append(line_new)

# your code here
print(line_uniques)
print(max(line_uniques,key=lambda x: len(x)))

