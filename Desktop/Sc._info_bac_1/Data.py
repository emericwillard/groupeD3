import csv
c = ""
with open("total_cases.csv", "r") as f:
    r = csv.reader(f)  
    for row in r:
        c += row[1] + "\t"
with open("covid", "w") as f:
    f.write(c[6:len(c)-1])

with open("covid", "r") as f:
    c = f.read()
    c = c.replace("\t", ", ")
    print(c)
with open("covid", "w") as f:
    f.write(str(c))
