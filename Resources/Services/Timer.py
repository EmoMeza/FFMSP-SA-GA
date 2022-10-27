import time
import Resources.Functions.Greedys as gd
import Resources.Services.FileManager as fm
import numpy as np

def timer(sequence,threshold,number):
    if(number==0):
        average_time=0
        quality=0
        desviation_quality=[]
        desviation_time=[]
        sum_quality=0
        for i in range(0,10):
            start_time=time.time()
            quality=float(gd.Probabilistic_Greedy(sequence,threshold))
            end_time=time.time()
            sum_quality=quality+sum_quality
            desviation_quality.append(quality)
            desviation_time.append(end_time-start_time)
            average_time+=end_time-start_time
        answer=[]
        answer.append(average_time/10)
        quality=quality/10
        desviation_quality=np.std(desviation_quality)
        desviation_time=np.std(desviation_time)
        answer.append(str(quality))
        answer.append(str(desviation_quality))
        answer.append(str(desviation_time))
    if(number==1):
        average_time=0
        quality=0
        desviation_quality=[]
        desviation_time=[]
        sum_quality=0
        for i in range(0,10):
            start_time=time.time()
            quality=float(gd.Deterministic_Greedy(sequence,threshold))
            end_time=time.time()
            sum_quality=quality+sum_quality
            desviation_quality.append(quality)
            desviation_time.append(end_time-start_time)
            average_time+=end_time-start_time
        answer=[]
        answer.append(average_time/10)
        quality=quality/10
        desviation_quality=np.std(desviation_quality)
        desviation_time=np.std(desviation_time)
        answer.append(str(quality))
        answer.append(str(desviation_quality))
        answer.append(str(desviation_time))
    return answer
    
def get_answer_Time(stage):
    for j in range(0,2):
        average_time=[]
        threshold=0.75
        for i in range(0,30):
            if(i<10):
                sequence=fm.get_Input_From_File(i+1,stage)
                average_time.append(timer(sequence,threshold,j))
            if(i==10):
                threshold=0.80
            if(i<20 and i>=10):
                sequence=fm.get_Input_From_File(i-9,stage)
                average_time.append(timer(sequence,threshold,j))
            if(i==20):
                threshold=0.85
            if(i<30 and i>=20):
                sequence=fm.get_Input_From_File(i-19,stage)
                average_time.append(timer(sequence,threshold,j))
        fm.save_To_File(average_time,j,stage)
    return True