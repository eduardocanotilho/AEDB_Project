
import random
from cleanup import cleanup


def gap_insertion(msa: list[list[str]], rng: random.Random) -> list[list[str]]:

	new_msa = [row.copy() for row in msa]

	sequence_index = rng.randint(0, len(new_msa) - 1)
	position = rng.randint(0, len(new_msa[sequence_index]))
	gap_size = rng.randint(1, 3)
	new_msa[sequence_index][position:position] = ['-'] * gap_size

	return cleanup(new_msa)


def gap_deletion(msa: list[list[str]], rng: random.Random) -> list[list[str]]:

	new_msa = [row.copy() for row in msa]

	sequence_index = rng.randint(0, len(new_msa) - 1)

	gaps = []

	i = 0

	while i < len(new_msa[sequence_index]):

		if new_msa[sequence_index][i] == '-':
			start = i
			while i < len(new_msa[sequence_index]) and new_msa[sequence_index][i] == '-':
				i += 1
			gaps.append((start, i))
	
		else:
			i += 1

	if len(gaps) > 0:
		start, end = rng.choice(gaps)
		del new_msa[sequence_index][start:end]

	return cleanup(new_msa)


def mutate(msa: list[list[str]], rng: random.Random) -> list[list[str]]:

	if rng.random() < 0.5:
		return gap_insertion(msa, rng)

	else:
		return gap_deletion(msa, rng)
