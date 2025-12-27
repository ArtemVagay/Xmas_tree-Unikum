import random
n = 0
while True:
	n = int(input("Введите размер для сигмента ёлки(рекоменд. 20) больше 3: "))
	if n > 3:
		break
c = 0
c = int(input("Введите кол-во сегментов ёлки(рекоменд. 5) больше 2: "))
xmas_balls = ["🟧", "🟥", "🟪"]
for a in range(1, c + 1):
	matrix = [[" " for i in range(n // 3 + a -1)] 		for j in range(n//4 + a -1)]

	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			if x == len(matrix[y]) // 2 + y:
				matrix[y][x] = "🟩"
			elif x  == len(matrix[y]) // 2 - y:
				matrix[y][x] = "🟩"
			elif x < len(matrix[y]) // 2 + y and 	x > len(matrix[y]) // 2 - y:
				matrix[y][x] = "🟩"
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			if matrix[y][x] == "🟩":
				rnd = random.randint(0,26)
				if rnd == 26:
					matrix[y][x] = xmas_balls[random.randint(0, len(xmas_balls) - 1)]
	row_count = 0
	for row in matrix:
		row_count += 1
		if row_count >= a:
			print(" " * (c-a), end="")
			for element in row:
				print(element, end="")
			print("")

matrix = [["🟫" for i in range(n // 4)] 		for j in range(n//3)]
for row in matrix:
	print(" " * (n//3 - c//2 + 1), end="")
	for element in row:
		print(element, end="")
	print()