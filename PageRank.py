import math
import matplotlib.pyplot as plt
import numpy
import random
from scipy.sparse.linalg import eigs

global list_webpages1


def Graph_Creation(): # This function basically creates the nodes and the links for the Porgram to work
    global list_webpages1
# while writting the program follow G= d*M + (1-d)*e*v ( M is the transision matrix with prob replced for dangling nodes and the other part is to simulate teleportatio)....... follow the same in your random walk formulation... putting d to follow given probs to move( 1/n for dangling nodes)  and 1-d to teleport
    dict_adjacency_list= eval(input("Enter the Adjacency dictionary as {'webpage 1': [indices of connected webpages],...}: "))
    list_webpages1= list(dict_adjacency_list.keys())
    adjacency_list=list(dict_adjacency_list.values())
    return adjacency_list

def progrability_adjacency_list(adjacency_list): # basically fixes dangling nodes
    adjacency_list1=adjacency_list.copy()
    for nodes in range(len(adjacency_list)):
        l = float(len(adjacency_list[nodes]))
#        neighbors=[neighbor_prob/l for neighbor_prob in neighbors ]
        if len(adjacency_list[nodes])==0:
            l1=list(range(1,len(adjacency_list)+1,1))
            adjacency_list1[nodes].extend(l1)
            print(adjacency_list1)

    return adjacency_list1

def adjacency_matrix(adjacency_list):
    adj_matrix=[]
    for i in range (len(adjacency_list)):
        prob_matrix=[]
        for j in range(len(adjacency_list)):
            l= float(len(adjacency_list[i]))
            if (j+1 in adjacency_list[i]):
                prob_matrix.append(1/l)
            else :
                prob_matrix.append(0)
        adj_matrix.append(prob_matrix)
    # transpose of this will be the prob column matrix required
    h=numpy.transpose(numpy.array(adj_matrix)) # returns the adjacency matrix with updated columns
    return h

def Google_matrix(adj_matrix):
    d= 0.85
#    e=numpy.transpose(numpy.array([1 for i in range(len(adj_matrix))]))
    l= float(len(adj_matrix))
    v=numpy.array([[1/l for i in range(len(adj_matrix))]for i in range(len(adj_matrix) )])
    G=numpy.add(adj_matrix*d, (1-d)*v)
    return G


def Page_ranks_interative_matrix(Google,list_webpages): # page rank by multiplying the Google matrix iteratively until the Pagerank vector converges

    l=float(len(Google))
    Page_ranks=numpy.transpose(numpy.array([1/l for i in range(len(Google)) ]))
    for i in range(1,1000000):
        Page_ranks=numpy.matmul(Google,Page_ranks)
    print(sum(Page_ranks))
    for i in range (len(Page_ranks)):
        print(list_webpages[i] , ": ", Page_ranks[i])
    return Page_ranks

def Page_rank_Eigen_vector_matrix(Google,list_webpages): # theoretically calculating this by finding the eigenvector

    Eigen_val,Eigen_vec=eigs(Google, k=1)
    Eigen_vec=Eigen_vec.tolist()
    Eigen_val=Eigen_val.tolist()
    Page_ranks=[]

    for i in range(len(Eigen_vec)):
        Page_ranks.append(float(Eigen_vec[i][0].real))
    s=sum(Page_ranks)
    for i in range(len(Page_ranks)):
        Page_ranks[i]=Page_ranks[i]/s

    print(sum(Page_ranks))
    for i in range(len(Page_ranks)):
        print(list_webpages[i], ": ", Page_ranks[i])
    return Page_ranks

def Random_walk_pagerank(adjacency_list,list_webpages):
    l=float(len(adjacency_list))
    page_ranks=[1 for i in range(len(adjacency_list))]
    cur_pos=0
    for i in range(10000):
        rand= random.random()
        randint=random.randint(0,len(adjacency_list[cur_pos])-1)
        if (rand < 0.15):
            cur_pos= random.randint(0,int(l)-1)
            page_ranks[cur_pos]=page_ranks[cur_pos]+1
        else:
            cur_pos=adjacency_list[cur_pos][randint]-1
            page_ranks[cur_pos] = page_ranks[cur_pos] + 1
    s=sum(page_ranks)
    page_ranks=[k/s for k in page_ranks]
    print(sum(page_ranks))
    for i in range(len(page_ranks)):
        print(list_webpages[i], ": ", page_ranks[i])
    return page_ranks







#Main Program

adj_list=Graph_Creation()

print("\n\n\n REPEATED MULTIPLICATION TRANSITION MATRIX PAGERANK") # until the page rank values convered
PR1=Page_ranks_interative_matrix(Google_matrix(adjacency_matrix(progrability_adjacency_list(adj_list))),list_webpages1) # should run

print("\n\n\n RANDOM WALK PAGERANK")
PR2=Random_walk_pagerank(progrability_adjacency_list(adj_list),list_webpages1) # lets check

print("\n\n\n EIGENVECTOR TRANSITION MATRIX PAGERANK")
PR3=Page_rank_Eigen_vector_matrix(Google_matrix(adjacency_matrix(progrability_adjacency_list(adj_list))),list_webpages1) # doesnt work

X_axis=[]
for i in range(len(list_webpages1)):
    X_axis.append(float(i))
X_axis=numpy.array(X_axis)

bar1=plt.bar(X_axis , PR1, 0.1,color='r' )
bar2=plt.bar(X_axis + 0.1, PR2, 0.1,color='b' )
bar3=plt.bar(X_axis + 0.1*2, PR3, 0.1,color='g' )

plt.xlabel("Websites")
plt.ylabel('Page Ranks')
plt.xticks(X_axis+0.1,list_webpages1)
plt.legend( (bar1, bar2, bar3), ('Player1', 'Player2', 'Player3') )
plt.show()


#test data = {"hello.com":[5,2,3,4,7],"mathworks.org":[1,],"physics.com":[2,1],"lhc.co.sw":[3,2,5],"feynmanlectures.com":[4,1,6,3],"github.com":[5,1],"cern.com":[5,]}
# test data 2 ={"hello.com":[2,],"mathworks.com":[3,],"physics.com":[4,],"lhc.co.sw":[5,],"feynmanlectures.com":[1,]}