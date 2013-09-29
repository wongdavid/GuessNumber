class Compare:
	def compare(self,listA,listB):
		a=0
		b=0
		for i in listA:
			for j in listB:
				if listA.index(i)==listB.index(j) and i==j:
					a += 1
				if listA.index(i)!=listB.index(j) and i==j:
					b += 1
		li = [a,b]
		return li
	def result(self,li):
		if li[0] == 4:
			return "True"
		else:
			return "%dA%dB"%(li[0],li[1])

if __name__ == "__main__":
	lia = [1,2,3,4]
	lib = [2,3,4,5]
	c = Compare()	
	print c.compare(lia,lib)
	print c.result([1,3])
				
