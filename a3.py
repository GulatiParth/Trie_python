def get_idx(ch):
	return ord(ch.lower()) - ord('a')
	
class Trie:
	class TrieNode:
		def __init__(self):
			self.node: dict[str,Trie] = {}
   
	def __init__(self):
		self.root: dict[str,Trie] = {}
		self.endofword = False

	# function adds word to the Trie
	def insert(self, word):
		ptr = self
		for char in word:
			if char not in ptr.root:
				ptr.root[char] = Trie() 
			ptr = ptr.root[char] 
		ptr.endofword = True  

	# function searches for word in the Trie, returns True if found, False otherwise
	def search(self, word):
		ptr = self
		for char in word: 
			if char not in ptr.root:
				return False
			ptr = ptr.root[char] 
		return ptr.endofword


	def listing(self,node, list_word,stored_list): 
		if node.endofword:	
			stored_list.append(list_word)
			
		for number, use in node.root.items():
			self.listing(use, list_word + number,stored_list)
   
   
	# function returns the list of all words in the Trie in alphabetical order
	def get_all(self):
		list = [] 
		self.listing(self,"",list)
		list.sort()
		return list
			
		
	# function returns the list of all words that begin with prefix in the Trie in
	# alphabetical order
	def begins_with(self, prefix):
		ptr = self 
		list = [] 
		for char in prefix:
			if char not in ptr.root: 
				return []
			ptr = ptr.root[char]

		self.listing(ptr,prefix,list) 
		list.sort() 
		return list