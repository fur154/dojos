import unittest

def find_equi_index(inArray, numElements):
    name = inArray
    equi = []
    i=0
    for index in range(len(name)):
        if index == 0:
            if sum(name[index+1:]) == 0:
                equi = index
        elif index == len(name)-1:
            if sum(name[0:index]) == 0:
                equi = index
        else :
            if sum(name[0:index]) == sum(name[index+1:]):
                equi = index
    if equi == []:
        return -1
    if equi != []:
        return equi


A = [-5,-2,3,-1,-6] 
answ=find_equi_index(A,3)
print(answ)


if __name__ == '__main__':
	unittest.main()
