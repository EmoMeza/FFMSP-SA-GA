import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.ProbabilisticGreedy as pg
import random

def find_Better_Char(sequences,answer,metric,position):
    new_answer=answer
    if(answer[position]=='A'):
        char_available=['C','G','T']
    elif(answer[position]=='C'):
        char_available=['A','G','T']
    elif(answer[position]=='G'):
        char_available=['A','C','T']
    elif(answer[position]=='T'):
        char_available=['A','C','G']

    quality_A=0
    quality_C=0
    quality_G=0
    quality_T=0

    for char in char_available:
        new_answer[position]=char
        new_quality=uf.answer_Quality(sequences,new_answer,metric)
        if(new_quality>uf.answer_Quality(sequences,answer,metric)):
            if(char=='A'):
                quality_A=new_quality
            elif(char=='C'):
                quality_C=new_quality
            elif(char=='G'):
                quality_G=new_quality
            elif(char=='T'):
                quality_T=new_quality

    max_qualities=[]
    if(quality_A>quality_C and quality_A>quality_G and quality_A>quality_T):
        max_qualities.append('A')
    if(quality_C>quality_A and quality_C>quality_G and quality_C>quality_T):
        max_qualities.append('C')
    if(quality_G>quality_A and quality_G>quality_C and quality_G>quality_T):
        max_qualities.append('G')
    if(quality_T>quality_A and quality_T>quality_C and quality_T>quality_G):
        max_qualities.append('T')
    if(len(max_qualities)>0):
        answer[position]=random.choice(max_qualities)
    return answer

def constructionPhase(sequences,threshold):
    return pg.Probabilistic_Greedy(sequences,threshold)
    # return pg.build_random_sequence(sequences)

def localSearchPhase(sequences,answer,metric):
    i=int(0.8*len(answer))
    improvement=True
    while improvement:
        new_answer=find_Better_Char(sequences,answer,metric,i)
        if(new_answer[i]==answer[i]):
            #return answer
            i+=1
        else:
            answer=new_answer
            i+=1
        if i==len(answer):
            return answer
    return True