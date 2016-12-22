#!/usr/bin/env python3

#BubbleSort

def main():
    data = input("Enter numbers to sort separated by spaces: ")
    list = data.split(" ")
    for i in range(0, len(list)):
        list[i] = int(list[i])
    bubble_sort(list)
    print(list)

def bubble_sort(list):
    is_unsorted = True
    while is_unsorted:
        is_unsorted = False
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                is_unsorted = True

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

if __name__ == "__main__":
    main()
