
# # # # # # # # # # # # # # # # # # # # # # # #
#   Day 6: Let's Review                       #
# # # # # # # # # # # # # # # # # # # # # # # #

def solve(s):
    even = ''
    odd = ''
    for idx in range(len(s)):
        if idx % 2 == 1:
            odd += s[idx]
        else:
            even += s[idx]
    print(f'{even} {odd}')

if __name__ == '__main__':
    test_cases = int(input().strip())
    for idx in range(test_cases):
        solve(input().strip())


