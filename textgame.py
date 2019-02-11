'''
A complete text game, the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.” '''

import sys

class Room(object):
	""" This class represents a Room object in the game. It has a name, a size and contents as properties
		the room size is the [x,y] of the room. The contents are items in the Room. 
		example room=Room('bedroom',size=[10,10],contents=['T.V']"""
	
	#initialize the Room object with name, size and contents
	def __init__(self,name,size=[],contents=[]):
		self.name=name
		self.size=size
		self.contents=contents
		
	#we set name using this method
	def set_name(self,name):
		self.name=name		
	#we get name using this method
	def get_name(self):
		return self.name
	#a method to set Room 'contents' property
	def set_contents(self,contents):
		self.contents=contents
		
	#a method to return Room 'contents' property
	def get_contents(self):
		return self.contents
	
	#a method to set Room 'size' property
	def set_size(self,size):
		self.size=size
		
	#a method to return Room 'size' property
	def get_size(self):
		return self.size		
		
	#__repr__ method return the string representation of the Room object
	def __repr__(self):
		#check if room has no contents
		if self.contents==[]:
			#string formating
			return f'{self.name} which is {self.size[0]} metres wide and {self.size[1]} metres long with no contents'
		else:
			return f'{self.name} which is {self.size[0]} metres wide and {self.size[1]} metres long containing {",".join(self.contents)}'

class Player(object):
	""" This class represents a payer object. The player has a name and stride properties. The stride is the 
		length of the player's single movement in meters in the left or right direction.
		example player=Player('emmanuel',stride=1)"""
	
	#initialization method. The player is not in the room by default i.e in_room=False , 
	#the stride defaults to 1 meter if not providedand the players position is an empty list by default
	def __init__(self,name,stride=1):
		self.name=name
		self.stride=stride
		self.in_room=False
		self.position=None
	
	#return the players current position	
	def get_position(self):
		return self.position
		
	#set the players position considering the room size
	def set_position(self,size,position):
		#_we check that the position given is not outside the room 
		#the contents of size list should be greater than the contents in position list
		_=[i>j for i,j in zip(size,position)]
		#if one item returns false, we consider the resulting list as false
		#we set the position to [0,0] 'the default door'
		if False in _ :
			_=False
			self.position=[0,0]
			print(f'''position outside the room : Reseting to {self.position}  ''')
		else:			
			self.position=position
		#by setting the position, the player enters the room	
		self.enter()	
	
	#the enter method puts the player in the room  	
	def	enter(self):
		self.in_room=True
	
	#a meethod to set the in_room property as False (t0 remove the player from the room)
	def exit(self):
		self.in_room=False
		self.position=None
		
	#method to move the player to the left by 'stride'
	def move_left(self,room):
		#get the Room width(x) using the Room.get_size() method at index=0
		x=room.get_size()[0]
		#verify that the player is in the room before proceeding
		if not self.in_room:
			raise ValueError('You have not entered any room')
			sys.exit()
		#check player's current position. if player players x=0, the player is at the rightmost position and therefore can move left
		# if player's position is < x, the player has not reached the leftmost position and can still move left
		if self.position[0] == 0 or self.position[0] < x:
			#add the player's stride to the current x position
			self.position[0]+=self.stride
			#Return the remaining distance in metres from the wall to the players current position
			return f'you are {self.position[0]} meters left'
		else:
			return f'You can’t move further in this direction.'
			#the player has reached the wall if x == the players current position
					
	
	def move_right(self,room):
		x=room.get_size()[0]
		#check player's current position. if player players x!=0, the player is some distance to the left so they can move right
		# if player's position is <= x, the player is some distance to the left so they can move right
		if self.position[0] != 0 and self.position[0] <= x:
			self.position[0] -= self.stride
			return f'you {x-self.position[0]} metres right '		
		elif self.position==[0,0]:
			return 'you are at the door'
		else:
			return f'You can’t move further in this direction.'
			
	def move_forward(self,room):
		#get the Room length(y) using the Room.get_size() method at index=1
		y=room.get_size()[1]
		if not self.in_room:
			raise ValueError('You have not entered any room')
			sys.exit()
		#if the player's position is y=0, the player is at the beginning position and can move forward
		#if the player's position is less than y, the player can still move forward
		if self.position[1] == 0 or self.position[1] < y:
			self.position[1]+=self.stride
			#return the players y position by substracting the current position from the total y
			return f'you are {self.position[1]} forward'
		else:
			#if the players current position == y, the player is at the wall 
			return 'You can’t move further in this direction.'			
	
	def move_back(self,room):
		#get the Room length(y) using the Room.get_size() method at index=1
		y=room.get_size()[1]
		if not self.in_room:
			raise ValueError('You have not entered any room')
			sys.exit()
		#if the player's position is y!=0, the player is some distance to the wall and can move back
		#if the player's position is <= y, the player can move back
		if self.position[1] !=0 and self.position[1] <= y:
			self.position[1] -= self.stride
			return f'you are {y-self.position[1]} meters back'
		
		elif self.position==[0,0]:
			return 'you are at the door'
		else:
			return 'You can’t move further in this direction.'	

			
