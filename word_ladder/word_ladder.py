# Given two words (beginWord and endWord), and a dictionary's word list, \
# return the shortest transformation sequence from beginWord to endWord, 
# such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Words                             vertex
# letters differnet                 edges
# shortest transformation sequence  path/bfs
# Dictionary                        list of vertexes
# beginword                         starting vertex
# endword                           destination vertex
# No duplicates                     uses a set()
# Same Length                       edges

f = open('words.txt', 'r')
words = f.read().split("\n")

word_set = set()
for word in words:
    word_set.add(word.lower())

# find/create all nodes/edges for words with one letter different
# replaces 
def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def find_word_ladder(beginWord, endWord):
    qq = Queue()
    visited = set()
    qq.enqueue([beginWord])

    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1] # Vertex is words
        if vertex not in visited:
            if vertex == endWord:
                return path
            visited.add(vertex)
            for new_vert in get_neighbors(vertex):
                new_path = list(path)
                new_path.append(new_vert)
                qq.enqueue(new_path)

print(find_word_ladder("sail", "boat"))