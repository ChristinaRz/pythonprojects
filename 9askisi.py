code = raw_input()
code = list(code)
array = [0]*5
pointerLocation = 0
i = 0
c = 0
open_braces=0
braces_location=[]
while i < len(code):
        if code[i] == '<':
            if pointerLocation > 0:
                pointerLocation -= 1
        elif code[i] == '>':
            pointerLocation += 1
        elif code[i] == '+':
            array[pointerLocation] += 1
        elif code[i] == '-':
            if array[pointerLocation] > 0:
                array[pointerLocation] -= 1
        elif code[i] == '.':
            print chr(array[pointerLocation])
        elif code[i] == ',':
            x = ord(input())
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pointerLocation] = y


        elif code[i] == '[':		
		open_braces += 1
    		braces_location.append(i)                		
	elif code[i] == ']':
		if array[pointerLocation] == 0:
    			open_braces -= 1
		else:        	
			i = braces_location[open_braces-1]
	i += 1
