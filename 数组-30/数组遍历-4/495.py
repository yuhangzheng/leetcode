class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalTime = 0
        n = len(timeSeries)
        if n == 0:
            return 0
        else: 
            for i in range(n - 1):
                totalTime += min(timeSeries[i + 1] - timeSeries[i], duration)
            return totalTime + duration 