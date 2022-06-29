import math
import numpy
import matplotlib.pyplot as mlp

def coinToss (positions,coin): # positions is [[a,b],[a1,b1]....] where a and b are the prob of heads and tails and the index is the position ie its the hilbert space Hx X Hc
    for states in range(len(positions)): # coin ia 2 *2 matrix all numpy arrays
       # h= numpy.matmul(numpy.array([2,3]),numpy.array([[0,2],[2,3]]))
        positions[states]=(numpy.matmul(numpy.array(positions[states]),coin)).tolist()
    position_copy= positions.copy()
    position_probs=probabilities(position_copy)
    return normalise(position_probs,positions)

def normalise(position_probs, positions):
    N= float(sum(position_probs))**(0.5)
    for states in range(len(positions)):
        for i in range(2): # there is only one T and H for every state Hx in the infinite dimensional hilbert space in the 1d quantum walk
            positions[states][i]= (positions[states][i])/N
    return positions

def probabilities (positions_probs):
    for states in range(len(positions_probs)):
        h=positions_probs[states][0]
        t=positions_probs[states][1]
        positions_probs[states]=abs(h)**2 + abs(t)**2
    return positions_probs # list of amplitude squares of the head and tail prob amplitudes in each state in Hx X Hc

def Shift_operation (positions):
    shifted_positions= [([0, 0]) for i in range(len(positions))]
    for i in range(1,len(positions)-1): # moving heads to right and tails to left ..... the indices hold info as 0--> -N .. N+1-->0 ... 2N+1--> N in the position hilbert space
        shifted_positions[i+1][0]=positions[i][0]
        shifted_positions[i -1][1]=positions[i][1]
    return shifted_positions

def initaliser(): # [ H, T]
    N= int(input("Enter the number of steps in the Quantum Walk") )
    position = [[0, 0] for i in range(2*N+1)]
    ##initial state
    position[N]=[1/(2**(0.5)),1j/(2**(0.5))]
#    position[N] = [1/4,15**(0.5)/4]
    return [position, N]

def main():
    data=initaliser()
    coin=numpy.array([[1,1],[1,-1]]) #hammard's coin
    positions = data[0].copy()
    N= data[1]
    for i in range(N):
        positions=Shift_operation(coinToss(positions,coin))

    probs=probabilities(positions)
    print("Sum of Probabilities=", sum(probs))
    mlp.plot(range(-N,N+1),probs)
    mlp.show()

main()