#We run the script here				
if __name__=='__main__':
	#a list of dictionaries containing room data
	data=[{'name':'bedroom','size':[20,20],'contents':['bed','dressing table','mirror','bed lamp','moisturizer']},
			{'name':'Kitchen','size':[10,20],'contents':['cooker','cutlery']},
			{'name':'living room','size':[40,20],'contents':['T.V','Couch']},
			{'name':'empty room','size':[50,20],'contents':[]},
			]
			
	door_position=[2,2]
	
	#the main game loop.
	#the loop only breaks if the player has seen enough of the room and wants to report
	def main(room,player):
		while True:
			#the player can move left,right,forward or back
			#the direction of the movement is taken from user input
			direction=input(f'Which direction do {player.name} want to move? (left, right, forward, back) ')
			if direction.lower() == 'left':
				print(player.move_left(room))
			elif direction.lower() == 'right':
				print(player.move_right(room))
			elif direction.lower() == 'forward':
				print(player.move_forward(room))
			elif direction.lower()=='back':
				print(player.move_back(room))
			
			#if the user supplies input that is not valid we restart the loop
			else:
				continue
		
			#we exit the loop if the player has seen enough and wants to report 
				
			enough=input('Have you seen enough? reply with "yes" or "no" ')
			if enough.lower().startswith('y'):
				print(f'I am in a {room}')
				player.exit()
				break
			elif enough.lower()=='no':
				continue
			else:
				continue
			
	#the user is prompted to start the game
	prompt=input('do you want to Start? (reply with yes or no) ')		
	if prompt.lower().startswith('y'):	
		#we assign a variable index = 0 to move to the first room in the data
		index=0	
		name=input("Enter the player's name: ")
		#we initialize a player with name and stride
		player=Player(name,stride=1)
		#first we check to confirm that our data is not empty
		try:
			assert len(data)!=0
			#we initialize the room using data[index][key] to get the values
			room=Room(data[index]['name'],data[index]['size'],data[index]['contents'])
			while True:
				#the players enters the room
				player.set_position(room.get_size(),door_position)
				#we run the main game loop			
				main(room,player)
				#if the user wants to continue playing..
				cont=input('Do you want to enter the next room? ')
				if cont.lower().startswith('y'):
					#we move the player to the next room in the data by adding 1 to index
					index+=1
					try:
						room=Room(data[index]['name'],data[index]['size'],data[index]['contents'])
					#if we have exhausted the our data; we exit the game
					except IndexError:
						print(f'{player.name} has no more rooms to explore')
						sys.exit()
					
				else:
					print(f'{player.name} has quit')
					break
		except AssertionError:
			print('we do not have data for the rooms')						
			
	#if the user does not want to start the game, we exit		
	else:
		sys.exit()	
	
