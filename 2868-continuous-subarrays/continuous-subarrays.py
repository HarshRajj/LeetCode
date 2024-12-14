

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        max_deque = deque()
        min_deque = deque()
        start = 0
        count = 0

        for end in range(n):
            
            while max_deque and nums[max_deque[-1]] <= nums[end]:
                max_deque.pop()
            max_deque.append(end)

            
            while min_deque and nums[min_deque[-1]] >= nums[end]:
                min_deque.pop()
            min_deque.append(end)

            
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                start += 1
                if max_deque[0] < start:
                    max_deque.popleft()
                if min_deque[0] < start:
                    min_deque.popleft()

            
            count += (end - start + 1)

        return count
