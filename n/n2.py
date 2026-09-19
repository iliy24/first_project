def format_name(last, first, middle=None):
   
    if middle is None:
        return last + " " + first
    else:
        return last + " " + first[0] + "." + middle[0] + "."


lst = []
m = int(input("Введите количество человек: "))

for i in range(m):
    name = input("Введите ФИО: ").split()
    if len(name) < 3:
        lst.append(format_name(name[0], name[1]))
    else:
        lst.append(format_name(name[0], name[1], name[2]))

print()
for el in lst:
    print(el)
