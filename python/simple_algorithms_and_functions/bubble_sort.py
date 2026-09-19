
#----------------------------------------------------------------------
# Bubble Sort - sort into order
#----------------------------------------------------------------------

listVal = [0, 3, 5, 1, 7, 9]

def bubble_sort(sortList):
	max = len(sortList)
	temp=0
	
	for n1 in range(max-1):
	  for n2 in range(max-n1-1):
	    if sortList[n2] > sortList[n2+1]:
	      temp = sortList[n2]
	      sortList[n2] = sortList[n2+1]
	      sortList[n2+1] = temp

print(listVal)
bubble_sort(listVal)
print(listVal)
