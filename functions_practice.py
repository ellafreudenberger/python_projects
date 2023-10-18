def hello():
    print("Hello, user!")

# Call hello function to print greeting
hello()

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# Example
result = pack("banana", 18, [1, 2, 3])
print(result)

def eat_lunch (lunchMeal_list):
    if not lunchMeal_list:
        print("My lunchbox is empty")
    else:
        print(f"First I eat {lunchMeal_list[0]}")
        for food in lunchMeal_list[1:]:
            print(f"Next I eat {food}")

# Example
lunchbox = ["cheese pizza", "caesar salad", "chocolate chip cookie"]
eat_lunch(lunchbox)

empty_lunchbox = []
eat_lunch(empty_lunchbox)