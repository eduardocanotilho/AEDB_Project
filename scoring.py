def make_sub_matrix(match: int, mismatch: int, alphabet: str) -> dict:
	sub_matrix = {}

	for char1 in alphabet:
		sub_matrix[char1] = {}

		for char2 in alphabet:
			if char1 == char2:
				sub_matrix[char1][char2] = match
			else:
				sub_matrix[char1][char2] = mismatch

	return sub_matrix


def score_column(char1: str, char2: str, sub_matrix: dict, gap: int) -> int:

	if char1 == "-" and char2 == "-":
		return 0
	elif char1 == "-" or char2 == "-":
		return gap
	elif char1 == "X" or char2 == "X":
		return -1
	else:
		return sub_matrix[char1][char2]


def score_alignment(seq1: str, seq2: str, sub_matrix: dict, gap: int) -> int:
	total = 0

	for i in range(len(seq1)):
		total += score_column(seq1[i], seq2[i], sub_matrix, gap)

	return total


def score_msa(msa: list[list[str]], sub_matrix: dict, gap: int) -> int:

	total = 0

	for col in range(len(msa[0])):
		for i in range(len(msa)):
			for j in range(i + 1, len(msa)):
				total += score_column(msa[i][col], msa[j][col], sub_matrix, gap)

	return total