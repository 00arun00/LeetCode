class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums : (List[int]) list of nums 
            target : (int) target which the two numbers should add up to 
        Returns:
            Solution :(List[int]) list of indices who add up to target
        -----------------------------------------------------------------
        key conepts:
            - dictionary

        Space complexity:
            o(n)

        Time complexity:
            o(n)

        """
        sum_dict = {}
        # loop through each element in the list of numbers 
        for i,num in enumerate(nums):
            # if we find the number in the sum_dict we are done
            if num in sum_dict:
                return [sol[num],i]
            # if number is not found we add {(target - num):i} to dict 
            else:
                sum_dict[target-num] = i
        #case where no solution is found
        assert 0,"No solution found"

