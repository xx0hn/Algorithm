# 336. Palindrome Pairs
# Hard

# 2544

# 228

# Add to List

# Share
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
 

# Constraints:

# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.
class TrieNode:
    def __init__ (self):
        self.children=collections.defaultdict(TrieNode)
        self.word_id=-1
        self.palindrome_word_ids=[]
class Trie:
    def __init__ (self):
        self.root=TrieNode()
    
    @staticmethod
    def is_palindrome(word:str)->bool:
        return word[::]==word[::-1]
    
    def insert(self, index, word)->None:
        node=self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node=node.children[char]
        node.word_id=index
    
    def search(self, index, word)->List[List[int]]:
        result=[]
        node=self.root
        
        while word:
            if node.word_id>=0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
                if not word[0] in node.children:
                    return result
                node=node.children[word[0]]
                word=word[1:]
        if node.word_id>=0 and node.word_id!=index:
            result.append([index, node.word_id])
        for palindrome_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result
        
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie=Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)
        result=[]
        for i, word in enumerate(words):
            result.extend(trie.search(i, word))
        return results
