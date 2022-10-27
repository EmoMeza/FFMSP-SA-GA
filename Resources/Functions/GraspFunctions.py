from time import time
import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.LocalSearchFunctions as lsf
import time
global solutions
global best_answer

solutions=[]


def GRASP(sequences,threshold,t,metric,current_time):
    best_answer=[]
    for i in range(sequences[0].get_len()):
        best_answer.append('A')
    best_quality=0
    i=0
    while t.is_alive():
        answer=lsf.constructionPhase(sequences,threshold)
        new_answer=lsf.localSearchPhase(sequences,answer,metric)
        new_quality=uf.answer_Quality(sequences,new_answer,metric)
        if(new_quality>best_quality):
            best_answer=new_answer
            best_quality=new_quality
            print("New best answer found: "+str(best_answer))
            print("Quality: "+str(uf.answer_Quality(sequences,best_answer,metric)))
            print("Time elapsed: "+str(time.time()-current_time)+"seconds")
            solution=[best_answer,uf.answer_Quality(sequences,best_answer,metric),(time.time()-current_time)]
            solutions.append(solution)
        i+=1
    return True

