class Solution:
    def change2(self, amount: int, coins: List[int]) -> int:
        result = []

        def dfs(i, path):
            if i == len(coins):
                if sum(path) == amount:
                    result.append(path[:])
                return
            
            if sum(path) > amount:
                return

            path.append(coins[i])
            dfs(i, path)
            path.pop()

            dfs(i + 1, path)
                
        dfs(0, [])
        print(result)
        return len(result)

    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, curr_sum):
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            if i == len(coins):
                if curr_sum == amount:
                    return 1
                return 0
            
            if curr_sum > amount:
                return 0

            a = dfs(i, curr_sum + coins[i])
            b = dfs(i + 1, curr_sum)

            dp[(i, curr_sum)] = a + b

            return a + b
                
        return dfs(0, 0)
        print(res)
        