def ispalindrome(s):
    left,right=0,len(s)-1
    while left<right:
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right-=1
            continue
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True

# Example usage:
if __name__ == "__main__":
    print(ispalindrome("A man, a plan, a canal: Panama")) # Output: True
    print(ispalindrome("race a car")) # Output: False
       