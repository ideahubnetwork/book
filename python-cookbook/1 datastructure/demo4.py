import heapq

nums = [8, 7, 6, 5, 4, 3, 2, 1]
heapq.heapify(nums)
print(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(nums)
print(heapq.nsmallest(3, nums, key=lambda x: x))
