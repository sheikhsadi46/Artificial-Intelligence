import numpy as np
def fitness(popu, inp_list):
    ftness = np.zeros(len(popu), int)
    for indx in range(len(popu)):
        ftness[indx] = sum(popu[indx]*inp_list)
    return abs(target-ftness)

def crossover(x, y, inp_number):
    crossover_lst=np.zeros(inp_number, int)
    cross_point=np.random.randint(1,inp_number-2)
    for indx in range(cross_point):
        crossover_lst[indx]=x[indx]
    for j in range(cross_point, inp_number):
        crossover_lst[j]=y[j]
    return crossover_lst

def mutation(crossover_lst):
    random_point = np.random.randint(0, len(crossover_lst))
    crossover_lst[random_point]=np.random.choice([0, 1])
    return crossover_lst

def select(popu, fvalues):
    reform = 1/fvalues
    probability = (reform/sum(reform))
    selected = np.random.choice(fvalues, 1, True, probability)
    index = np.where(fvalues==selected[0])
    return population[index[0][0]]

def genetic(inp_list,population, inp_number, target, mutation_threshold = 0.3):
    fitnes=fitness(population,inp_list)
    counter=0
    while (target not in (fitness(population,inp_list)+target)) and counter!=5000:
        offsprings=np.zeros((len(population),inp_number),int)
        for indx in range(len(population)):
            x=select(population,fitnes)
            y=select(population,fitnes)
            crossover_lst=crossover(x,y,inp_number)
            mutation_chance=np.random.uniform(0.0,0.5)
            if mutation_chance<mutation_threshold:
                crossover_lst=mutation(crossover_lst)
            offsprings[indx]=crossover_lst
        population=offsprings
        fitnes=fitness(offsprings,inp_list)
        counter+=1
    max_fit=np.amin(fitnes)
    index=np.where(fitnes == max_fit)
    temp = False
    if target in (fitness(population,inp_list)+target):
        for i in population[index[0][0]]:
            if i == 1:
                temp = True
    if temp == True:
        solution=population[index[0][0]]
    else:
        solution=[-1]
    return solution

file = open("Lab 2.txt", "r")
inp_number=int(file.readline())
list2 = []
for i in range(inp_number):
    tran_type, tran_amount = file.readline().split(" ")
    
    if tran_type == "l":
        list2.append(-int(tran_amount))
    else:
        list2.append(int(tran_amount))
counter=0
while True:
    dummy_popu = np.random.randint(4,9)
    target = 0
    population = np.random.randint(0, 2, (dummy_popu, inp_number))

    out_result=genetic(list2,population, inp_number, target)
    string=list(map(str,out_result))
    
    if string[0]!="-1":
        break
    if counter>10:
        break
    counter+=1

print("".join(string))
file.close()