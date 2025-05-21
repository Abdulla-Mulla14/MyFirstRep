distance = 10

if distance < 3:
    mode = "walk"
elif distance <= 15:
    mode = "bike"
else:
    mode = "car"

print(mode)
