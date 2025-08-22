#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Competitive Programming Templates (Python)
-----------------------------------------
Drop-in snippets for rapid problem solving. Copy/paste functions as needed.
Language: Python 3.10+
Note: Keep I/O fast (use sys.stdin.buffer.readline) for large input.
"""

# ===== Fast I/O =====
import sys
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, accumulate
from math import gcd, sqrt, ceil, floor
import heapq

input = sys.stdin.readline

# ===== Utilities =====
INF = 10 ** 18
MOD = 10 ** 9 + 7

# Fast power (a^e mod m)
def mod_pow(a: int, e: int, m: int = MOD) -> int:
    a %= m
    res = 1
    while e:
        if e & 1:
            res = (res * a) % m
        a = (a * a) % m
        e >>= 1
    return res

# Modular inverse (m prime)
def mod_inv(a: int, m: int = MOD) -> int:
    return mod_pow(a, m - 2, m)

# nCr precompute (factorials mod MOD)
class Comb:
    def __init__(self, n: int, mod: int = MOD):
        self.mod = mod
        self.f = [1] * (n + 1)
        for i in range(1, n + 1):
            self.f[i] = self.f[i - 1] * i % mod
        self.invf = [1] * (n + 1)
        self.invf[n] = pow(self.f[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.invf[i - 1] = self.invf[i] * i % mod
    def nCr(self, n: int, r: int) -> int:
        if r < 0 or r > n: return 0
        return self.f[n] * self.invf[r] % self.mod * self.invf[n - r] % self.mod

# ===== Arrays / Prefix / Difference =====

def prefix_sums(arr):
    # ps[i] = sum of arr[0..i-1], ps[0] = 0
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

# Range sum [l, r] inclusive using prefix sums
# sum = ps[r+1] - ps[l]

class DifferenceArray:
    # Supports range add and finalizing to actual array
    def __init__(self, n):
        self.d = [0] * (n + 1)
    def range_add(self, l, r, val):
        self.d[l] += val
        if r + 1 < len(self.d):
            self.d[r + 1] -= val
    def finalize(self):
        cur = 0
        out = []
        for i in range(len(self.d) - 1):
            cur += self.d[i]
            out.append(cur)
        return out

# ===== Two Pointers / Sliding Window =====

def longest_subarray_sum_leq_k(arr, k):
    s = 0
    l = 0
    best = 0
    for r, v in enumerate(arr):
        s += v
        while s > k and l <= r:
            s -= arr[l]
            l += 1
        best = max(best, r - l + 1)
    return best

# ===== Binary Search / Ternary Search =====

def binary_search_first_true(lo, hi, check):
    # find smallest x in [lo, hi] with check(x) == True; assume monotonic
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# Binary search on answer example skeleton
# ans = binary_search_first_true(lo, hi, lambda x: feasible(x))

# Ternary search on unimodal real/integer domain

def ternary_search_int(lo, hi, f):
    while hi - lo > 3:
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        if f(m1) < f(m2):
            lo = m1
        else:
            hi = m2
    best_x = lo
    best_v = f(lo)
    for x in range(lo + 1, hi + 1):
        v = f(x)
        if v < best_v:
            best_v = v
            best_x = x
    return best_x, best_v

# ===== Meet-in-the-Middle (subset sums example) =====

def meet_in_middle_subset_sum(arr, target):
    n = len(arr)
    a, b = arr[: n // 2], arr[n // 2 :]
    A = [0]
    for x in a:
        A += [x + s for s in A]
    B = [0]
    for x in b:
        B += [x + s for s in B]
    B.sort()
    for s in A:
        # find if target - s in B
        i = bisect_left(B, target - s)
        if i < len(B) and B[i] == target - s:
            return True
    return False

# ===== Graphs: BFS / DFS / Topo / DSU =====

def bfs(graph, src):
    n = len(graph)
    dist = [INF] * n
    dist[src] = 0
    q = deque([src])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

sys.setrecursionlimit(1 << 25)

def dfs_recursive(graph, u, seen=None):
    if seen is None:
        seen = set()
    seen.add(u)
    for v in graph[u]:
        if v not in seen:
            dfs_recursive(graph, v, seen)
    return seen

# Topological sort (Kahn's algorithm)

def topo_sort(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order  # if len(order) < n => cycle exists

# Disjoint Set Union (Union-Find)
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
        self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True

# ===== Shortest Paths / MST =====

def dijkstra(n, adj, src):
    # adj: list of list[(v, w)]
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def bellman_ford(n, edges, src):
    # edges: list of (u, v, w)
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        any_relaxed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                any_relaxed = True
        if not any_relaxed:
            break
    # Negative cycle detection (optional)
    # for u, v, w in edges:
    #     if dist[u] + w < dist[v]:
    #         return None  # or handle
    return dist

def floyd_warshall(dist):
    # dist: n x n matrix, dist[i][i] = 0
    n = len(dist)
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == INF: continue
            for j in range(n):
                v = dik + dist[k][j]
                if v < dist[i][j]:
                    dist[i][j] = v
    return dist

# Kruskal MST

def mst_kruskal(n, edges):
    # edges: (w, u, v)
    edges.sort()
    dsu = DSU(n)
    total = 0
    used = []
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            used.append((u, v, w))
    return total, used

# Prim MST (adj as (v, w))

def mst_prim(n, adj, start=0):
    seen = [False] * n
    pq = []
    seen[start] = True
    for v, w in adj[start]:
        heapq.heappush(pq, (w, start, v))
    total = 0
    edges = []
    cnt = 1
    while pq and cnt < n:
        w, u, v = heapq.heappop(pq)
        if seen[v]:
            continue
        seen[v] = True
        total += w
        edges.append((u, v, w))
        cnt += 1
        for x, wx in adj[v]:
            if not seen[x]:
                heapq.heappush(pq, (wx, v, x))
    return total, edges

# ===== Max Flow (Dinic) =====
class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
    def add_edge(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u])])
    def bfs(self, s, t, lvl):
        for i in range(self.n):
            lvl[i] = -1
        q = deque([s])
        lvl[s] = 0
        while q:
            u = q.popleft()
            for v, c, _ in self.g[u]:
                if c > 0 and lvl[v] < 0:
                    lvl[v] = lvl[u] + 1
                    q.append(v)
        return lvl[t] >= 0
    def dfs(self, u, t, f, it, lvl):
        if u == t:
            return f
        i = it[u]
        while i < len(self.g[u]):
            it[u] = i
            v, c, rev = self.g[u][i]
            if c > 0 and lvl[u] + 1 == lvl[v]:
                pushed = self.dfs(v, t, min(f, c), it, lvl)
                if pushed:
                    self.g[u][i][1] -= pushed
                    self.g[v][rev][1] += pushed
                    return pushed
            i += 1
        return 0
    def maxflow(self, s, t):
        flow = 0
        lvl = [-1] * self.n
        while self.bfs(s, t, lvl):
            it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF, it, lvl)
                if not pushed:
                    break
                flow += pushed
        return flow

# ===== Dynamic Programming =====

# 0/1 Knapsack (weight W)
def knapsack_01(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for cap in range(W, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[W]

# Unbounded Knapsack
def knapsack_unbounded(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        w, v = weights[i], values[i]
        for cap in range(w, W + 1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[W]

# LIS O(n log n)

def LIS_length(arr):
    tails = []
    for x in arr:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

# LCS length (O(n*m))

def LCS_length(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            cur = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = cur
    return dp[m]

# Edit Distance (Levenshtein)

def edit_distance(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        ndp = [i] + [0] * m
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                ndp[j] = dp[j - 1]
            else:
                ndp[j] = 1 + min(dp[j], ndp[j - 1], dp[j - 1])
        dp = ndp
    return dp[m]

# Grid DP: min path sum

def min_path_sum(grid):
    n, m = len(grid), len(grid[0])
    dp = [INF] * (m + 1)
    dp[1] = 0
    for i in range(n):
        ndp = [INF] * (m + 1)
        for j in range(1, m + 1):
            ndp[j] = grid[i][j - 1] + min(dp[j], ndp[j - 1])
        dp = ndp
    return dp[m]

# Bitmask DP (TSP skeleton)

def tsp_dp(dist):
    n = len(dist)
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            cur = dp[mask][u]
            if cur >= INF: continue
            nxt_mask = mask
            for v in range(n):
                if mask & (1 << v):
                    continue
                nm = mask | (1 << v)
                dp[nm][v] = min(dp[nm][v], cur + dist[u][v])
    ans = INF
    for u in range(n):
        ans = min(ans, dp[(1 << n) - 1][u] + dist[u][0])
    return ans

# Digit DP skeleton: count numbers in [0..N] satisfying property
# Define states: pos, tight, sum/parity/etc. Memoize.
from functools import lru_cache

def digit_dp_count(N: int):
    s = str(N)
    @lru_cache(maxsize=None)
    def dp(i, tight, parity):
        if i == len(s):
            return 1 if parity == 0 else 0
        limit = int(s[i]) if tight else 9
        total = 0
        for d in range(0, limit + 1):
            total += dp(i + 1, tight and d == limit, parity ^ (d & 1))
        return total
    return dp(0, True, 0)

# DP on DAG (count paths)

def count_paths_DAG(n, edges, src, dst):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    order = topo_sort(n, edges)
    ways = [0] * n
    ways[src] = 1
    for u in order:
        for v in g[u]:
            ways[v] = (ways[v] + ways[u]) % MOD
    return ways[dst]

# Tree DP example: subtree sizes and rerooting skeleton

def tree_dp_subtree_sizes(n, adj):
    sz = [1] * n
    parent = [-1] * n
    def dfs(u, p):
        parent[u] = p
        for v in adj[u]:
            if v == p: continue
            dfs(v, u)
            sz[u] += sz[v]
    dfs(0, -1)
    return sz, parent

# ===== Data Structures =====

# Fenwick Tree (BIT) 1-indexed
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx
    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

# Segment Tree (iterative) for range min
class SegTreeMin:
    def __init__(self, arr):
        n = 1
        while n < len(arr):
            n <<= 1
        self.N = n
        self.t = [INF] * (2 * n)
        for i, v in enumerate(arr):
            self.t[n + i] = v
        for i in range(n - 1, 0, -1):
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])
    def update(self, idx, val):
        i = self.N + idx
        self.t[i] = val
        i //= 2
        while i:
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])
            i //= 2
    def query(self, l, r):
        # inclusive l, exclusive r
        l += self.N; r += self.N
        res = INF
        while l < r:
            if l & 1:
                res = min(res, self.t[l]); l += 1
            if r & 1:
                r -= 1; res = min(res, self.t[r])
            l //= 2; r //= 2
        return res

# Sparse Table for idempotent ops (e.g., min/max/gcd)
class SparseTable:
    def __init__(self, arr, op=min):
        self.op = op
        self.n = len(arr)
        self.K = (self.n).bit_length()
        self.st = [arr[:]]
        k = 1
        while (1 << k) <= self.n:
            prev = self.st[-1]
            cur = []
            for i in range(self.n - (1 << k) + 1):
                cur.append(op(prev[i], prev[i + (1 << (k - 1))]))
            self.st.append(cur)
            k += 1
    def query(self, l, r):
        # inclusive l, exclusive r
        k = (r - l).bit_length() - 1
        return self.op(self.st[k][l], self.st[k][r - (1 << k)])

# ===== Strings =====

# KMP prefix function

def prefix_function(s: str):
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

# Z-function

def z_function(s: str):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# Rolling hash (double optional)
class RollingHash:
    def __init__(self, s: str, base=911382323, mod=972663749):
        n = len(s)
        self.mod = mod
        self.base = base
        self.pw = [1] * (n + 1)
        self.h = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            self.pw[i] = (self.pw[i - 1] * base) % mod
            self.h[i] = (self.h[i - 1] * base + ord(ch)) % mod
    def get(self, l, r):
        # substring s[l:r] (0-indexed, r exclusive)
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

# ===== LCA / Binary Lifting =====
class LCA:
    def __init__(self, n, adj, root=0):
        self.LOG = (n).bit_length()
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        def dfs(u, p):
            self.up[0][u] = p
            for v in adj[u]:
                if v == p: continue
                self.depth[v] = self.depth[u] + 1
                dfs(v, u)
        dfs(root, -1)
        for k in range(1, self.LOG):
            for v in range(n):
                if self.up[k - 1][v] != -1:
                    self.up[k][v] = self.up[k - 1][self.up[k - 1][v]]
    def lift(self, v, k):
        i = 0
        while k:
            if k & 1:
                v = self.up[i][v]
            if v == -1: break
            k >>= 1
            i += 1
        return v
    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        a = self.lift(a, self.depth[a] - self.depth[b])
        if a == b: return a
        for k in range(self.LOG - 1, -1, -1):
            if self.up[k][a] != self.up[k][b]:
                a = self.up[k][a]
                b = self.up[k][b]
        return self.up[0][a]

# ===== Number Theory =====

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start:n + 1:step] = [False] * (((n - start) // step) + 1)
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return is_prime, primes

# Factorization using smallest prime factor (SPF)
class SPF:
    def __init__(self, n):
        self.spf = list(range(n + 1))
        for i in range(2, int(n ** 0.5) + 1):
            if self.spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i
    def factor(self, x):
        f = Counter()
        while x > 1:
            p = self.spf[x]
            f[p] += 1
            x //= p
        return f

# Extended GCD, CRT (basic)

def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    y, x, g = egcd(b, a % b)
    y -= (a // b) * x
    return (x, y, g)

# Chinese Remainder Theorem for pair (a ≡ r1 mod m1, a ≡ r2 mod m2)

def crt_pair(r1, m1, r2, m2):
    x1, y1, g = egcd(m1, m2)
    if (r2 - r1) % g != 0:
        return (0, -1)  # no solution
    lcm = m1 // g * m2
    t = ((r2 - r1) // g * x1) % (m2 // g)
    r = (r1 + t * m1) % lcm
    return (r, lcm)

# ===== Geometry =====

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

# Convex Hull (Monotone Chain)

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    def build(seq):
        hull = []
        for p in seq:
            while len(hull) >= 2:
                x1, y1 = hull[-2]
                x2, y2 = hull[-1]
                x3, y3 = p
                if cross(x2 - x1, y2 - y1, x3 - x2, y3 - y2) <= 0:
                    hull.pop()
                else:
                    break
            hull.append(p)
        return hull
    lower = build(points)
    upper = build(reversed(points))
    return lower[:-1] + upper[:-1]

# Line Sweep (interval union length)

def union_length(segments):
    events = []
    for l, r in segments:
        events.append((l, 1))
        events.append((r, -1))
    events.sort()
    active = 0
    prev = None
    total = 0
    for x, t in events:
        if active > 0 and prev is not None:
            total += x - prev
        active += t
        prev = x
    return total

# ===== Bit Tricks =====

def iter_submasks(mask):
    s = mask
    while s:
        yield s
        s = (s - 1) & mask

# Count bits (popcount)

def popcount(x):
    return x.bit_count()

# ===== Boilerplate for multiple testcases =====

def main():
    t = int(input())
    for _ in range(t):
        # solve()  # implement per problem
        pass

if __name__ == "__main__":
    # main()
    pass
