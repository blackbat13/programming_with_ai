import random

# Bubble sort
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

if __name__ == "__main__":
    # Generate list of random numbers
    lst = [int(1000 * random.random()) for i in range(10)]
    print(lst)
    print(bubble_sort(lst))