
def table(n,m):
	"""Prints multiplication table of n"""
	for i in range(m+1):
		print(f"{n}X{i+1}={n*(i+1)}")

table(10,10)