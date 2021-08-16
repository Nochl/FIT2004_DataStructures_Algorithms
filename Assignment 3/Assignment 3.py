"""Assignment 3 - Enoch Leow 30600022"""


class node:
    """
    Class for each node in the Trie
    """
    def __init__(self, value=None):
        """
        Initialise a node with given value, child table with length of alphabet
        :param value: value of node (lowercase letter within the string)
        """
        self.value = value
        self.child = 26*[None]                                              # create table to store any childs
        self.prefixes = 1                                                   # record how many prefixes up to the node
        self.endofstring = 0                                                # record number of words which end at node


class Trie:
    """
    Class for Trie containing words in a given text
    """
    def __init__(self, text):
        """
        Initialise trie with root node and store text into trie
        :param text: list of strings comprised of lowercase letters
        :time_complexity: O(T), where T is the total character count over all strings in the list
        """
        self.root = node()                                                  # initialise root node
        self.insert_text(text)                                              # call insert_text to add it to trie

    def insert_string(self, string):
        """
        Add given string to the trie
        :param string: string comprised of lowercase letters
        :time_complexity: O(S), where S is the character count of string
        :return: None

        """
        self.root.prefixes += 1                                             # adds 1 to prefixes at root
        current_node = self.root
        for letter in string:                                               # insert each letter
            if current_node.child[ord(letter) - 97] is None:                # create new node if None
                current_node.child[ord(letter) - 97] = node(letter)
                current_node = current_node.child[ord(letter) - 97]
            else:                                                           # proceed down next trie node if it exists
                current_node = current_node.child[ord(letter) - 97]
                current_node.prefixes += 1                                  # adds 1 to its prefixes
        current_node.endofstring += 1                                       # adds 1 to end of string counter

    def insert_text(self, text):
        """
        Store text into trie
        :time_complexity: O(T), where T is the total character count over all strings in the list
        :param text: list of strings comprised of lowercase letters
        :time_complexity: O(T), where T is the total character count over all strings in the list
        :return: None
        """
        for string in text:                                                 # calls insert string for each word in text
            self.insert_string(string)

    def string_freq(self, query_str):
        """
        Return frequency of given string in the trie
        :param query_str: string comprised of lowercase letters
        :time_complexity: O(q), where q is length of query_str
        :return: frequency of given string in the trie
        """
        current_node = self.root
        for letter in query_str:                                            # navigates to correct node (end of string)
            if current_node.child[ord(letter) - 97] is None:
                return 0                                                    # returns 0 if string dosen't exist
            else:
                current_node = current_node.child[ord(letter) - 97]
        return current_node.endofstring                                     # returns the nodes endofstring counter

    def prefix_freq(self, query_str):
        """
        Return frequency of prefixes of given string in the trie
        :param query_str: string comprised of lowercase letters
        :time_complexity: O(q), where q is length of query_str
        :return: frequency of prefixes of given string in the trie
        """
        current_node = self.root
        for letter in query_str:                                            # navigates to correct node (end of string)
            if current_node.child[ord(letter) - 97] is None:
                return 0                                                    # returns 0 if string dosen't exist
            else:
                current_node = current_node.child[ord(letter) - 97]
        return current_node.prefixes                                        # returns the nodes prefixes counter

    def wildcard_prefix_freq(self, query_str):
        """
        Return list containing all the strings which have a prefix which matches query_str
        :param query_str: non-empty string consisting only of lowercase letters and exactly one '?'
        :time_complexity: O(q + S), where
            q is length of query_str
            S is the total number of characters in all strings of the text
        :return: list containing all the strings which have a prefix which matches query_str in lexicographic order
        """
        current_node = self.root
        base = ""                                                           # variable storing substring before "?"
        wildcard_strings = []                                               # all wildcard strings with matching prefix
        index = 0                                                           # index of "?"
        for letter in query_str:                                            # navigate to node before "?"
            if letter == "?":
                break
            else:
                base += letter
                current_node = current_node.child[ord(letter) - 97]
                index += 1

        newstr = query_str[index:]                                          # slices string from "?" to end

        for i in range(26):                                                 # navigates down all paths after "?"
            if current_node.child[i] is not None:
                for j in self.wildcard_search(newstr[1:], current_node.child[i]):
                    wildcard_strings.append(base + j)
        return wildcard_strings                                             # returns all strings with matching prefix

    def wildcard_search(self, query_str, node):
        """
        Recursive function which returns list of suffixes of query_str from node
        :param query_str:non-empty string consisting only of lowercase letters
        :param node: node in trie
        :time_complexity: O(q + S), where
            q is length of query_str
            S is the total number of characters in all strings of the text
        :return: list of suffixes of query_str from node
        """
        temp = []                                                           # stores all suffixes from node
        if len(query_str) == 0:                                             # base case if length of query_str is 0
            for i in range(node.endofstring):
                temp.append(node.value)                                     # append value to temp

        for i in range(25):                                                 # checks each child for paths down the trie
            if node.child[i] is not None:
                if query_str == "":
                    for j in self.wildcard_search(query_str[1:], node.child[i]):  # goes down if query_str is empty
                        temp.append(node.value+j)
                elif ord(query_str[0])-97 == i or query_str[0] == "?":      # goes down if query_str[0] = child or "?"
                    for j in self.wildcard_search(query_str[1:], node.child[i]):
                        temp.append(node.value+j)
        return temp                                                         # return list of suffixes of query_str


