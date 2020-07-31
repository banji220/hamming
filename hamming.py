def distance(strand_a, strand_b):

    if len(strand_a) == len(strand_b):
        first_strand = [letter for letter in strand_a]
        second_strand = [letter for letter in strand_b]
    else:
        raise ValueError("The length of Sequences are not equal")
        
        
    diff = zip(first_strand, second_strand)
    count = []
    for x, y in diff:
        if x != y:
            count.append(x)
    print(count)
        
    return len(count)

