try:
	import pip
except:
	import roman
else:
	try:
		import roman
	except:
		pip.main(["install","roman"])
import sys
size = 256
cells = [0]*size
pointer = 0
try:
	with open(sys.argv[1]) as file:
		nScript = [line.strip(" ") for line in file]
except:
	get = input("Code: ")
	nScript = get.split()
#print(nScript)
romanScript = ""
for i in nScript:
	try:
		romanScript += roman.toRoman(int(i))
	except:
		romanScript += i
#print(romanScript)
inputString = input("Input: ")
inIndex = 0
i = 0
while True:
	#print(romanScript[i],end="")
	if romanScript[i].upper() == "I":
		cells[pointer]+=1
	elif romanScript[i].upper() == "V":
		cells[pointer]-=1
	elif romanScript[i].upper() == "X":
		pointer+=1
	elif romanScript[i].upper() == "L":
		pointer-=1
	elif romanScript[i].upper() == "D":
		print(chr(cells[pointer]),end="")
		try:
			cells[pointer] = ord(inputString[inIndex])
		except:
			cells[pointer] = 0
		inIndex+=1
	elif romanScript[i].upper() == "C":
		if cells[pointer] == 0:
			count = 1
			while count > 0:
				i+=1
				if romanScript[i].upper() == "C":
					count+=1
				elif romanScript[i].upper() == "M":
					count-=1
	elif romanScript[i].upper() == "M":
		if cells[pointer] != 0:
			count = -1
			while count < 0:
				i-=1
				if romanScript[i].upper() == "C":
					count+=1
				elif romanScript[i].upper() == "M":
					count-=1
	i+=1
	if i == len(romanScript):
		sys.exit(0)