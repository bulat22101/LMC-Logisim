fileInName = "in"  # input("Enter your filename")
fileOutName = "out"  # input("Enter name of result file")
commands = []
vs = set()  # переменные
cs = set()  # константы
labels = dict()  # метки
file = open(fileInName, "r")
lineNumber = 0
for line in file.readlines():
    command = []
    for part in line.strip().split():
        if len(part) > 0:
            command.append(part)
    if command[0][-1] == ":":
        labels[command[0][:-1]] = lineNumber
        command.pop(0)
    if command[0] == "add":
        commands.append([1, command[1]])
    if command[0] == "sub":
        commands.append([2, command[1]])
    if command[0] == "sta":
        commands.append([3, command[1]])
    if command[0] == "lda":
        commands.append([5, command[1]])
    if command[0] == "bra":
        commands.append([6, command[1]])
    if command[0] == "brz":
        commands.append([7, command[1]])
    if command[0] == "brp":
        commands.append([8, command[1]])
    if command[0] == "inp":
        commands.append([9])
    if command[0] == "out":
        commands.append([10])
    if command[0] == "hlt":
        commands.append([0])
    if len(command) > 1:
        if command[1].isdigit():
            cs.add(command[1])
        else:
            vs.add(command[1])
    lineNumber += 1
vsp = dict()
csp = dict()
for v in vs:
    vsp[v] = lineNumber
    lineNumber += 1
for c in cs:
    csp[c] = lineNumber
    lineNumber += 1
total = []
for command in commands:
    res = command[0] * 0x100000
    if 0 < command[0] < 6:
        if command[1].isdigit():
            res += csp[command[1]]
        else:
            res += vsp[command[1]]
    elif 5 < command[0] < 9:
        res += labels[command[1]]
    total.append(res)
for i in range(len(vsp) + len(csp)):
    total.append(0)
for key in csp.keys():
    pos = csp[key]
    total[pos] = int(key)
fout = open(fileOutName, 'w')
print("v2.0 raw", file=fout)
for res in total:
    print(hex(res)[2:], end=" ", file=fout)
