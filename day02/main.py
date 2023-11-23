INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()

rounds = raw.strip().splitlines()

points1 = {
    "A X": 3+1,
    "A Y": 6+2,
    "A Z": 0+3,
    "B X": 0+1,
    "B Y": 3+2,
    "B Z": 6+3,
    "C X": 6+1,
    "C Y": 0+2,
    "C Z": 3+3,
}
print(sum(points1[r] for r in rounds))


points2 = {
    "A X": 0+3,
    "A Y": 3+1,
    "A Z": 6+2,
    "B X": 0+1,
    "B Y": 3+2,
    "B Z": 6+3,
    "C X": 0+2,
    "C Y": 3+3,
    "C Z": 6+1,
}
print(sum(points2[r] for r in rounds))
