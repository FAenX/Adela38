#we will twst our module using unittest
import unittest
#we import random to use it to generate random numbers for our tests
import random
#we import our module
import captainpirate

#we craeate a test case class
class CaptainPirateTestCase(unittest.TestCase):
	#we generate random numbers for draft and crew
	new_draft=random.randint(0,100)
	new_crew=random.randint(0,50)
	titanic=captainpirate.Ship(new_draft,new_crew)
	
	#we test our titanic arguments are the ones we supplied
	def test_args(self):				
		#				
		self.assertEqual(self.titanic.draft,self.new_draft,print(f'draft => ({self.new_draft})'))
		self.assertEqual(self.titanic.crew,self.new_crew,print(f'crew => ({self.new_crew})'))
		
	#we test if titanic.is worth it works as expected given various values of crew and draft
	def test_is_worth_it(self):	
		titanic=captainpirate.Ship(self.new_draft,self.new_crew)

		if titanic.draft -20 > titanic.crew*1.5:
			self.assertTrue(titanic.is_worth_it(),print(f'draft=>{titanic.draft} crew=>{titanic.crew}\
														 crew_weight=>{titanic.crew * 1.5} {titanic.is_worth_it()}'))
		
		elif titanic.draft -20 <= titanic.crew*1.5:
			self.assertFalse(titanic.is_worth_it(),print(f'draft=>{titanic.draft} crew=>{titanic.crew}\
														 crew_weight=>{titanic.crew * 1.5} {titanic.is_worth_it()}'))
if __name__ =='__main__':		
	unittest.main(verbosity=2)
		
	
