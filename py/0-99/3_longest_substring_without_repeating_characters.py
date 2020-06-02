class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        """
            Takes in a string S and returns the length of the longest 
            substring without repeating characters

            Args:
                S : (str) String of chars
            Returns:
                maxLength : (int) length of longest substring

        ---------------------------------------------------------------------

        Time Complexity:
            o(n)

        Space complexity:
            o(n)

        """
        start = maxLength = 0 

        usedChars = {}

        for idx, char in enumerate(S):
            if char in usedChars and start <= usedChars[char]:
                start = usedChars[char] + 1
            else:
                maxLength = max(maxLength, idx - start + 1)
            usedChars[char] = idx
        return maxLength
