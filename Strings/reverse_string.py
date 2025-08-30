def reverseString(s):
    left,right=0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

# Example usage:
if __name__ == "__main__":
    s=["h","e","l","l","o"]
    print(reverseString(s)) # Output: ["o","l","l","e","h"]