from time import time
import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.LocalSearchFunctions as lsf
import random
import time

solutions=[]


def GA(sequences,threshold,t,metric,current_time,mutation_rate):
    i=0
    while t.is_alive():
        first_generation=first_Generation(sequences,threshold)
        best_answer=fitness(sequences,first_generation,metric)[0]
        best_quality=uf.answer_Quality(sequences,best_answer,metric)
        best_time_found=time.time()-current_time
        current_generation=first_generation
        print(f'first generation created')
        while(t.is_alive()):
            print(f'current generation: {i}')
            generation_ordered_by_fitness=fitness(sequences,current_generation,metric)
            print(uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric))
            if(generation_ordered_by_fitness[0]>best_answer):
                best_answer=generation_ordered_by_fitness[0]
                best_quality=uf.answer_Quality(sequences,best_answer,metric)
                best_time_found=time.time()-current_time
                print(f'new best answer found, quality: {best_quality}')
            new_generation=crossover(generation_ordered_by_fitness)
            new_generation=mutation(new_generation,mutation_rate)
            current_generation=new_generation
            i+=1
    return best_answer,best_quality,best_time_found


def first_Generation(sequences,threshold):
    first_generation=[]
    for i in range(20):
        first_generation.append(lsf.constructionPhase(sequences,threshold))
    return first_generation

def fitness(sequences,current_generation,metric):
    if(len(current_generation)==0):
        return False
    fitness=[]
    for answer in current_generation:
        fitness.append(uf.answer_Quality(sequences,answer,metric))
    for i in range(len(fitness)):
        for j in range(len(fitness)):
            if(fitness[i]>fitness[j]):
                temp=fitness[i]
                fitness[i]=fitness[j]
                fitness[j]=temp
                temp=current_generation[i]
                current_generation[i]=current_generation[j]
                current_generation[j]=temp
    return current_generation

def crossover(answers):
    new_generation=[]
    answers_to_use=[]

    for i in range(len(answers)):
        answers_to_use.append(answers[i])
    
    quarters_list=quarters(answers_to_use)
    
    for i in range(len(answers)):
        new_answer=[]
        for j in range(4):
                new_answer+=quarters_list[j][random.randint(0,len(quarters_list[j])-1)]
        new_generation.append(new_answer)
    
    return new_generation 
def quarters(answers):
    first_quarter=[]
    
    for i in range(int(len(answers)/2)):
        quarter=[]
        for j in range(int(len(answers[0])/4)):
            quarter.append(answers[i][j])
        first_quarter.append(quarter)
    
    second_quarter=[]
    for i in range(int(len(answers)/2)):
        quarter=[]
        for j in range(int(len(answers[0])/4),int(len(answers[0])/2)):
            quarter.append(answers[i][j])
        second_quarter.append(quarter)
    
    third_quarter=[]
    for i in range(int(len(answers)/2)):
        quarter=[]
        for j in range(int(len(answers[0])/2),int(len(answers[0])*3/4)):
            quarter.append(answers[i][j])
        third_quarter.append(quarter)
    
    fourth_quarter=[]
    for i in range(int(len(answers)/2)):
        quarter=[]
        for j in range(int(len(answers[0])*3/4),int(len(answers[0]))):
            quarter.append(answers[i][j])
        fourth_quarter.append(quarter)
    
    return [first_quarter,second_quarter,third_quarter,fourth_quarter]

def mutation(answers,mutation_rate):
    for i in range(len(answers)):
        if(random.random()<mutation_rate):
            for j in range(int(len(answers[0])/2)):
                position=random.randint(0,len(answers[0])-1)
                answers[i][position]=random.choice(['A','C','G','T'])
    return answers