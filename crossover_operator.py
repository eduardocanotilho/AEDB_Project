
import random
from cleanup import cleanup


def count_residues(sequence: str) -> int:
	count: int = 0

	for char in sequence:
		if char != '-':
			count += 1

	return count


def index_at_residue(sequence: str, residues_count: int) -> int:
	index: int = 0
	count: int = 0

	while index < len(sequence) and count < residues_count:
		if sequence[index] != '-':
			count += 1
		index += 1

	return index


def split_at(alignment: list[str], residues_count: list[int]) -> (list[str], list[str], list[int]):
	left: list[str] = []
	right: list[str] = []
	residues: list[int] = []

	for i in range(len(alignment)):
		index = index_at_residue(alignment[i], residues_count[i])
		
		left.append(alignment[i][:index])
		right.append(alignment[i][index:])
		residues.append(count_residues(left[i]))

	return left, right, residues


def crossover(parent1: list[list[str]], parent2: list[list[str]], rng: random.Random) -> list[list[str]]:

	parent1 = cleanup(parent1)
	parent2 = cleanup(parent2)

	residues_count = []

	for sequence in parent1:
		total = count_residues(sequence)
		residues_count.append(rng.randint(0, total))

	left1, right1, residues1 = split_at(parent1, residues_count)
	left2, right2, residues2 = split_at(parent2, residues_count)

	child = []

	for i in range(len(parent1)):
		child.append(left1[i] + right2[i])

	return cleanup(child)
