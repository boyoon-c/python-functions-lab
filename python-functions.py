'''
1
'''

def sum_to(n):
    sum = 0
    for i in range(1, n+1, 1):
        sum+=i
    return sum

print(sum_to(10))

'''
2
'''

def largest(num_list):
    max = 0
    for i in num_list:
        if i > max:
            max = i
    return max

print(largest([10, 4, 2, 231, 91, 54]))

'''
3
'''

def occurrences(sent, char):
    count=0
    char_len=len(char)
    sent_len=len(sent)
    for i in range(sent_len):
        if (sent[i:i+char_len]==char):
            count+=1
    return count

print(occurrences('fleep floop', 'fl'))


'''
4
'''

def product(num1, num2, *args):
    res=num1*num2
    for arg in args:
        print(arg)
        res*=arg
    return res

print(product(4, 0.5, 5))