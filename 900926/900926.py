import random  # this should be helpful!


def probability_of_repeated_kmer(num_trials: int, n: int, k: int, alphabet_size: int) -> float:
    """
    Estimate the probability that a random genome contains two equal k-mers.

    Parameters:
        num_trials (int)    - How many random genomes to build (at least 1).
        n (int)             - The length of each random genome.
        k (int)             - The length of the k-mers to compare.
        alphabet_size (int) - How many distinct symbols the genome is built from.

    Returns:
        float - The fraction of the random genomes that contained some k-mer twice.
    """
    import random

def probability_of_repeated_kmer(num_trials: int, n: int, k: int, alphabet_size: int) -> float:
    if n < 2 * k:
        return 0.0

    repeated = 0

    for _ in range(num_trials):
        genome = [random.randrange(alphabet_size) for _ in range(n)]
        kmers = set()

        for i in range(n - k + 1):
            kmer = tuple(genome[i:i + k])

            if kmer in kmers:
                repeated += 1
                break

            kmers.add(kmer)

    return repeated / num_trials
