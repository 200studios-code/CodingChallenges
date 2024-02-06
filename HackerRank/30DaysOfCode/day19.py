
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        div_sum = 0
        for idx in range(1, n+1):
            if n % idx == 0:
                div_sum += idx
        return div_sum
