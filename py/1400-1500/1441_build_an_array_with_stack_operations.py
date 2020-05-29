class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
            return the stack commands to build array from an increasing array 1->n

            Args:
                target: (List[int]) array to be built
                n: (int) max element in source array
            Returns:
                commands: (List[str]) list of commands ["Push","Pop"]

            ________________________________________________________________________

            Time Complexity:
                O(n)
            Space Complexity:
                O(n)

        """
        commands = []
        prev = 1
        for i in target:
            commands += ["Push","Pop"]*(i-prev)
            commands.append("Push")
            prev = i +1 
        
        return commands 

