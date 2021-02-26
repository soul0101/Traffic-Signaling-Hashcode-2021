from tqdm import tqdm
import operator
from operator import attrgetter
from library import *
from collections import defaultdict


def readF(filename):
    f = open(filename)

    D, I, S, V, F = [int(x) for x in f.readline().split(' ')[0:5]]
    streets = []
    cars = []
    for i in range (S):
        input = f.readline().replace('\n','').split(' ')
        B = int(input[0])
        E = int(input[1])
        name = input[2:-1]
        #print(name)
        time = int(input[-1])
        streets.append(
            Street(i, B, E, name, time)
        )

    for car in range (V):
        input = f.readline().replace('\n','').split(' ')
        P = int(input[0])
        street = input[1:]
        cars.append(
            Car(car, P, street)
        )

   
    return streets, cars


def outF(filename, sched):

    f = open(filename, 'w+')

    f.write(str(len(sched)) + '\n')

    for i in sched:
      f.write('{}\n'.format(i))
      f.write('{}\n'.format(len(sched[i])))
      for j in sched[i]:
        f.write(j[0]+' '+str(j[1])+'\n')

    f.close()

def solveAll(filename):
    streets, cars = readF(filename)

    traffic = []

    frequency_end = [0]*(len(streets))
    frequency_street = defaultdict(int)
    inc = defaultdict(list)

    for street in streets:
        frequency_end[street.E] += 1

    for street in streets:
        if(frequency_end[street.E]) == 1:
            traffic.append(
                Light(street.E, street.name[0], 1)
            )
    #print(traffic)

    for street in streets:
      inc[street.E].append(street.name)


    for car in cars:
        for i in car.street:
            frequency_street[i] += 1    

    new_frequency = sorted(frequency_street.items(), key = lambda x: x[1], reverse= True)

    for i in range (len(inc)):
        if(frequency_end[i] > 1):            
            for street in inc[i]:
                # traffic.append(
                #     Light(i, street[0], frequency_street[street[0]])
                # ) 
                traffic.append(
                    Light(i, street[0], 1)
                ) 

    sched = defaultdict(list)

    for i in traffic:
      sched[i.intersection].append([i.street,i.time])
                         

    #print(sched)

    outF(filename.replace('.txt', '') + '.out', sched)



solveAll("f.txt")