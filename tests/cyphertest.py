#we test our code using unittest module
import unittest
#we import the module we want to test
import cypher

#create a test case class
class DecodeTestCase(unittest.TestCase):
	#letters of alphabet
	alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	#we test if our function can decode 'scout','masterpiece' and 'cat'
	def test_decode(self):
		#the key 
		key=1939
		#assert that the decoded word is correct
		self.assertEqual(cypher.decode([ 20, 12, 18, 30, 21],key,self.alpha),'scout')
		self.assertEqual(cypher.decode([ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8],key,self.alpha),'masterpiece')
		self.assertEqual(cypher.decode([ 4, 10, 23],key,self.alpha),'cat')		
	
	
#this part runs if the module is run directly	
if __name__=='__main__':
	unittest.main(verbosity=2)
