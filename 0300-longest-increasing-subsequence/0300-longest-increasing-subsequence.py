class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 가장 긴 증가하는 수열의 길이를 출력
        # ex) [10, 9, 2, 5, 3, 7, 101, 18]
        # Can you come up with an algorithm that runs in O(nlogn)
        # D[i]는? i번째까지 증가하는 수열의 길이

        N = len(nums)
        D = [1] * N
        
        for i in range(1, N):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    D[i] = max(D[i], D[j]+1)

        return max(D)
