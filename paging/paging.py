#Auther Bonile Kunana

#date 15/04/2023

# This code implement FIFO, LRU and Optimal algorthms
#  
#Fifo algorithm
from ctypes import pointer
import sys
import random
from turtle import right

"""Fifo algorithm"""
def Fifo(frameSize, pageArray):
    """initilise helping variables"""
    pointer = 0
    hit = 0
    miss = 0
    """define memory array and initilise entries to -1 """
    mainMemory = [-1 for i in range(frameSize)]
    """iterate through the bigger array"""
    for i in pageArray:
        flag = False
        """iterate through memory array"""
        for j in mainMemory:
            if j ==int(i):
                """check for page hits"""
                hit =hit+1
                flag = True
                break
        """check for page fault"""
        if (flag==False):
            miss =miss+1
            """replace the oldest element in the memory"""
            mainMemory[pointer] = int(i)
            pointer=pointer+1
            """controling the pointer"""
            if(pointer==frameSize):
                pointer = 0 
    return miss 

"""Least recently used algorithm"""
def lru(frameSize, pageArray):
    """initilise helping variables"""
    pointer = 0
    hit=0
    miss = 0
    """define memory array and initilise entries to -1 """
    mainMemory = [-1 for i in range(frameSize)]
    """iterate through the bigger array"""
    for i in range(len(pageArray)):
        flag = False
        """iterate through memory array"""
        for j in mainMemory:
            """check for page hits"""
            if j==int(pageArray[i]):
                hit =hit+1
                flag = True
                break
        """check for page faults"""
        if(flag==False):
            miss =miss+1
            """identify victime page"""
            if(pointer>=frameSize):
                left = pageArray[0:i]
                dist = [-1 for i in range(10)]
                present = [-1 for i in range(10)]
                len_of_left = len(left)
                len_of_mem = len(mainMemory)
                """these loops calculate the distances for replacement"""
                for j in range(len_of_left):
                    index = int(left[j])
                    dist[index] = i-j
                    for l in range(len_of_mem):
                        if mainMemory[l]==int(left[j]):
                            present[index] = l
                            break
                max = 0
                num = 0
                len_of_dist = len(dist)
                for j in range(len_of_dist):
                    if(present[j]>-1 and dist[j]> max ):
                        max = dist[j]
                        num = present[j]
                """replace victime page"""
                mainMemory[num] = int(pageArray[i])
            else:
                mainMemory[pointer] = int(pageArray[i])
                pointer += 1  
    return miss

"""Optimal algorithm"""
def optimal(frameSize,pageArray):
    """initilise helping variables"""
    pointer = 0
    hit=0
    miss = 0
    """initialise main memory to appropriate size"""
    mainMemory = [-1 for i in range(frameSize)]
    """iterate through Virtual memory"""
    for i in range(len(pageArray)):
        flag = False
        """iterate through main memory"""
        for j in mainMemory:
            """check for page hits"""
            if j==int(pageArray[i]):
                hit += 1
                flag = True
                break
        """check for page faults"""
        if(flag==False):
            miss += 1
            if(pointer>=frameSize):
                """this is for slicing the reference array"""
                right = pageArray[i+1:]
                """here we keep track of the distances for replacement"""
                dist = [-1 for i in range(10)]
                present = [-1 for i in range(10)]
                len_of_right = len(right)
                len_of_mainMemory = len(mainMemory)
                """these loops calculate the distances for replacement"""
                for j in range(len_of_right):
                    index = int(right[j])
                    dist[index] = i-j
                    for l in range(len_of_mainMemory):
                        if mainMemory[l]==int(right[j]):
                            present[index] = l
                            break
                max = 0
                num = 0
                """in this part we are doing the replacement"""
                for j in range(len(dist)):
                    if(dist[j]> max and present[j]>-1):
                        max = dist[j]
                        num = present[j]
                if(num!=0):
                    mainMemory[num] = int(pageArray[i])
            else:
                mainMemory[pointer] = int(pageArray[i])
                pointer += 1 
    return miss

def main():
    # TODO: Implement page replacement simulation
    size = int(sys.argv[1])
    
    """this is where we generate random values"""
    pages = []
    """this loop will run 32 times, to change the size of reference string change the range"""
    for i in range(0,23): 
        n = random.randint(0,9)
        pages.append(n)
    print("reference string = ",pages) # this is for the convinience of the marker
    """print out results"""
    print('FIFO', Fifo(size, pages), 'page faults.')
    print('LRU', lru(size, pages), 'page faults.')
    print('OPT', optimal(size, pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()    