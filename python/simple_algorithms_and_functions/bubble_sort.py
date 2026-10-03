#----------------------------------------------------------------------
# Bubble Sort - sort into order
#
# Designed by Surjit Randhawa 2026
#----------------------------------------------------------------------

listVal = [3,2,1,5,4,0]

def bubble_sort(sortList):
	max = len(sortList)
	
	for n1 in range(max-1):
	  for n2 in range(max-n1-1):
	    if sortList[n2] > sortList[n2+1]:
	      temp = sortList[n2]
	      sortList[n2] = sortList[n2+1]
	      sortList[n2+1] = temp

print(listVal)
bubble_sort(listVal)
print(listVal)
