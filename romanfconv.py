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
try:
	with open(sys.argv[1]) as file:
		nScript = " ".join([line.strip() for line in file])
except:
	nScript = input("Code: ")
try:
	out = sys.argv[2]
except:
	pass
valid = ""
list = []
for i in nScript:
	old = valid
	valid += i
	try:
		roman.fromRoman(valid)
	except:
		valid = i
		list.append(str(roman.fromRoman(old)))
list.append(str(roman.fromRoman(valid)))
try:
	f = open(out, "w")
except:
	pass
else:
	f.write(" ".join(list))
	f.close()
finally:
	print(" ".join(list))
