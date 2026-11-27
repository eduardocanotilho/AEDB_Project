
import os

DATA_FOLDER = "data"

def load_blosum(file_path):
	matrix = {}

	with open(file_path, "r") as handle:
		lines = [line.split() for line in handle if line.strip()]

	amino_acids = lines[0]

	for line in lines[1:]:
		amino_acid = line[0]
		scores = list(map(int, line[1:]))
		matrix[amino_acid] = dict(zip(amino_acids, scores))

	return matrix

def load_fasta(file_path):
	sequences = {}
	current_id = None

	with open(file_path, "r") as handle:
		for line in handle:
			line = line.strip()

			if not line:
				continue

			if line.startswith(">"):
				current_id = line[1:].split()[0]
				sequences[current_id] = ""
			else:
				sequences[current_id] += line

	return sequences

def load_data(filename):
	file_path = os.path.join(DATA_FOLDER, filename)

	if filename.endswith(".mat"):
		return load_blosum(file_path)

	elif filename.endswith(".fa") or filename.endswith(".fasta"):
		return load_fasta(file_path)