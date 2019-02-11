"""Task
Write a function that accepts an array of integers code and a key number. As the result, it should return string containing a decoded message from the code.
Input / Output

The code is a array of positive integers.

The key input is a positive integer.

Example
decode([ 20, 12, 18, 30, 21],1939);  ==> "scout"
decode([ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8],1939);  ==>  'masterpiece' """

#we creare a function decode which takes code and key as arguments
def decode(code,key,alpha):
	#split 'key' into a list using list comprehensions
	key=[i for i in str(key)]
	#if len(code) is equal to len(key) decode the code directly	
	if len(code) == len(key):
		#substract each key value from code	to get decoded values using zip method	
		decoded=[int(x)-int(y) for x,y in zip(code,key)]
	
	#else if the length of the code is greater than the length of the key,
	#repeat the key at the end untill it is the same length as the code e.g m  a  s  t  e  r  p  i  e  c  e
	#																	  13   1  19 20  5 18 16  9  5  3  5
	#																	+  1   9  3  9  1  9  3  9  1  9  3

	elif len(code) > len(key):
		#record the initial index
		index=0
		#we create a loop and append the key[index] to the end of the key untill the length of the key equals the length of the code
		#and the loop exits
		while len(key) != len(code): 
			key.append(key[index])
			index+=1
			#if the index equals the last index of the key, reset index (index starts at zero so we substract 1 from the length)
			if index == len(key) - 1:
				index=0
		#substract each key value from code	to get decoded values using zip method
		decoded=[int(x)-int(y) for x,y in zip(code,key)]
		
	#else if the length of the code is less than the length of the key,
	#reduce the key to the length of the code	
	elif len(code) < len(key):
		new_key=key[0:len(key)-1]
		
		#substract each value from code	to get decoded values using zip method
		decoded=[int(x)-int(y) for x,y in zip(code,new_key)]
		
	#we match the decoded list to the letters of alphabet using the values in decoded as indices to get the decoded word
	#and join the list into a word (python indeces start at 0 so we substract 1 from i to get the corresponding letter of alphabet
	word=[alpha[i-1] for i in decoded]
	word=''.join(word)
		
	#return decoded	
	return word
		
	
#if the code is run directly as opposed to being imported, this part is called	
if __name__=='__main__':
	alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	key=1939
	code=[ 20, 12, 18, 30, 21]
	word=decode(code ,key,alpha)
	print(word)
	

