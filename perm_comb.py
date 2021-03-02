import sys

# method that calculates factorials
def factorial(input):
    if type(input) != int:
        return 'Can only accept integer inputs'
    if input < 0:
        return 'Invalid input. Must be a value greater than 0'
    if input == 0 or input == 1:
        return 1
    return input * factorial(input - 1)

# smart factorial that doesn't perform the full operation and saves time
def fact_with_div(n, mid, k):
    result = 1
    if mid > k:
        while n != mid:
            result *= n
            n -= 1
    else:
        while n != k:
            result *= n
            n -= 1
    return result

# method that performs the combination formula
def combination(n, k):
    numerator = fact_with_div(n, n - k, k)
    denominator = factorial(k) if k < n - k else factorial(n - k)
    return int(numerator / denominator)
# method that performs the permutation formula
def permutation(n, k):
    numerator = fact_with_div(n, n - k, 0)
    return numerator


def main():
    # options for operations and matching code
    options = {'Combinations':'(C)','C':'(C)', 'Permutations':'(P)','P':'(P)',
            'Ordered with Replacement':'(OR)', 'OR':'(OR)'}
    
    # reading input for operation type until correct
    operation_choice = input('Please choose an operation: ')
    while operation_choice not in options:
        print('That is an invalid option. Please select one of the following options:')
        for key in options:
            print(f'>> {key}')
        operation_choice = input('Please choose an operation: ')
    operation = options[operation_choice]

    # reading n and k values until correct
    n = int(input('Number of elements to pick from (n): '))
    k = int(input('Number of spaces to fit to (k): '))
    while k > n or k < 0 or n < 0:
        print('Both values have to be in the range 0 \u2264 k \u2264 n.' + 
                f'\nYour values are k = {k} and n = {n}')
        n = int(input('Number of elements to pick from: '))
        k = int(input('Number of spaces to fit to: '))

    # operation choosing
    if operation == '(C)':
        result = combination(n, k)
    elif operation == '(P)':
        result = permutation(n, k)
    else:
        result = n ** k
    print(f'Result: {result}')
    

if __name__ == '__main__':
    main()