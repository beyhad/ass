class Stack:
	def __init__(self):		
	    self._data = []

	def push(self,x):
		self._data.append(x)

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

if __name__ == '__main__':
	s = Stack()
	List = [2,4,6,8,10,12,14,16,18,20]
	length=len(List)
	print(length)
	for i in range(len(List)):
		s.push(List[i])
	List = []
	for i in range(length):
		List.append(s.pop())
	print(List)
		