
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Anna", age=22)
# name: Anna
# age: 22