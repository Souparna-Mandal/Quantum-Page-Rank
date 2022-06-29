import PageRank


#PageRank.progrability_adjacency_list() will return the adjacency list with which we will work

#hilbert space will have number of nodes as dimensions with its own [a,b] prob amplitudes of heads and tails which after being m,uliplied by the coin operator will be split to the others and everything normalized


def normalise(position_probs, Nodess): #returns the list as normalised
    N= float(sum(position_probs))**(0.5)
    for states in range(len(Nodess)):
        for i in range(2): # there is only one T and H for every state Hx in the infinite dimensional hilbert space in the 1d quantum walk
            Nodess[states][i]= (Nodess[states][i]) / N
    return Nodess

def probabilities (positions_probs): # pass in the List containing the nodes with [h,t]
    for states in range(len(positions_probs)):
        h=positions_probs[states][0]
        t=positions_probs[states][1]
        positions_probs[states]=abs(h)**2 + abs(t)**2
    return positions_probs # list of amplitude squares of the head and tail prob amplitudes in each state in Hx X Hc

def ax_calc(adjacency_matrix,node_no):
    weighted_out_deg= 1
    weighted_in_deg=sum(adjacency_matrix[node_no-1])
    ax=weighted_in_deg/(weighted_out_deg+weighted_in_deg)
    return ax

def coin_operator(adjacency_matrix,node):





