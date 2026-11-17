
def count_residues(sequence: str) -> int:
    residues: set[str] = {"A", "G", "C", "T"} 
    count: int = 0
    for i in range(0, len(sequence)):
        if sequence[i] in residues:
            count += 1
    return count

#print(count_residues("--AC--"))

def index_at_residue(sequence: str, residues_count: int) -> int:
    residues: set[str] = {"A", "G", "C", "T"}
    index: int = 0
    count: int = 0
    while count != residues_count:
        if sequence[index] in residues:
            count += 1
        index += 1
    return index

#print(index_at_residue("--AC--GT", 2))

def split_at(alignment: list[str], residues_count: list[int]) -> (list[str], list[str], int):
    left: list[str] = []
    right: list[str] = []
    residues: list[str] = []
    
    index = index_at_residue(alignment[0], residues_count[0])
    i: int = 0

    for seq in alignment:
        left.append(seq[:index])
        right.append(seq[index:])
        residues.append(count_residues(left[i]))
        i += 1

    return (left, right, residues)

align1 = ["ATC-G-G-TT","A-CCGC-ATC","A-CCG--ATC"]

l1, r1, residues = split_at(align1, [3]*len(align1))
print(l1)
print(r1)
print(residues)
