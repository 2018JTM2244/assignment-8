###### this is the first .py file ###########

####### write your code here ##########

def main():
	n,m=int(input("Enter the integer n: ")), int(input("Enter the integer m: "))
	if not (n>1 and n<=105):
		return
	if not (m>1 and m<=105):
		return


	l= []
	listofmin=[]
	for x in range(n):
		s= list(input())
		l=l+[s]
	print(l)

	i=0 ; j=0
#	a='S'|'D'
	countr,countl,countd,countu=0,0,0,0
	for a in l[i][j]:
		for a in  l[i][j]:
			while l[i][j]=='S':
				countr+=1
				if j==m-1:
					break
				j+=1
			j=j-countr
			while l[i][j]=='S':
				countl+=1
				if j==-1:
					break
				j-=1
			j=j+countl
			while l[i][j]=='S':
				countu+=1
				if i==-1:
					break
				i-=1
			i=i+countu
			while l[i][j]=='S':
				countd+=1
				if i==n-1:
					break
			i=i-countd
			j+=1		
		i+=1
		listofmin=listofmin+[min(countr,countl,countd,countu)]
		print(listofmin)
		if i==n-1:
			break


	max_value=max(listofmin)
	if max_value>1:
		print(max_value+" "+max_value)
	else:
		temp = max_value
		listofmin.remove(max_value)
		max_value=max(listofmin)
		print(temp+" "+max_value)




#		for S in l[i][j]
#			i-=1
#			while l[i]==S
#				countl+=1
#		i=i+countl			
#		while l[i][j-1]
#			while l[i-=1][j]
#
#	import re
#
#	for S in l
#
#	maxpattern = 0
#	if (m>)
#
# i=0
# count=0
# while i<n
# 	for S in list[i][:1]
# 		if count==1
# 			break
# 		count+=1
# 	for S in list[i][1:2]
# 		for S in list[i+1][:j]
		

if __name__ == '__main__':
	main()