def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Abdulla", power = "Lazer")
print_kwargs(name = "Abdulla")
print_kwargs(name = "Abdulla", power = "Lazer", enemy = "Dr.Jackaal")