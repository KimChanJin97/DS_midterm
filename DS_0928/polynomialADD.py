class Polynomial2:
    """Polynomial using array."""
    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    def __str__(self):
        ret = ""
        for coef, exp in [
            (self.coef[i], i) for i in range(self.degree + 1) if self.coef[i] != 0
        ][
            ::-1
        ]:
            ret += f"({coef})x^{exp} + "

        return f"{ret}\b\b"

    def __add__(self, other):
        poly = Polynomial2(max(self.degree, other.degree))

        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()

            if exp_01 > exp_02:
                poly.attach(self.get_coef(exp_01), exp_01)
                self.remove(exp_01)
            elif exp_01 < exp_02:
                poly.attach(other.get_coef(exp_02), exp_02)
                other.remove(exp_02)
            else:
                coef = self.get_coef(exp_01) + other.get_coef(exp_02)
                exp = exp_01
                poly.attach(coef, exp)

                self.remove(exp_01)
                other.remove(exp_02)

        return poly

    def attach(self, coef, exp):
        self.coef[exp] = coef
        return self

    def get_lead_exp(self):
        i = len(self.coef) - 1
        while i >= 0 and self.coef[i] == 0:
            i -= 1

        if i < 0:
            raise Exception("Failed to get_lead_exp.")
        return i

    def evaluate(self, x):
        return sum(
            (coef * (x**exp) for exp, coef in enumerate(self.coef) if coef != 0)
        )

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)
        # any : 값이 뭐라도 있는지 판단하는 함수

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    def remove(self, exp):
        self.coef[exp] = 0

    '''
    elif문은 if문 반대로 하면 된다.
    마지막 else는 같은 경우 동일한 지수에 계수를 가지고 있으면 그놈은 항의 덧셈으로 더하면 된다. 하지만 지수의 위치는 그대로 이다.
    같은 놈을 소화했으니까 둘다 remove해줘야 한다 그래야 최고차항을 뽑을때 영향을 주지 않는다.
    '''

if __name__ == '__main__':

    poly1 = Polynomial2(20)
    poly1.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly1)

    poly2 = Polynomial2(4)
    poly2.attach(1, 4).attach(10, 3).attach(3, 2).attach(1, 0)
    print(poly2)

    poly = poly1 + poly2
    print('poly1 + poly2 = ')
    print(poly)