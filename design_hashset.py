class MyHashSet:

	def __init__(self):
		self.capacity = 8
		self.size = 0
		self.s = [None] * 8
		self.lf = float(2) / 3

	def myhash(self, key):
		return key%self.capacity


	def add(self, key):
		if float(self.size)/self.capacity >= self.lf:
			self.capacity <<= 1
			ns = [None]*self.capacity
			for i in range(self.capacity >> 1):
				if self.s[i] and self.s[i] != "==TOMBSTONE==":
					n = self.myhash(self.s[i])
					while ns[n] is not None:
						n = (5*n+1)%self.capacity
					ns[n] = self.s[i]
			self.s = ns
		h = self.myhash(key)
		while self.s[h] is not None:
			if self.s[h] == key:
				return
			h = (5*h + 1) % self.capacity
			if self.s[h] == "==TOMBSTONE==":
				break
		self.s[h] = key
		self.size += 1


	def remove(self, key):
		h = self.myhash(key)
		while self.s[h]:
			if self.s[h] == key:
				self.s[h] = "==TOMBSTONE=="
				self.size -= 1
				return
			h = (5*h+1)%self.capacity


	def contains(self, key):
		h = self.myhash(key)
		while self.s[h] is not None:
			if self.s[h] == key:
				return True
			h = (5*h + 1)%self.capacity
		return False


obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)        
obj.contains(2)
obj.remove(2)         
obj.contains(2)