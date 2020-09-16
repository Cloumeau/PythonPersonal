#find greatest common divisor of two integers

def RecGCD(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return RecGCD(low, high%low)
print(RecGCD(22,20))