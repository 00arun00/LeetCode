class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
            Finds the number of students who are busy doing home work at a given time

            Args:
                startTime: (List[int]) list of start time for home work for 'i'th student
                endTime: (List[int]) list of end time for home work for 'i'th student
                queryTime: (int) time when we need to find the number of busy students

            Returns:
                count: (int) number of busy students

            _________________________________________________________________________________

            Time Complexity:
                O(n)

            Space Complexity:
                O(n)

        """
        count = 0

        for start,end in zip(startTime, endTime):
            if end >= queryTime and start <= queryTime:
                count += 1
        return count

