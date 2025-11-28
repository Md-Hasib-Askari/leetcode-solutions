import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    n, q = map(int, input().split())
    s = list(input().strip())
    print(n, q, s)

    for _ in range(q):
        cx, cv, ci = map(int, input().split())
        print(cx, cv, ci)
        s_copy = s[:]

        for i in range(n):
            if s_copy[i] == '?' and ci > 0 and i+1 < n and s_copy[i+1] != 'I':
                s_copy[i] = 'I'
                ci -= 1
        
        for i in range(n):
            if s_copy[i] == '?' and ci > 0 and i+1 < n and s_copy[i+1] == '?':
                s_copy[i] = 'I'
                ci -= 1

        result = 0
        for i, ch in enumerate(s_copy):
            if i+1 < n and s_copy[i] == 'I' and s_copy[i+1] in "VX":
                result += -1
            elif ch == 'I':
                result += 1
            elif ch == 'V':
                result += 5
            elif ch == 'X':
                result += 10

        # decide V or I
        qs = [i for i in range(n) if s_copy[i] == '?']
        dp = {}
        def dfs(index, cv, ci, cx):
            if index == n:
                return 0
            
            if (index, cv, ci, cx) in dp:
                return dp[(index, cv, ci, cx)]
            
            if cv == 0 and ci == 0 and cx == 0:
                return 0
            
            if s_copy[index] != '?':
                res = dfs(index+1, cv, ci, cx)
                dp[(index, cv, ci, cx)] = res
                return res


        for i in range(n):
            if s_copy[i] == '?' and cv > 0 and i-1 >= 0 and s_copy[i-1] == 'I':
                s_copy[i] = 'V'
                cv -= 1

        for i in range(n):
            if s_copy[i] == '?' and ci > 0:
                s_copy[i] = 'I'
                ci -= 1

        
        for i in range(n):
            if s_copy[i] == '?' and cv > 0:
                s_copy[i] = 'V'
                cv -= 1

        for i in range(n):
            if s_copy[i] == '?' and cx > 0:
                s_copy[i] = 'X'
                cx -= 1

        output(f"{result}\n")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        print("-" * 20)


'''
? ? I V ? V X I V ?
0 0 4
1 1 -1 5 -1 5 10 -1 5 1 -> 25

4 4 0
5 5 -1 5 5 5 10 -1 5 5 -> 43

1 0 0
-1 V -1 V -1 V X -1 V X -> 36

1 1 0
I I -I V -I V X -I V V -> 

1 1 3
I ? I V I V X I V ?


? V ? ? ? ? I V V

9 2 4
-I V -I V I I -I V V -> 19
'''