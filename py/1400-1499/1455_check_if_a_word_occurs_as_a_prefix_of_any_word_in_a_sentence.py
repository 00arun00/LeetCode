class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
            checks if a search word is prefix of any of the words in a 
            sentence and returns the index of the matching word

            Args:
                sentence : (str) sentence to be tested
                searchWord : (str) word to be searched for

            Returns:
                word_idx : (int) index of that matching word [-1 if not found]
        ______________________________________________________________________

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)

        """
        for i,word in enumerate(sentence.split()):
            if self.isPrefix(word,searchWord):
                return i+1
        return -1


    @staticmethod
    def isPrefix(word: str, searchWord: str) -> bool:
        """
            helper function: 
            returns true if searchWord is the prefix of the given word

            Args:
                word : (str) word to be checked
                searchWord : (str) word to search for 
            Returns:
                is_prefix : (bool) True if search word is a prefix else False 
        """
        l = len(searchWord)
        if l > len(word):
            return False

        return word[:l] == searchWord:

