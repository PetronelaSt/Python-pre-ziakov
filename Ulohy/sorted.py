def sortNames(file, newFile):
    sortedNames = []
    count = 0
    with open(file, 'r') as f:
        for line in sorted(f):
            sortedNames.append(line)
            count += 1
    with open(newFile, "w") as f:
        for i in range(1, count):
            f.write(sortedNames[i])
    print("Hotovo")

myFile = 'attendance.txt'
newFile = 'sortedAttendance.txt'
sortNames(myFile, newFile)

def addName(name):
    with open(newFile, "w") as f:
        for i in f:
            if
            f.write(sortedNames[i])
    print("Hotovo")
