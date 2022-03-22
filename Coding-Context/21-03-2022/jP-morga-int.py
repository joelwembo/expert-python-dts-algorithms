# JP Morgan Inteview

# Smallest suficient Substring

class Solution:
    def solve(self, S, T):
      INF = float("inf")
      N = len(S)
      dp = [INF] * N
      for i in range(N):
         if S[i] == T[0]:
            dp[i] = 1
      for j in range(1, len(T)):
         last = {}
         dp2 = [INF] * N
         for i in range(N):
            if S[i] == T[j]:
               prev_i = last.get(T[j − 1], None)
               if prev_i is not None:
                  dp2[i] = dp[prev_i] + (i − prev_i)
            last[S[i]] = i
         dp = dp2
      m = min(dp)
      i = dp.index(m)
      if m == INF:
         return ""
      return S[i − dp[i] + 1 : i + 1]
ob = Solution()
print(ob.solve("abcbfbghfb","fg"))