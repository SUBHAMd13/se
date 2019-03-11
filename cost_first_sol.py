
# Denomination of currency input taking from file xyz.txt and put output back in out.txt

fil1 = open("xyz.txt","r")
stri = fil1.read()
notes = []

for val in stri.split():
	notes.append(int(val))

amount = notes[-1]
if (amount <= 0):
	print("Invalid Input.")
else:
	arr = []
	while(amount > 0):
		for i in range(0, len(notes)-1):
			if(amount >= notes[i]):
				arr.append(amount/notes[i])
				
				amount = amount % notes[i]
			else:
				arr.append(0)

fil2 = open("out.txt","w")
fil2.write(str(arr))
fil1.close()
fil2.close()
