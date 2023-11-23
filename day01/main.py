import heapq

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()

elf_sums = tuple(
    sum(map(int, elf.split()))
    for elf in raw.strip().split("\n\n")
)
top_three = heapq.nlargest(3, elf_sums)

print(top_three[0])
print(sum(top_three))
