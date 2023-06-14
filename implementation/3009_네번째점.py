square = []
x_axis ={}
y_axis ={}
for _ in range(3):
    x, y = map(int, input().split())
    square.append((x,y))


for x1,y1 in square:
    
    x_axis [x1] = x_axis.get(x1, 0) +1
    y_axis [y1] = y_axis.get(y1, 0) +1

x4=[key for key, value in x_axis.items() if value == 1]
y4=[key for key, value in y_axis.items() if value == 1]
print(x4[0], y4[0])


