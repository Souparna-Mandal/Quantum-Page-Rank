import math
import random

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

global n1 # no of steps right
global n2 # no of steps left
global depth
depth=100000 # odd so that we have clear distinct middle value     # set as float
n1=0
n2=0
randomWalkData={}
list_n1=[]
list_n2=[]

# things to do 1) make a grapgh of the N plots and do some basic checks by adding the probabilities to get to 1 and other stufff
# move onto thw QW and start reading the paper

def randomGen() :
    randNo= random.randint(0,depth)
    return randNo/float(depth)
def n1_n2_updater(prob_right):# prob lrft = 1- prob right
    global n1
    global n2
    randNo= randomGen() # between 0 and 1
    if (randNo < prob_right): # ignores that number and starts left and riught of it if if prob of right is 0.4 it takes till 0.399 for right and 0.400001 and so on for left
        n1=n1+1
    else :
        n2=n2+1
def n1_n2_reset():
    global n1
    global n2
    n1=0
    n2=0

def m_calculator(N,prob_right): # total number of strps = N
    for i in range(N):
        n1_n2_updater(prob_right)
    m=n1-n2
    list_n1.append(n1)
    list_n2.append(n2)
    n1_n2_reset()
    if (m in randomWalkData.keys()):
        randomWalkData[m]=randomWalkData[m]+1
    else :
        randomWalkData[m]=1

def walkInputs():
    No_of_walks = int(input("Enter the Number of Walks"))
    Prob_Right = float(input("Enter the probability for a right step"))
    N = int(input("enter the number of steps in each walk"))
    return [N,No_of_walks,Prob_Right]



def randomWalks_run(N,No_of_walks,Prob_Right):

    for i in range (No_of_walks):
        m_calculator(N,Prob_Right)


def plot_data():
    global data_list
    data_list= walkInputs() # [N,No_of_walks,Prob_Right]
    randomWalks_run(data_list[0],data_list[1],data_list[2])
    global x_values
    global y_values
    x_values= list(randomWalkData.keys())
    y_values= list(randomWalkData.values())
    y_values= [x/data_list[1] for x in y_values]  # gives the probability of each run
    plt.bar(x_values,y_values,width=0.1)
    plt.xlabel("Distance Travelled")
    plt.ylabel("probability")
    plt.show()


def analytical_theoretical_prob_calculator():
    m = int (input("Enter the distance between -N and N whose probabilities you want to compare "))
    ep=y_values[x_values.index(m)]
    print ("Experimental Probability: ", ep)
    N= int(data_list[0])
    p=data_list[2]
    q=1-p
    fact_N=math.factorial(N)
    fact_Naddm=math.factorial((N+m)//2)
    fact_Nsubm=math.factorial((N-m)//2)
    Calc_prob = (fact_N/(fact_Nsubm*fact_Naddm))*p**((N+m)//2)*q**((N-m)//2)
    print("Theoretical Probability : ",Calc_prob)
    print("Deivation from Theory : ",(ep-Calc_prob)*100/Calc_prob," %")
    print("**************************\n\n\n\n\n")

def mean_n1_n2_avg_deviation():
    print("EXPERIMENTAL VALUES")
    mean_n1=sum(list_n1)/len(list_n1)
    mean_n2=sum(list_n2)/len(list_n2)
    mean_m= mean_n1-mean_n2
    n1_disp=0
    for i in range(len(list_n1)):
        n1_=(mean_n1-list_n1[i])**2
        n1_disp=n1_+n1_disp
    n1_disp=n1_disp/len(list_n1)
    m_disp=math.sqrt(4*n1_disp)
    print("Mean n1: ", mean_n1)
    print("Mean n2: ", mean_n2)
    print("Mean m: ", mean_m)
    print("Mean m dispersion: ", m_disp)
    print("\n")


    print("THEORETICAL VALUES")
    p=data_list[2]
    q=1-p
    N = int(data_list[0])
    mean_n1=N*p
    mean_n2=N*q
    mean_m = mean_n1 - mean_n2
    m_disp=math.sqrt(4*N*p*q)
    print("Mean n1: ", mean_n1)
    print("Mean n2: ", mean_n2)
    print("Mean m: ", mean_m)
    print("Mean m dispersion: ", m_disp)

def N_relationship_checker():
    global list_n1
    global list_n2
    global  n1
    global n2
    global randomWalkData
    avg_distance_travelled=[] #list of log of displacement
    N_list=[]
    n1 = 0
    n2 = 0
    randomWalkData = {}
    list_n1 = []
    list_n2 = []
    for j in range (1,101):
        N_list.append(math.log(j))
        randomWalks_run(j, data_list[1], data_list[2])# i are the number of steps
        mean_n1 = sum(list_n1) / len(list_n1)
        n1_disp = 0
        for i in range(len(list_n1)):

            n1_ = (mean_n1 - list_n1[i]) ** 2
            n1_disp = n1_ + n1_disp
        n1_disp = n1_disp / len(list_n1)
        m_disp = math.sqrt(4 * n1_disp)
        avg_distance_travelled.append(math.log(m_disp))

        n1 = 0
        n2 = 0
        randomWalkData = {}
        list_n1 = []
        list_n2 = []
    slope = float((avg_distance_travelled[99]-avg_distance_travelled[20]))/(N_list[99]-N_list[20]) # havent taken the average
    print("Slope: ",slope )
    plt.plot(N_list,avg_distance_travelled)
    plt.ylabel("log  avg distance")
    plt.xlabel("N ")
    plt.show()





plot_data()
mean_n1_n2_avg_deviation()
N_relationship_checker()
#while True:
#    analytical_theoretical_prob_calculator()
#    val= (input("Enter 1 to keep checking for more values "))
#    if (val !="1"):
#        break















