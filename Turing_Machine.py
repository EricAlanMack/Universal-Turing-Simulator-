
pre_tape = list(raw_input("Give me tape in starting position: "))
tape = []
tp = ''
for i in pre_tape:
	tape.append(int(i))
tape = tape + [0,0,0,0,0]
position = 0
lookup = {}

class instruction(object):					
#"""This is the class that generates states given arbitrary machine instructions."""
	def __init__(self, (e, a, b, c, d, f, g, h, i, j)): 
		self.alpha = a
		self.bravo = b
		self.charlie = c
		self.delta = d
		self.echo = e 
		self.fox = f
		self.golf = g
		self.hotel = h
		self.india = i
		self.juliet = j


		
	def run(self): 
		global tape
		global position 
		if tape[position] == self.alpha: 
			tape[position] = self.bravo
			position = position + self.charlie
			if self.delta == self.echo:
				self.run()
			elif self.delta == 'HALT':
				pass
			else: 
				lookup[self.delta].run() 	 		
		elif tape[position] == self.golf:
			tape[position] = self.hotel
			position = position + self.india 
			if self.juliet == self.fox: 
				self.run()
			elif self.juliet == 'HALT':
				pass 
			else: 
				lookup[self.juliet].run()
		global tp
		for i in range(len(tape)):
			tp = tp+str(tape[i])
				
counter = 1

tuples_list = []
command_map = {'l': -1, 'r': 1, 'n': 0}  

while True: 
	print_input_1 = int(raw_input("What does state %d print when scanner sees 1, (or '2' if finished)? " % counter))
	if print_input_1 == 2:
		break 
	move_input_1 = raw_input("Where does state %d send the scanner when it sees 1? " % counter)	
	
	ns_input_1 = raw_input("What state does state %d call when scanner sees 1? " % counter)
								
	print_input_0 = int(raw_input("What does state %d print when scanner sees 0? " % counter))
								
	move_input_0 = raw_input("Where does state %d send the scanner when it sees 0? " % counter)	
							
	ns_input_0 = raw_input("What state does state %d call when scanner sees 0? " % counter)
	
	if print_input_1 != 2:
		tuples_list.append((str(counter),
						1,
						print_input_1, 
						command_map[move_input_1], 
						ns_input_1, 
						str(counter),
						0,
						print_input_0, 
						command_map[move_input_0], 
						ns_input_0)) 	
	counter += 1 
	
#Need to instantiate classes. 

state_names_list = []

for i in range(len(tuples_list)):
	state_names_list.append('state'+str(i + 1))

for i in range(len(tuples_list)): 
	globals()[state_names_list[i]] = instruction(tuples_list[i])
	
for i in range(len(tuples_list)): 
	lookup[tuples_list[i][0]] = globals()[state_names_list[i]]
	

print "Your input tape was", ''.join(pre_tape)+'00000' 

state1.run()

new_tape=[]
for i in range(len(tape)): 
	new_tape.append(str(tape[i]))
	
print "Your output tape is", ''.join(new_tape)
