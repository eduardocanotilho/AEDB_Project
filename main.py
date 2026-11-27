
import random
from file_loading import load_data
from cleanup import cleanup
from initialization import init_population
from scoring import score_msa
from crossover_operator import crossover
from mutation import mutate


def main():
	rng = random.Random(42)

	sequences = load_data("cytochromes.fa")
	blosum = load_data("blosum62.mat")

	sequences = list(sequences.values())

	population = init_population(sequences, 10, 5, rng)

	for i in range(len(population)):
		score = score_msa(population[i], blosum, -8)

		print("Individual:", i + 1)
		print("Score:", score)

	parent1 = population[0]
	parent2 = population[1]

	child = crossover(parent1, parent2, rng)

	gap = 0
	print("\nCrossover")
	print("Score:", score_msa(child, blosum, gap))

	mutated = mutate(child, rng)

	print("\nMutation")
	print("Score:", score_msa(mutated, blosum, gap))

	print("\nFinal alignment")

	for sequence in mutated:
		print("".join(sequence))


if __name__ == "__main__":
	main()