# __init__ : degree 최고차항 -> 최고차항+1만큼의 방을 만듦
# get_lead_exp : 최고차항 지수 출력
# evaluate : 함수에 x 대입 후 계산
# get_coef : 계수 뽑기 ex) 20 넣으면 3
# is_zero :
# zero : 모두 0으로 리셋
# attach : (3,20) 계수, 지수 넣으면 3x^20
# remove :
# 지수는 인덱스로, 계수는 실제값으로
class Polynomial:
    def __init__(self, degree):
        self.degree = degree # 최고차항 지수 20
        self.coef = [0] * (self.degree + 1) # [0, 0, ... 0, 0]

    # 구현
    def get_lead_exp(self): # 최고차항 지수 리턴
        i = len(self.coef) - 1 # 21 - 1 = 20
        while i >= 0 and self.coef[i] == 0:
            i -= 1

        if i < 0:
            raise Exception("Failed to get_lead_exp.")
        return i

    # 구현
    def evaluate(self, x):
        return sum(coef * (x**exp) for exp, coef in enumerate(self.coef)
                   if coef != 0)

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    # 구현
    def attach(self, coef, exp):
        self.coef[exp] = coef
        return self

    def remove(self, exp):
        self.coef[exp] = 0

    # 구현
    def __str__(self):
        ret = ""
        for coef, exp in [
            (self.coef[i], i) for i in range(self.degree + 1)
            if self.coef[i] != 0
        ][::-1]:
            ret += f"({coef})x^{exp} + "
        return f"{ret}\b\b"

    # 구현
    def __add__(self, other):
        poly = Polynomial(max(self.degree, other.degree))



if __name__ == "__main__":
    poly = Polynomial(20)
    poly.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly)
    x = 3
    res = poly.evaluate(x)
    print(f"{poly} = {res}, where xi = {x}")
    print(poly.get_lead_exp())
