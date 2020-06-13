lis = [[int(a) for a in input().split()] for i in range(9)]

def isPlaceAble(x, y, n):
	for i in range(9):
		if lis[x][i] == n:
			return False

			
	for i in range(9):
		if lis[i][y] == n:
			return False


	# xs = -1
	# xe = -1
	# ys = -1
	# ye = -1
	
	# if x > -1 and x < 3:
	# 	xs = 0
	# 	xe = 3
	# elif x > 2 and x < 6:
	# 	xs = 3
	# 	xe = 6
	# elif x > 5 and x < 9:
	# 	xs = 6
	# 	xe = 9

	# if y > -1 and y < 3:
	# 	ys = 0
	# 	ye = 3
	# elif y > 2 and y < 6:
	# 	ys = 3
	# 	ye = 6
	# elif y > 5 and y < 9:
	# 	ys = 6
	# 	ye = 9

	# for i in range(xs, xe):
	# 	for j in range(ys, ye):
	# 		if lis[i][j] == n:
	# 			return False


	x = x//3
	y = y//3
	for i in range(x*3, x*3+3):
		for j in range(y*3, y*3+3):
			if lis[i][j] == n:
				return False
			

	return True


def countZero():
	zcount = 0
	for i in lis:
		for j in i:
			if j == 0:
				zcount += 1


	return zcount


def sudoku_solve(x, y, a):
	if a == 0:
		printLis()


	for x in range(9):
		for y in range(9):
			if lis[x][y] == 0:
				for z in range(1, 10):
					if isPlaceAble(x, y, z):
						lis[x][y] = z
						sudoku_solve(x, y, a-1)
						lis[x][y] = 0


			if lis[x][y] == 0:
				return
				


def printLis():
	for i in range(9):
		for j in range(9):
			print(lis[i][j], end=' ')
			if(j == 2 or j == 5):
				print('|', end=' ')


		print()
		if(i == 2 or i == 5):
			for k in range(21):
				if k == 6 or k == 14:
					print('+', end='')
				else:
					print('-', end='')


			print()


sudoku_solve(0, 0, countZero())