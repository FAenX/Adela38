""" tests for the textgame module """
#import unittest for testing
import unittest
#the module being tested
import textgame 
#we import random to help us generate random numbers to be used in the test
import random
#we imort copy so that we can use it's deepcopy function. 
#(to remember states that are otherwise overwritten when tests are run)
import copy

#set variables required by textgame classes
xy=None

name=None

items=None

size=None
#this variable will hold the original position of the textgame.Player() instance before any movement 
position=[]

#test case for textgame.Room class
class RoomClassTestCase(unittest.TestCase):
	#initialize a new instance of Room class
	room=textgame.Room(name,size=xy,contents=items)	
	
	#test room.set_name function
	def test_set_name(self):
		#gernerate a string
		name_id=''
		for i in range(5):
			#string concatanation
			name_id+=str(i)
		#set the room name
		self.room.set_name(name_id)
		#assert that the name attribute in not None 	
		self.assertIsNotNone(self.room.name)
	
	#test Room.get_name method	
	def test_get_name(self):
		name_id=''
		for i in range(5):
			name_id+=str(i)
		#set the room name
		self.room.set_name(name_id)	
		#assert that the name set is the name of the room
		self.assertEqual(self.room.name,name_id)
	
	#test room.set_contents 
	def test_set_contents(self):
		#create a list using list comprehensions
		items=[str(i) for i in range(random.randint(0,5))]
		#set the room contents to be the created list
		self.room.set_contents(items)
		#ssert that the room contents is not None
		self.assertIsNotNone(self.room.contents)
	
	#test room.get_contents	
	def test_get_contents(self):
		#create a random list
		items=[str(i) for i in range(random.randint(0,5))]
		#set the contents
		self.room.set_contents(items)
		#assert that the contents are the contents we set
		self.assertEqual(self.room.contents,items)
	
	#test room.set_size()	
	def test_set_size(self):
		#generate a random size
		size=[random.randint(0,100),random.randint(0,100)]
		#set the room size to the generated size
		self.room.set_size(size)
		#assert that the room size is not None
		self.assertIsNotNone(self.room.size)
	
	#test room.get_size() method	
	def test_get_size(self):
		#generate a random size
		size=[random.randint(0,100),random.randint(0,100)]
		#set size
		self.room.set_size(size)
		#assert that the room size is the size we set
		self.assertEqual(self.room.size,size)

#test case for textgame.Player() class	
class PlayerClassTestCase(unittest.TestCase):
	#set variables used by the class	
	size=[random.randint(0,100),random.randint(0,100)]
	pos=[random.randint(0,50),random.randint(0,50)]
	
	#initialize instances of the textgame.Room and textgame.Player classes
	room=textgame.Room(name,size=size,contents=items)
	player=textgame.Player(name)	
	
			
	#test the default position of the player 
	def test_default_player_position(self):
		#create a new instance of player
		new_player=textgame.Player(name)
		#assert that the player is not in the room (new_player.in_room==False)
		self.assertFalse(new_player.in_room)
	
	#test player.set_position() function of the player instance	
	def test_set_position(self):
		#set the players position to pos 
		#if pos is is not outside the room size else set the player position to [0,0] (the door)	
		self.player.set_position(self.room.get_size(),self.pos)
		#assert that the player position is not None
		self.assertIsNotNone(self.player.get_position())
	#test the player.get_position() method 	
	def test_get_position(self):
		#set the player position
		self.player.set_position(self.room.get_size(),self.pos)
		#assert that the player position is not None
		self.assertIsNotNone(self.player.get_position())
	
	#test left movement	
	def test_move_left(self):
		#deepcopy the players current position
		position=copy.deepcopy(self.player.position)
		#set the players position
		self.player.set_position(self.room.get_size(),self.pos)	
		#move the player to the left by stride length (default stride is 1)	
		movement=self.player.move_left(self.room)
		#assert that the players new position is greater than the previous position
		self.assertTrue(self.player.get_position()[0] > position[0],print(f'from {position[0]} to {self.player.get_position()[0]}'))
	#test the player's right movement	
	def test_move_right(self):
		position=copy.deepcopy(self.player.position)
		self.player.set_position(self.room.get_size(),self.pos)
		movement=self.player.move_right(self.room)
		#assert that the players new position is less than the previous position
		self.assertTrue(self.player.get_position()[0] <= position[0],print(f'from {position[0]} to {self.player.get_position()[0]}'))
	#test the player's forward movement	
	def test_move_forward(self):
		position=copy.deepcopy(self.player.position)
		self.player.set_position(self.room.get_size(),self.pos)			
		movement=self.player.move_forward(self.room)
		#assert that the players new position is greater than the previous position
		self.assertTrue(self.player.get_position()[1] > position[1],print(f'from {position[1]} to {self.player.get_position()[1]}'))
	#test the player's back movement	
	def test_move_back(self):
		position=copy.deepcopy(self.player.position)
		self.player.set_position(self.room.get_size(),self.pos)			
		movement=self.player.move_back(self.room)
		#assert that the players new position is less than the previous position		
		self.assertTrue(self.player.get_position()[1] <= position[1],print(f'from {position[1]} to {self.player.get_position()[1]}'))
	#test that the player can exit the room	
	def test_player_exit(self):
		new_player=textgame.Player('name')
		new_player.exit()
		self.assertFalse(new_player.in_room)
	#test that the player can enter the room
	def test_enter(self):
		new_player=textgame.Player('name')
		new_player.enter()
		self.assertTrue(new_player.in_room)
		
			
#run the test script with verbosity=2 to increase output		
if __name__=='__main__':
	unittest.main(verbosity=2)
	
	
	
	
	
