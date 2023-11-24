import string

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
lines = raw.strip().split()

priorities = {c: i+1 for i, c in enumerate(string.ascii_letters)}

def shared_item(*strings: str) -> str:
    return next(iter(set.intersection(*map(set, strings))))

rucksacks = tuple((s[:len(s)//2], s[len(s)//2:]) for s in lines)
print(sum(priorities[shared_item(a, b)] for a, b in rucksacks))

groups = tuple(lines[3*i:3*(i+1)] for i in range(len(lines)//3))
print(sum(priorities[shared_item(a, b, c)] for a, b, c in groups))
