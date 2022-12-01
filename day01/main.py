INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()

elves = tuple(
    tuple(int(line) for line in chunk.split())
    for chunk in raw.split("\n\n")
)

print(max(sum(elf) for elf in elves))
print(sum(sorted(tuple(sum(elf) for elf in elves))[-3:]))
