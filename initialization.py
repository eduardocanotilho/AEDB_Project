import random
from cleanup import cleanup

def init_population(sequences: list[str], pop_size: int, max_gaps: int, rng: random.Random) -> list[list[list[str]]]:

	population: list[list[list[str]]] = []

	if pop_size < 1:
		print("pop_size must be at least 1.")
		return population
	if max_gaps < 0:
		print("max_gaps must be a positive number.")
		return population
	
	for i in range(pop_size):
		individual = []
		for sequence in sequences:
			leading_gaps = rng.randint(0, max_gaps)
			individual.append("-" * leading_gaps + sequence)
		msa = cleanup(individual)
		population.append(msa)
	return population