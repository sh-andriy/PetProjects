a = [454, 54, 1, 0, 0, 545, 3, 13, 15, 78, 100, 22, 13]
#      0   1  2   3  4  5   6  7    8  9    10  11  12


def bubble_sort(unsorted_list: list) -> list:
    n = len(unsorted_list)

    for i in range(n - 1):
        flag = 0

        for j in range(n - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                c = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = c
                flag = 1

        if flag == 0:
            break

    return unsorted_list


custom_sort = bubble_sort(a.copy())
python_sort = sorted(a)

print(custom_sort, python_sort)

assert custom_sort == python_sort

