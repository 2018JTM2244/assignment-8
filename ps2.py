###### this is the second .py file ###########

####### write your code here ##########
#Main function
def main():
	#key inputs
	k1,k2,k3=int(input("Enter the k1 key: ")), int(input("Enter the k2 key: ")), int(input("Enter the k3 key: "))
	if not (k1>0 and k1<=150):
		return
	if not (k2>0 and k2<=150):
		return
	if not (k3>0 and k3<=150):
		return

	#String input
	S= input("Enter the string required to be decrypted: ")
	print(S)
	length=len(S)

	if len(S)>150:
		exit()

	#groups given in the question
	group1=['a','b','c','d','e','f','g','h','i']
	group2=['j','k','l','m','n','o','p','q','r']
	group3=['s','t','u','v','w','x','y','z','_']

	list1=[]
	list2=[]
	list3=[]
	reqlist=[]

	i=0
	j,k,m=0,0,0

	#loop for separing the string into lsits according to groups defined
	while i<len(S):
		if S[i] in group1:
			list1=list1+[S[i]]
			j+=1
	        
		if S[i] in group2:
			list2=list2+[S[i]]
			k+=1

		if S[i] in group3:
			list3=list3+[S[i]]
			m+=1

		i+=1

	#function definition for rotation of elements in the grouped lists
	def rightRotate(l, n):
	    return l[-n:] + l[:-n]


	list1 = rightRotate(list1,k1)
	list2 = rightRotate(list2,k2)
	list3 = rightRotate(list3,k3)

	i,j,k,m=i-i,j-j,k-k,m-m

	#loop for converting enrypted message into decrypted one
	while i<len(S):
		if S[i] in group1:
			reqlist=reqlist+[list1[j]]
			j+=1
	        
		if S[i] in group2:
			reqlist=reqlist+[list2[k]]
			k+=1

		if S[i] in group3:
			reqlist=reqlist+[list3[m]]
			m+=1

		i+=1

	s= ''.join(reqlist) 
	print(s)

if __name__ == '__main__':
	main()
#import numpy
#numpy.roll(list1,k1)
#numpy.roll(list2,k2)
#numpy.roll(list3,k3)

#import collections
#list1.rotate(k1)
#list2.rotate(k2)
#list3.rotate(k3)

#function for rotating the list elements
#def rotate(list,x):
#	x=x%len(list)
#	return list[x:] + list[:x]

# Returns the rotated list 
# def rightRotate(lists,num): 
#     output_list = [] 
#     # Will add values from n to the new list 
#     for item in range(len(lists) - num, len(lists)): 
#         output_list.append(lists[item])   
#     # Will add the values before 
#     # n to the end of new list     
#     for item in range(0, len(lists) - num):  
#         output_list.append(lists[item])     
#     return output_list 

#function for rotating the list elements
