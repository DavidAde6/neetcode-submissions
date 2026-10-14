class Node:
    def __init__(self):
        self.nextLetters = {}

class PrefixTree:

    def __init__(self):
        # we store first letter 
        self.store = {}
        

    def insert(self, word: str) -> None:
        #  str is inserted into prefixtree
        currStore = self.store
        index = 0
        while index < len(word) and word[index] in currStore:
                currStore = currStore[word[index]].nextLetters
                index += 1
        if index == len(word) and "." in currStore:
            return

        # meaning last char wasnt found or some previous character wasnt
        while index < len(word):
            currStore[word[index]] = Node() # e has node
            #print(index)
            currStore = currStore[word[index]].nextLetters # currstore is es next letters
            index += 1

        currStore["."] = Node()


    def search(self, word: str) -> bool:
        currStore = self.store

        index = 0
        #print(word)
        while word[index] in currStore:
            currStore = currStore[word[index]].nextLetters
            #print(currStore.keys())
            index += 1
            if index >= len(word):
                return "." in currStore
        return False

    def startsWith(self, prefix: str) -> bool:
        currStore = self.store

        index = 0
        while prefix[index] in currStore:
            currStore = currStore[prefix[index]].nextLetters
            index += 1
            if index >= len(prefix):
                return True

        return False