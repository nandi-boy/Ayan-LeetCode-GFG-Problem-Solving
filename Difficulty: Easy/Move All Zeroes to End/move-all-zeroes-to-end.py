class Solution:
	def pushZerosToEnd(self, arr):
    	arr2 = []
    	for i in range(len(arr)):
    	    if(arr[i]!=0):
    	        arr2.append(arr[i])
    	if(len(arr)!=len(arr2)):
    	     for i in range(len(arr)-len(arr2)):
    	         arr2.append(0)
        for i in range(len(arr)):
            arr[i]=arr2[i]
        return arr2