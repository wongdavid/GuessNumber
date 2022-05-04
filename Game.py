import Construct
import Compare

def switch(li):
	intli = []
	for i in li:
		intli.append(int(i))
	return intli

if __name__ == "__main__":
	construct = Construct.Construct()
	sourcelist = construct.toList()
	count = 10
	print("please input 4 numbers seprated by \",\"")
	inp = raw_input()
	inlist = inp.split(',')
	inlist = switch(inlist)
	compare = Compare.Compare()
	result = compare.result(compare.compare(sourcelist,inlist))
	boolean = not (result == "True") and count > 0
	while (boolean):
		count -= 1
		print("A hint: %r"%result)
		print("sorry, please try again.You have %d chance left\n"%(count))
		print("please input 4 numbers seprated by \",\"")
		inp = raw_input()
		inlist = inp.split(',')
		inlist = switch(inlist)
		result = compare.result(compare.compare(sourcelist,inlist))
		boolean = not (result == "True") and count > 0
	if result == "True":
		print("Congradulations, you get the right answer!")
	else:
		print("time up! sorry")
