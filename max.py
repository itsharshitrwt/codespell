

# python function to find maximum in arr[] of size n



def maximum(arr, n):

	# Initialize maximum element
	max = arr[0]

	#comparison 
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max



arr = [5,6,32,56,78,16,800]
n = len(arr)
Ans = maximum(arr, n)
print("Largest in given array ", Ans)
