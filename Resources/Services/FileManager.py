import os
import Resources.Classes.Sequences as seq


def open_File_By_Name(name):
    current_path=os.getcwd() 
    file_path=current_path+"/Resources/Examples/"+str(name)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences

def get_Input_From_File(number,stage):
    if(stage==0):
        name="100-300-0"
    if(stage==1):
        name="100-600-0"
    if(stage==2):
        name="100-800-0"
    if(stage==3):
        name="200-300-0"
    if(stage==4):
        name="200-600-0"
    if(stage==5):
        name="200-800-0"
    current_path=os.getcwd() 
    if(number<10):
        filename=name+"0"+str(number)+".txt"
    elif(number==10):
        filename=name+"10.txt"
    file_path=current_path+"/Resources/Examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences
def save_To_File(average_time,number,stage):
    if(stage==0):
        name="100-300"
    if(stage==1):
        name="100-600"
    if(stage==2):
        name="100-800"
    if(stage==3):
        name="200-300"
    if(stage==4):
        name="200-600"
    if(stage==5):
        name="200-800"
    current_path=os.getcwd() 
    if(number==0):
        file_path=current_path+"/Resources/Data/ProbalisticTime_"+name+".txt"
    if(number==1):
        file_path=current_path+"/Resources/Data/DeterministicTime_"+name+".txt"
    file=open(file_path,"w")
    for i in range(0,len(average_time)):
        if(i==0):
            if(number==0):
                file.write("Probabilistic Greedy\n")
            if(number==1):
                file.write("Deterministic Greedy\n")
            file.write("Threshold: 0.75\n")
        if(i<10):
            file.write(name+str(i+1)+".txt\n\tTime:"+str(average_time[i][0])+"\n\tQuality: "+str(average_time[i][1])+"\n\tQuality Desviation: "+str(average_time[i][2])+"\n\tTime Desviation: "+str(average_time[i][3])+"\n")
        if(i==10):
            file.write("Threshold: 0.80\n")
        if(i<20 and i>=10):
            file.write(name+str(i-9)+".txt\n\tTime:"+str(average_time[i][0])+"\n\tQuality: "+str(average_time[i][1])+"\n\tQuiality Desviation: "+str(average_time[i][2])+"\n\tTime Desviation: "+str(average_time[i][3])+"\n")
        if(i==20):
            file.write("Threshold: 0.85\n")
        if(i<30 and i>=20):
            file.write(name+str(i-19)+".txt\n\tTime: "+str(average_time[i][0])+"\n\tQuality: "+str(average_time[i][1])+"\n\tQuality Desviation: "+str(average_time[i][2])+"\n\tTime Desviation: "+str(average_time[i][3])+"\n")
    file.close()