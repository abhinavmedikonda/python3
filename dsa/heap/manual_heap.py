class Solution:
    def __init__(self, nums: list[int]):
        self.mnhp = nums
        for i in range((len(nums)-1)//2, -1, -1):
            self.heapify_down(i)
    def heapify_down(self, i):
        l = (i*2)+1
        r = (i*2)+2
        mn = i
        if l < len(self.mnhp) and self.mnhp[l] < self.mnhp[mn]:
            mn = l
        if r < len(self.mnhp) and self.mnhp[r] < self.mnhp[mn]:
            mn = r
        if mn != i:
            self.swap(i, mn)
            self.heapify_down(mn)
    def heapify_up(self, i):
        if i != 0:
            p = (i-1)//2
            if self.mnhp[i] < self.mnhp[p]:
                self.swap(i, p)
                self.heapify_up(p)
    def get_min(self):
        return self.mnhp[0] if self.mnhp else None
    def add_numbers(self, lst):
        for n in lst:
            self.mnhp.append(n)
            self.heapify_up(len(self.mnhp)-1)
        return self.mnhp[0] if self.mnhp else None
    def remove_min(self):
        if not self.mnhp:
            return None
        outp = self.mnhp[0]
        self.mnhp[0] = self.mnhp[-1]
        self.mnhp.pop()
        self.heapify_down(0)
        return outp
    def swap(self, a, b):
        temp = self.mnhp[a]
        self.mnhp[a] = self.mnhp[b]
        self.mnhp[b] = temp

if __name__ == '__main__':
    inp = [int(n) for n in input('enter numbers to initiate heap: ').strip().split()]
    o = Solution(inp)
    print(f'\nmin: {o.get_min()}')
    while True:
        print(f'''\n1. add numbers:\n2. get min\n3. remove min''')
        match input('Enter choice: '):
            case '1':
                inp = [int(n) for n in input('numbers: ').strip().split()]
                print(f'\nmin: {o.add_numbers(inp)}')
            case '2':
                print(f'\n{o.get_min()}')
            case '3':
                print(f'\n{o.remove_min()}')
