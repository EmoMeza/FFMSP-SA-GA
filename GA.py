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
    best_agent=fitness(sequences,first_generation,metric)[0]
    best_quality=uf.answer_Quality(sequences,best_agent,metric)
    best_time_found=time.time()-current_time
    
    # Antes de empezar el ciclo se guarda la primera generacion como la generacion actual
    current_generation=first_generation
    print(f'first generation created')
    # Empezamos el ciclo
    while(t.is_alive()):
        
        # Se printea por pantalla la generacion actual
        
        # Se ordena la generacion actual en base a su calidad
        generation_ordered_by_fitness=fitness(sequences,current_generation,metric)

        #Revisamos si la mejor respuesta de la generacion actual es mejor que la mejor respuesta
        if(uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)>best_quality):
            
            # Se guarda la mejor respuesta anterior en la lista de la primera generacion
            first_generation[random.randint(0,population_size-1)]=best_agent
            
            # Se actualiza la mejor respuesta con su calidad y tiempo
            best_agent=generation_ordered_by_fitness[0]
            best_quality=uf.answer_Quality(sequences,best_agent,metric)
            best_time_found=time.time()-current_time
            
            #print the quality of the best agent found and the time it took to find it
            print(f'best agent found: {best_quality} in {best_time_found} seconds')
        
        #Reviamos si la mejor respuesta de la generacion actual es igual a la mejor respuesta de la generacion anterior 
        if(last_gen_best==uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)):
            
            # Si es igual aumentamos el contador de respuestas iguales
            cont_same+=1
            
            # Si el contador de respuestas iguales es igual a 10 reiniciamos el contador e ingresamos una respuesta de la primera generacion
            if cont_same==10:
                
                # Ingresamos una respuesta de la primera generacion
                generation_ordered_by_fitness[1]=first_generation[random.randint(0,population_size-1)]
                
                # Reiniciamos el contador
                cont_same=0
        else:
            
            # Reiniciamos el contador
            cont_same=0
        
        #Se crea la nueva generacion utilizando crossover
        new_generation=crossover(generation_ordered_by_fitness)
        
        #Se mutan las respuestas de la nueva generacion
        new_generation=mutation(new_generation,mutation_rate,threshold)
        
        # Se actualiza el mejor de la generacion anterior
        last_gen_best=uf.answer_Quality(sequences,generation_ordered_by_fitness[0],metric)
        
        #La nueva generacion se convierte en la generacion actual
        current_generation=new_generation
        i+=1
    return best_agent,best_quality,best_time_found


#Se crea la primera generacion en base al greedy probabilista
def first_Generation(sequences,threshold,population_size):
    
    #print that the first generation is being created
    print('creating first generation')
    
    #creamos la lista de agentes para la primera generacion
    first_generation=[]
    
    # Creamos una iteracion para cada agente de la primera generacion
    for i in range(population_size):
        
        # Añadimos un agente a la lista de agentes de la primera generacion
        first_generation.append(lsf.constructionPhase(sequences,threshold))
        
        # Se entrega el progreso de la creacion de la primera generacion
        print(f'agent {i+1}/{population_size} created')
    return first_generation

# La funcion fitness ordena la generacion actual en base a su calidad
# Esto lo hace creando una lista de calidades y ordenandola de mayor a menor
# Realizando los mismos cambios en la lista de agentes de la generacion actual
def fitness(sequences,current_generation,metric):

    # Creamos una lista de calidadess
    fitness=[]

    # Se crea una iteracion para cada agente de la generacion actual
    for agent in current_generation:
    
        # Se añade la calidad del agente a la lista de calidades
        fitness.append(uf.answer_Quality(sequences,agent,metric))
    
    #se ordena la lista de calidades de mayor a menor realizando los mismos cambios en la lista de agentes de la generacion actual
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

# Crossover se encarga de mezclar las mejores dos respuestas de la lista de agentes de la generacion actual
# 
def crossover(agents):
    # Creamos una lista de agentes para la nueva generacion
    new_generation=[]
    agents_to_use=[]

    # Se crea una iteracion para cada agente de la generacion actual
    for i in range(len(agents)):
        agents_to_use.append(agents[i])
    
    # Se obtiene una lista de los mejores dos agentes de la generacion actual
    tenth_list=tenth(agents_to_use)

    # Se crea una iteracion para cada agente de la generacion actual    
    for i in range(len(agents)):
        
        # Se crea una lista de agentes para la nueva generacion
        new_agent=[]

        # Se crea una iteracion para cada agente de la lista de los mejores dos agentes de la generacion actuals
        for j in range(10):
                new_agent+=tenth_list[random.randint(0,1)][j]

        # Se añade el agente a la lista de agentes de la nueva generacion
        new_generation.append(new_agent)
    return new_generation 


# La funcion tenth se encarga de devolver una lista con los genes de los mejores dos agentes de la lista de agentes de la generacion actual
def tenth(agents):
    tenth_list=[]
    father=agents[0]
    mother=agents[1]
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

# Mutacion se usa una vez creada una nueva generacion para mutar las respuestas
# de esta generacion. Se muta una respuesta si el numero aleatorio es menor al
# porcentaje de mutacion. Se muta una respuesta cambiando un elemento de la respuesta
# por un elemento aleatorio de la secuencia, y se repite este proceso hasta que la
# no se cumpla la condicion


def mutation(agents,mutation_rate,threshold):
    for i in range(len(agents)):
        if(random.random()<mutation_rate):
            for j in range(int(len(agents[0]))-int(float(len(agents[0]))*float(threshold))):
                position=random.randint(0,len(agents[0]))
                #position=random.randint(int(float(len(agents[0]))*float(threshold)),len(agents[0]))
                while True:
                    if(position==len(agents[0])):
                        position=0
                    agents[i][position]=random.choice(['A','C','G','T'])
                    if(random.random()>mutation_rate):
                        break
                    else:
                        position+=1
    return agents
