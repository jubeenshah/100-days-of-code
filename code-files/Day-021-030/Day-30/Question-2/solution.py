def permutationEquation(p):
    return [(p.index(p.index(i)+1)+1) for i in range(1, max(p)+1)]
permutationEquation([4,3,5,1,2])