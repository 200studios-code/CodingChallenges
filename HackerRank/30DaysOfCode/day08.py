# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input().strip())
    phoneBook = {}
    for _ in range(n):
        name, number = input().split()
        phoneBook[name] = number
    q = ''
    while True:
        try:
            q = input().strip()
        except EOFError:
            break
        if q not in phoneBook:
            print('Not found')
        else:
            print(f'{q}={phoneBook.get(q)}')
