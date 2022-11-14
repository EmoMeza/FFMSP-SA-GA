from time import time
import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.LocalSearchFunctions as lsf
import Resources.Functions.HammingFunctions as hf
import random
import time

solutions=[]


def GA(sequences,threshold,t,metric,current_time,mutation_rate,population_size):
    cont_same=0
    last_gen_best=0
    i=1
    #Se crea la primera generacion utilizando el greedy probabilista
    first_generation=first_Generation(sequences,threshold,population_size)
    # Se ordena la primera generacion en base a su calidad y se guarda la mejor junto con su calidad y tiempo
    best_answer=fitness(sequences,first_generation,metric)[0]
    best_quality=uf.answer_Quality(sequences,best_answer,metric)
    best_time_found=time.time()-current_time
    # Antes de empezar el ciclo se guarda la primera generacion como la generacion actual
    current_generation=first_generation
    print(f'first generation created')
    while(t.is_alive()):
        #print the number of generation
        print(f'generation {i}')
        #ordenamos las respuestas de la generacion actual
        generation_ordered_by_fitness=fitness(sequences,current_generation,metric)
        print(uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric))
        #Revisamos si la mejor respuesta de la generacion actual es mejor que la mejor respuesta
        if(uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)>best_quality):
            first_generation[random.randint(0,population_size-1)]=best_answer
            best_answer=generation_ordered_by_fitness[0]
            best_quality=uf.answer_Quality(sequences,best_answer,metric)
            best_time_found=time.time()-current_time
            #print the quality of the best answer found and the time it took to find it
            print(f'best answer found: {best_quality} in {best_time_found} seconds')
        if(last_gen_best==uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)):
            cont_same+=1
            if cont_same==10:
                #create a new answer replacin the second best answer
                generation_ordered_by_fitness[1]=first_generation[random.randint(0,population_size-1)]
                #reset the counter
                cont_same=0
        else:
            #reset the counter
            cont_same=0
        #Se crea la nueva generacion utilizando crossover
        new_generation=crossover(generation_ordered_by_fitness)
        #Se mutan las respuestas de la nueva generacion
        new_generation=mutation(new_generation,mutation_rate,threshold)
        #La nueva generacion se convierte en la generacion actual
        last_gen_best=uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)
        current_generation=new_generation
        i+=1
    return best_answer,best_quality,best_time_found


#Se crea la primera generacion en base al greedy probabilista
def first_Generation(sequences,threshold,population_size):
    #print that the first generation is being created
    print('creating first generation')
    first_generation=[]
    for i in range(population_size):
        first_generation.append(lsf.constructionPhase(sequences,threshold))
        print(f'answer {i+1}/{population_size} created')
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
    
    tenth_list=tenth(answers_to_use)
    
    for i in range(len(answers)):
        new_answer=[]
        for j in range(10):
                new_answer+=tenth_list[random.randint(0,1)][j]
        new_generation.append(new_answer)
    return new_generation 

def tenth(answers):
    tenth_list=[]
    father=answers[0]
    mother=answers[1]
    father_genes=[]
    mother_genes=[]
    #first we save the genes of the father
    for i in range(10):
        gen=[]
        for j in range(int(len(father)/10)):
            gen.append(father[i*int(len(father)/10)+j])
        father_genes.append(gen)
    #then we save the genes of the mother
    for i in range(10):
        gen=[]
        for j in range(int(len(mother)/10)):
            gen.append(mother[i*int(len(mother)/10)+j])
        mother_genes.append(gen)
    tenth_list.append(father_genes)
    tenth_list.append(mother_genes)
    return tenth_list

#Mutacion se usa una vez creada una nueva generacion para mutar las respuestas
#de esta generacion. Se muta una respuesta si el numero aleatorio es menor al
#porcentaje de mutacion. Se muta una respuesta cambiando un elemento de la respuesta
#por un elemento aleatorio de la secuencia


def mutation(answers,mutation_rate,threshold):
    for i in range(len(answers)):
        if(random.random()<mutation_rate):
            for j in range(int(len(answers[0]))-int(float(len(answers[0]))*float(threshold))):
                position=random.randint(0,len(answers[0]))
                #position=random.randint(int(float(len(answers[0]))*float(threshold)),len(answers[0]))
                while True:
                    if(position==len(answers[0])):
                        position=0
                    answers[i][position]=random.choice(['A','C','G','T'])
                    if(random.random()>mutation_rate or position==len(answers[0])):
                        break
                    else:
                        position+=1
    return answers
