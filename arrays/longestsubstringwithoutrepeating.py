class Solution(object):
    def LengthOfLongestSubstring(self, s):
        seen={}
        left=0
        max_len=0
        for right,ch in enumerate(s):
            if ch in seen:
                left =max(left,seen[ch]+1)
            seen[ch]=right
            max_len= max(max_len,right-left+1)
        return max_len
    
# Exmaple usage
if __name__ == "__main__":
    s="abcabcbb"
    print("Length of Longest Substring Without Repeating Characters:", Solution().LengthOfLongestSubstring(s)) # Output: 3