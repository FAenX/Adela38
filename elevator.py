""" Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order):
left - The current floor of the left elevator
right - The current floor of the right elevator
call - The called floor, i.e. the floor you want to reach

It should return the name of the elevator closest to the called floor ("left"/"right").

In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

You can assume that the inputs will always be valid integers between 0-2.
Examples:
elevator(0, 1, 0); // => "left"
elevator(0, 1, 1); // => "right"
elevator(0, 1, 2); // => "right"
elevator(0, 0, 0); // => "right"
elevator(0, 2, 1); // => "right"
"""

#create elevator function
def choose_elevator(left, right, call):
	#if the absolute value of call-left < absolute value of call-right
	#then the left elevator is closer to the call than the right elevator
	if abs(call-left) < abs(call-right):
		return 'left'
	elif abs(call-left) > abs(call-right):
		return 'right'
	#if the absolute values are equal, we choose the right elevator 
	else:
		return 'right'
	
	
if __name__ == '__main__':
	left=0
	right=1
	call=0
	print(choose_elevator(left,right,call))
