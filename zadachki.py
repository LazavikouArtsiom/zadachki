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
    array = [int(el) for el in array]
    array[-1] += 1
    return [str(el) for el in array]


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

def reverse_string_by_words(strng):
    return ' '.join(strng.split()[::-1])

#def find_major_element(array):
    #unique_el = list(set(array))
    #temp = [x for x in Counter(array).values()]
    #return unique_el[temp.index(max(temp))]

def find_major_element(array):
    return sorted(Counter(array).items(), key=lambda x: x[1])[-1][0]

def len_of_last(strng):
    return len(strng.split()[-1])

class Stack():
    
    def __init__(self):
        self.stack = []
    
    def push(self, el):
        self.stack.append(el)
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)






if __name__ == '__main__':
    #print(find_median([1, 3, 4, 7], [2, 5, 6, 8]))
    #print(ispalindrome_int(121))
    #print(first_occurance("aoaoa", "ao"))
    #print(increment_last(['1', '2', '3', '4']))
    #print(len_of_last("Hello World"))
    #print(single_one_1([1, 1, 2, 2, 3]))
    #print(reverse_string_by_words("asd asd dsa sad"))
    print(find_major_element([1,1,2,3,2,2,2,1,2,3]))
