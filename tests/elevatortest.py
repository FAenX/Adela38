#import unittest module 
import unittest
#import our module to be tested
import elevator

#create elevator test case class
class ElevatoTestCase(unittest.TestCase):
	#create our tests
	def test_elevator(self):
		#assert equal dependinf on the positions of the elevator and the call
		#should return either left or right 		
		self.assertEqual(elevator.choose_elevator(0,1,0),'left')
		self.assertEqual(elevator.choose_elevator(0,1,1),'right')
		self.assertEqual(elevator.choose_elevator(0,1,2),'right')
		self.assertEqual(elevator.choose_elevator(0,0,0),'right')
		self.assertEqual(elevator.choose_elevator(0,2,1),'right')
		
		
#if we run our tests directly		
if __name__=='__main__':
	unittest.main(verbosity=2)


