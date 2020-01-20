def find_median(list1, list2):
    final = sorted(list1 + list2)
    if len(final) % 2 == 1:
        return final[len(final) // 2]
    else:
        return (final[len(final) // 2 - 1] + final[len(final) // 2]) / 2


def ispalindrome_int(num):
    return str(num) == str(num)[::-1]


def first_occurance(haystack, needle):
    return haystack.find(needle)


def increment_last(array):
    array[-1] += 1
    return array


from collections import Counter

def single_one(ls):
    return [v for k, v in Counter(ls).items() if v == 1]

def single_one_1(ls):
    counter = {}
    for element in ls:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1
    return [v for k, v in counter.items() if v == 1]


if __name__ == '__main__':
    print(find_median([1, 3, 4, 7], [2, 5, 6, 8]))
    print(ispalindrome_int(121))
    print(first_occurance("aoaoa", "ao"))
    print(increment_last([1, 2, 3, 4]))
    print(single_one_1([1, 1, 2, 2, 3]))
