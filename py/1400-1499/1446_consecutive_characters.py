class Solution:
    def maxPower(self, s: str) -> int:
        """
            given a string s returns the max count of consecutive characters

            Args:
                s : (str) string to find the power of 

            Returns:
                max_power: (int) max number of consecutive chars
            
            __________________________________________________________________

            Time Complexity:
                O(n)

            Space Complexity:
                O(1)
        """

        if len(s) < 2:
            return len(s)

        prev_char = s[0]
        max_power, count = 1, 1

        for curr_char in s[1:]:
            if curr_char == prev_char:
                count += 1
            else:
                prev_char = curr_char
                max_power = max(max_power,count)
                count = 1
        return max(max_power, count)

