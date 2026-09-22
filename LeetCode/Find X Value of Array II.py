from typing import List


class SegmentTree:
    def __init__(self, arr, k):
        self.n = len(arr)
        self.k = k
        self.tree = [([0] * k, 0) for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, arr)

    def make_node(self, val):
        rem = val % self.k
        cnt = [0] * self.k

        cnt[rem] = 1
        return cnt, rem

    def merge(self, left, right):
        left_cnt, left_prod = left
        right_cnt, right_prod = right

        prod = (left_prod * right_prod) % self.k
        cnt = left_cnt[:]

        for x in range(self.k):
            new_rem = (left_prod * x) % self.k
            cnt[new_rem] += right_cnt[x]

        return cnt, prod

    def build(self, idx, l, r, arr):
        if l == r:
            self.tree[idx] = self.make_node(arr[l])
            return

        mid = (l + r) >> 1

        self.build(2 * idx + 1, l, mid, arr)
        self.build(2 * idx + 2, mid + 1, r, arr)

        self.tree[idx] = self.merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, idx, l, r, start, end):
        if r < start or l > end:
            return None

        if l >= start and r <= end:
            return self.tree[idx]

        mid = (l + r) >> 1

        left = self.query(2 * idx + 1, l, mid, start, end)
        right = self.query(2 * idx + 2, mid + 1, r, start, end)

        if left is None: return right
        if right is None: return left

        return self.merge(left, right)

    def update(self, idx, l, r, u_idx, u_val):
        if l == r:
            self.tree[idx] = self.make_node(u_val)
            return

        mid = (l + r) >> 1

        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_idx, u_val)

        else:
            self.update(2 * idx + 2, mid + 1, r, u_idx, u_val)

        self.tree[idx] = self.merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])
        

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        seg = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            seg.update(0, 0, n - 1, idx, val)

            cnt, prod = seg.query(0, 0, n - 1, start, n - 1)

            ans.append(cnt[x])

        return ans