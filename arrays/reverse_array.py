def reverse_array(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

# Exmaple usage
if __name__ == "__main__":
    arr=[1,2,3,4,5]
    print("Reversed Array: ", reverse_array(arr)) # ouput : [5,4,3,2,1]