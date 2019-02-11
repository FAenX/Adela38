""" You are a leader of a small pirate crew. And you have a plan. 
With the help of OOP you wish to make a pretty efficient system 
to identify ships with a heavy booty on board.

Unfortunately for you, people weigh a lot this days, 
so how do you know if a ship if full of gold and not people?
You begin with writing a generic Ship class:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew


Every time your spies see a new ship enter the dock, 
they will create a new ship object based on their 
observations:
draft - an estimate of the ship's weight based on how low it is in the water
crew - the count of crew on board

Titanic = Ship(15, 10)


Taking into account that an average crew member on board adds 
1.5 units to the draft, a ship that has a draft of more than 
20 without crew is considered worthy to loot. Any ship weighing 
that much must have a lot of booty!
Add the method

Is_worth_it

to decide if the ship is worthy to loot. For example:

Titanic.is_worth_it() 
> False
 """


#we create a class Ship
class Ship(object):
	# the ship's __init__ method takes draft and crew as arguments. 
	def __init__(self, draft, crew):
		self.draft=draft
		self.crew=crew
		
		
	#we create a method which returns True if the ships draft-20 > the crew weight
	#else it returns false 	meaning it is not worth hijacking
	def is_worth_it(self):
		try:
			assert self.crew*1.5 < self.draft-20
			return True
		except AssertionError:
			return False		
	
		
#if the script is run directly without importing			
if __name__=='__main__':
	#initialize a new ship called titanic
	titanic=Ship(15,10)
	#check if the ship is worth hijacking
	print(titanic.is_worth_it())
	
