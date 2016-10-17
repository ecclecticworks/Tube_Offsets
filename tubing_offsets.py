#tubing offsets
tube_6 = 1.125 
tube_8 = 1.875
tube_12 = 3.375
tube_16 = 1.1875


#get tube diameter
dia = raw_input("> what diameter tube are you bending, 6, 8, 12, 16? ",)
dia = int(dia)
print (30 * '-')
if dia == 6:
		length = raw_input ("> What is your outside to outside dimension? >");
		length = float(length)
		OD = length + tube_6
		print "> mark your tubing at %s" % OD
	
elif dia == 8:
		length = raw_input ("What is your outside to outside dimension? >");
		length = float (length) 	
		OD = length+tube_8
		
		print "> Mark your tubing at %s " % OD
elif dia == 12:
		length = raw_input (">What is the outside to outside dimension? >");
		length = float(length)
		OD = length+tube_12
		print "> Mark your tunbing at %s" % OD
elif dia == 16:
		length = raw_input (">What is the outside to outside dimension? >");
		length = float(length)
		OD = length+tube_16
		print "> Mark your tubing at %s" % OD
		
else: 
		print "invalid selection"


res = raw_input ("would you like to enter another value?", yes, no)
	