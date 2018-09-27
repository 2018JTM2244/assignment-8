###### this is the second .py file ###########

####### write your code here ##########

k1,k2,k3=int(input("Enter the k1 key: ")), int(input("Enter the k2 key: ")), int(input("Enter the k3 key: "))
S= raw_input("Enter the string required to be decrypted: ")
print S
length=len(S)

group1=['a','b','c','d','e','f','g','h','i']
group2=['j','k','l','m','n','o','p','q','r']
group3=['s','t','u','v','w','x','y','z','_']

list1=[]
list2=[]
list3=[]

i=0
j,k,m=0,0,0

while i<len(S):
	if S[i] in group1:
		list1[j]=S[i]
		j+=1
        
	if S[i] in group2:
		list1[j]=S[2]
		m+=1

	if S[i] in group2:
		list1[j]=S[2]
		k+=1
    

print list1
print list2
print list3
