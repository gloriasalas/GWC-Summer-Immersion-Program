start = '''You wake up one morning and find yourself in a big crisis. 
Trouble has arised and your worst fears have come true. Zoom is out to destroy
the world for good. However, a castrophe has happened and now the love of 
your life is in danger. Which do you decide to save today?'''

print(start)
done = False
print(" Type 'Flash to save the world' or 'Flash to save the love of his life' ")
user_input = input()
while not done: 
	if user_input == "world":
		print (" Flash has to fight zoom to save the world. ")
		done = True
		
		print("Should Flash use lightening to attack Zoom or read his mind?")
		user_input = input()
		
		if user_input == "lightening":
			print("Flash defeats Zoom and saves the world!")
			done = True
			
		elif user_input == "mind":
			print("Flash might be able to defeat Zoom, but is still a disadvantage. ")
			done = True
		print("Flash is able to save the world.")
	elif user_input == "love":
			print ("In order to save the love of his life, Flash has to choose between two options. ")
			done = True
			
			print("Should Flash give up his power or his life in order to save the love of his life?")
			user_input = input()
			
			if user_input == "power":
				print("The Flash's speed is gone. But he is given the love of his life back into his hands. ")
				done = True
			elif user_input == "life":
				print("The Flash will die, but he sees that the love of his life is no longer in danger.")
				done = True
print("No matter the circumstances, Flash is still alive. ")