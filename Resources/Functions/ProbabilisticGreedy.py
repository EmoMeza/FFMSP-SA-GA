import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.HammingFunctions as hf
import random

def Probabilistic_Greedy(sequences,threshold):
    uf.resetSequences(sequences)
    metric=hf.min_Hamming_Distance(sequences,threshold)
    answer=uf.build_PG_Solution(sequences,metric)
    return answer
