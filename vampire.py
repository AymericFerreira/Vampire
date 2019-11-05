import itertools
import time
import numpy as np

def merge_list_and_convert_to_int(list1):
    finalList = []
    for element in list1:
        finalList += element
        
    int1 = int(''.join(finalList))
    return int1
        
        
def is_vampire_number(number):
    strListNumber = str(number)
    digitList = []
    for digit in strListNumber:
        digitList.append(digit)
    for sequence in list(itertools.permutations(digitList, len(strListNumber))):
        sequenceList = list(sequence)
        list1 = sequenceList[:len(sequenceList)//2]
        list2 = sequenceList[len(sequenceList)//2:]
        number1 = merge_list_and_convert_to_int(list1)
        number2 = merge_list_and_convert_to_int(list2)
        
        if int(number1) * int(number2) == number:
            return True
    return False
    

number = 1000174288

t1 = time.time()
for i in range(100):
    print(number, is_vampire_number(number))
print(time.time()-t1)