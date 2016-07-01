# coding: utf8

def chercher_pivot(A,n,k):
	while ((A[k][k]==0) and (k<n)):
		k+=1
	if (k==n):
		return -1
	else:
		return k

def permuter_ligne(A, n, A1, b, k, i):
	for j in range(n):
		ech=A[i][j]
		A[i][j]=A[k][j]
		A[k][j]=ech
		ech=A1[i][j]
		A1[i][j]=A1[k][j]
		A1[k][j]=ech
	ech=b[i]
	b[i]=b[k]
	b[k]=ech

def elimination(A,n,A1,b,k):
	for i in range(k+1,n):
		r=A[i][k]/A[k][k]
		for j in range(n):
			A[i][j]-=r*A[k][j]
			A1[i][j]-=r*A1[k][j]
		b[i]-=r*b[k]


def remontee(A,n,A1,b):
	x=[0 for i in range(0,n)]
	x[n-1]=b[n-1]/A[n-1][n-1]
	for j in range(n):
		A1[n-1][j]/=A[n-1][n-1]
	for i in range(n-2,-1,-1):
		x[i]=b[i]
		for j in range(i+1,n):
			x[i]-=A[i][j]*x[j]
			for k in range(n):
				A1[i][k]-=A[i][j]*A1[j][k]
		x[i]/=A[i][i]
		for j in range(n):
			A1[i][j]/=A[i][i]
	return x

def saisie(A,n,b):
	print("Donnez A :")
	for i in range(n):
		for j in range(n):
			A[i][j]=float(input())
		print()
	print("Donnez les coordonnés de b :")
	for i in range(n):
		b[i]=float(input())

def init_inverse(n):
	A=[[0 for j in range(0,n)] for i in range(0,n)]
	for i in range(n):
		A[i][i]=1
	return A


n=int(input("Donnez n : "))
A=[[0 for j in range(0,n)] for i in range(0,n)]
b=[0 for i in range(0,n)]
saisie(A,n,b)
A1=init_inverse(n)

k=0
drapeau=0
while ((drapeau==0) and k!=n):
	i=chercher_pivot(A,n,k)
	if (i!=-1):
		if (i!=k):
			permuter_ligne(A,n,A1,b,k,i)
		elimination(A,n,A1,b,k)
		k+=1
	else:
		drapeau=1
if(k==n and A[k-1][k-1]!=0):
	x=remontee(A,n,A1,b)
	print("La solution de ce système lineaire est : ")
	print(x)
	print("L'inverse de la matrice donne :")
	print(A1)
else:
	print("Pas de solution unique !")

input("Appuyez sur ENTREE pour continuer...")