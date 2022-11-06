from time import time
import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.LocalSearchFunctions as lsf
import random
import time

solutions=[]


def GA(sequences,threshold,t,metric,current_time,mutation_rate):
    i=1
    #Se crea la primera generacion utilizando el greedy probabilista
    first_generation=first_Generation(sequences,threshold)
    best_answer=fitness(sequences,first_generation,metric)[0]
    best_quality=uf.answer_Quality(sequences,best_answer,metric)
    best_time_found=time.time()-current_time
    current_generation=first_generation
    print(f'first generation created')

    while(t.is_alive()):
        #ordenamos las respuestas de la generacion actual
        generation_ordered_by_fitness=fitness(sequences,current_generation,metric)
        #Revisamos si la mejor respuesta de la generacion actual es mejor que la mejor respuesta
        if(uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)>best_quality):
            best_answer=generation_ordered_by_fitness[0]
            best_quality=uf.answer_Quality(sequences,best_answer,metric)
            best_time_found=time.time()-current_time
            #print the quality of the best answer found and the time it took to find it
            print(f'best answer found: {best_quality} in {best_time_found} seconds')
        #Se crea la nueva generacion utilizando crossover
        new_generation=crossover(generation_ordered_by_fitness)
        #Se mutan las respuestas de la nueva generacion
        new_generation=mutation(new_generation,mutation_rate)
        #La nueva generacion se convierte en la generacion actual
        current_generation=new_generation
        i+=1
    return best_answer,best_quality,best_time_found


#Se crea la primera generacion en base al greedy probabilista
def first_Generation(sequences,threshold):
    first_generation=[]
    for i in range(20):
        first_generation.append(lsf.constructionPhase(sequences,threshold))
    return first_generation

#El fitness revisa la calidad de cada respuesta y las ordena de mayor a menor
# en base a su calidad haciendo los mismos cambios en la lista de respuestas
# teniendo asi en la primera mitad de la lista las respuestas con mayor calidad 
def fitness(sequences,current_generation,metric):
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

#Crossover se encarga de mezclar las respuestas de la primera mitad de la lista
#Esto lo hacen guardando las respuestas de la primera mitad en cuartos y mezclando
#los cuartos de las respuestas de la primera mitad para crear las respuestas de la
#nueva generacion
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

#Esta funcion ayuda a crossover a crear los cuartos de las respuestas de la primera mitad
#de la lista de respuestas. Se encarga de crear una lista de 4 listas, cada una de estas
#listas contiene los cuartos de las respuestas de la primera mitad de la lista de respuestas
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


#Mutacion se usa una vez creada una nueva generacion para mutar las respuestas
#de esta generacion. Se muta una respuesta si el numero aleatorio es menor al
#porcentaje de mutacion. Se muta una respuesta cambiando un elemento de la respuesta
#por un elemento aleatorio de la secuencia
def mutation(answers,mutation_rate):
    for i in range(len(answers)):
        if(random.random()<mutation_rate):
            for j in range(int(len(answers[0])/2)):
                position=random.randint(0,len(answers[0])-1)
                answers[i][position]=random.choice(['A','C','G','T'])
    return answers