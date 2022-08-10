def getAverage(file):
    with open(file, "r") as f:
        for line in f:
            marks = [int(x) for x in str(line) if x.isdigit()]
            average = sum(marks) / len(marks)
            print(line.split()[0] + " " + line.split()[1] + ": " + str(average))


myFile = "marks.txt"
getAverage(myFile)
