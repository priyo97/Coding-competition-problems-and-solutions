def main():

	t = int(input())

	while t:

		chef = True

		p1, p2, k = [int(x) for x in input().split()]

		n = (p1 + p2) // k

		i = 0

		while i < n:

			chef = not chef

			i += 1

		if chef:

			print("CHEF")
		
		else:

			print("COOK")

		t -= 1

main()