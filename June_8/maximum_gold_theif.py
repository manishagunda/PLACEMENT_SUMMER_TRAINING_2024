'''
ip [3,9,4,1,5,7] quantity of gold
thief not stole conscutive houses bcz of alarm
op
max gold he can stole
=9+1+7=17
                                    [13,9,4,10,5,7]
                                    /			\
                            13,[4,10,5,7]		9,[10,5,7]
                            /    /	   \   \	  /		\
                        4,[5,7] 10,[7]  5	7	10,[7]  5
                        /	\	/	\  	=18		/       =14
                    5,[]   7,[] 7,[] []			7,[]
                    =22		=29  =30 =20		=26
'''
def maxLoot(hval,n): 
	if (n < 0): 
		return 0
	if (n == 0): 
		return hval[0] 
	pick = hval[n] + maxLoot(hval, n - 2) 
	notPick = maxLoot(hval, n - 1) 
	return max(pick, notPick) 
hval =[3,9,4,1,5,7] #[13,9,4,10,5,7]
n = len(hval) 
print("Maximum loot possible : ",maxLoot(hval, n - 1)) 


