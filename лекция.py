def f(n):
	#n=int(input())
	if n==0 or n==1:
		return 1
	return f(n-1)+f(n-2)
print (f(35))
