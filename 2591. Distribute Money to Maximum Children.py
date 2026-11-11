class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        if money > 8*children:
            return children - 1

        money -= children #everyone at least 1 dollar
        
        k = money // 7
        money %= 7
        
        if k < children and k > 0:
            if money == 3 and children-k == 1:
                k -= 1
        elif k == children and money > 0:
            k -= 1
        return k
