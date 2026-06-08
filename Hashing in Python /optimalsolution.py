class Solution:
    def frequencyCount(self, arr):
        n=len(arr)
        freq_map = {}
        for i in range(0, n):
            if arr[i] in freq_map:
                freq_map[arr[i]] += 1
            else:
                freq_map[arr[i]] = 1
                
        result=[0]*n
        for i in range(1,n+1):
            if i in freq_map:
                result[i-1] = freq_map[i]
                
        return result