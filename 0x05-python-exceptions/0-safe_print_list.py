def safe_print_list(my_list=[], x=0):
	cont = 0
	try:
		for elem in range(my_list[0], my_list[x]):
			print("{}".format(elem), end='')
			cont += 1
	except IndexError:
		for i in my_list:
			print("{}".format(i), end='')
			cont += 1
	print()
	return cont
