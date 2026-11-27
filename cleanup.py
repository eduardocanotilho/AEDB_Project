
def cleanup(msa: list[list[str]]) -> list[list[str]]:

	padded_msa: list[list[str]] = [list(row) for row in msa]
	max_length: int = 0

	for seq in padded_msa:
		row_len = len(seq)
		if row_len > max_length:
			max_length = row_len

	for seq in padded_msa:
		while len(seq) < max_length:
			seq.append('-')

	clean_msa: list[int] = []
	for i in range(max_length):
		all_gaps = True
		for row in padded_msa:
			if row[i] != '-':
				all_gaps = False
				break
		if not all_gaps:
			clean_msa.append(i)

	return [[row[i] for i in clean_msa] for row in padded_msa]