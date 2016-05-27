def distance(dna_1, dna_2):
    """
    This function generates the hamming difference for two strands of DNA that are the same length

    :param dna_1:  DNA strand 1
    :param dna_2:  DNA strand 2
    :return:  hamming_difference
    """
    hamming_difference = 0

    # turn the strings into a list of characters
    a = list(dna_1)
    b = list(dna_2)

    # iterate through both lists and compares.  If they are not the same increment the hamming_difference
    for nucleotide_1, nucleotide_2 in map(None, dna_1, dna_2):
        if nucleotide_1 != nucleotide_2:
            hamming_difference += 1

    return hamming_difference