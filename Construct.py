import random
class Construct:
	def __init__(self):
		self.a = random.randint(0,9)
		self.b = random.randint(0,9)
		while (self.b == self.a):
			self.b = random.randint(0,9)
		self.c = random.randint(0,9)
		while (self.c == self.b or self.c == self.a):
			self.c = random.randint(0,9)
		self.d = random.randint(0,9)
		while (self.d == self.c or self.d == self.b or self.d == self.a):
			self.d = random.randint(0,9)

	def toList(self):
		li=[]
		li.append(self.a)
		li.append(self.b)
		li.append(self.c)
		li.append(self.d)
		return li
	a=0
	b=0
	c=0
	d=0

if __name__ == "__main__":
	con = Construct()
	print("%d,%d,%d,%d"%(con.a,con.b,con.c,con.d))
	print(con.toList())
