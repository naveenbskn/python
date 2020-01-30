pos = {
	"x": 0, 
	"y": 0
}

while True:

	line =input()
	if not line:
		break

	direction, steps = line.split()
	if direction == "UP":
		pos["y"] += int(steps)
	elif direction == "DOWN":
		pos["y"] -= int(steps)
	elif direction == "LEFT":
		pos["x"] -= int(steps)
	elif direction == "RIGHT":
		pos["x"] += int(steps)
print(pos)
print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)))
