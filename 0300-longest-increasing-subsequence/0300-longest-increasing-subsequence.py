class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 가장 긴 증가하는 수열의 길이를 출력
        # ex) [10, 9, 2, 5, 3, 7, 101, 18]
        # Can you come up with an algorithm that runs in O(nlogn)
        # D[i]는? i번째까지 증가하는 수열의 길이

        lis = [nums[0]]
        for num in nums:
            # 현재요소가 마지막 요소보다 큰 경우 추가 
            if num > lis[-1]:
                lis.append(num)
            else:
                l, r = 0, len(lis) - 1
                while l < r:
                    mid = (l + r) // 2
                    # 이진탐색을 통한 값
                    if lis[mid] < num:
                        l = mid + 1
                    else:
                        r = mid
                lis[l] = num
                
        return len(lis)
        
      