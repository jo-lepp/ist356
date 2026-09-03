#when you write a function:

#First, write program
# input
# numbers = [2, 3, 5, 10]

# # process
# total = sum(numbers) # 20
# count = len(numbers) # 4
# avg = total / count # 5.0

# # output
# print(avg)

#Second, rewrite program into function
def average(numbers: list[float]) -> float:
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

numbers = [5,6]
grades = [100, 100, 0, 100]
avg_grade = average(grades)
print(f"Average of {grades} is {avg_grade}") # 75.0

def test_avg():
    numbers = [1,1,1,1]
    expect = 1.0
    actual = average(numbers)
    assert expect == actual

test_avg()
