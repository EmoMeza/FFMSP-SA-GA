import Resources.Services.FileManager as fm
import Resources.Functions.HammingFunctions as hf
import Resources.Functions.GraspFunctions as grsp
import GA as GA
import random
import sys
from time import sleep
import time
import threading
from Resources.Functions.GraspFunctions import solutions



def timer(seconds):
    for i in range(seconds):
        sleep(1)
    return True


def main():

    

    file_name=sys.argv[2]
    seconds=sys.argv[4]
    threshold=float(sys.argv[6])
    population=int(sys.argv[10])
    mutation_rate=float(sys.argv[12])
    
    if(sys.argv[8]=="1"):
            tuning=True
    else:
        tuning=False

    t=threading.Thread(target=timer,args=[int(seconds)])
    sequences=fm.open_File_By_Name(file_name)
    t.start()
    metric=hf.min_Hamming_Distance(sequences,threshold)
    current_time=time.time()
    best_answer=GA.GA(sequences,threshold,t,metric,current_time,mutation_rate,population,tuning)
    
    if tuning == True:
        print(f'{-best_answer[1]}')
    else:
        print(f'Final best answer found: {best_answer[0]}')
        print(f'Final quality: {best_answer[1]}')
        print(f'Final time elapsed: {best_answer[2]}')

if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("Incorrect execution:\tNo Arguments\n")
        print("For help, enter the following argument:")
        print("\tpython3 main.py -h")

    elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("\t\t\t~~~~~~~~")
        print("\t\t\t| Help |")
        print("\t\t\t~~~~~~~~\n")
        print("For correct execution of the program, you must enter the following arguments:\n")
        print("\tpython3 grasp.py -i [Filename] -t [MaxTimeInSeconds] -th [threshold] -p [PopulationSize] -mr [MutationRate] -tuning [TuningMode]\n")
        print("Example: python3 main.py -i 100-300-001.txt -t 90 -th 0.8 -tuning 0 -p 10 -mr 0.4 ")
        print("This program will display the time and quality of the solution obtained")

    elif((len(sys.argv)==13 and sys.argv[1]=="-i" and sys.argv[3]=="-t" and sys.argv[5]=="-th" and sys.argv[7]=="-tuning" and sys.argv[9]=="-p" and sys.argv[11]=="-mr")):
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 main.py -h")
        