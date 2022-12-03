from string import ascii_letters

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
sacks = raw.strip().split()

def f(s) -> str:
    i = len(s)//2
    l, r = s[:i], s[i:]
    inter ,= set(l) & set(r)
    return inter
priority = {
    it: i+1
    for i, it in enumerate(ascii_letters)
}
print(sum(priority[f(s)] for s in sacks))

groups = tuple(
    tuple(sacks[3*i:3*(i+1)])
    for i in range(len(sacks)//3)
)
def g(a, b, c) -> str:
    inter ,= set(a) & set(b) & set(c)
    return inter
print(sum(priority[g(*group)] for group in groups))
