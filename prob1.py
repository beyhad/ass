class Stack:
	def __init__(self):		
	    self._data = []

	def push(self,i):
		self._data.append(i)

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def copy_reverse(self, A):
	    for i in range(len(self._data)):
	        A.push(self.pop())

	    print(A._data)	
	    

	    
if __name__ == '__main__':
	S = Stack()
	A = Stack()
	S.push(10)
	S.push(20)
	S.copy_reverse(A)
		
