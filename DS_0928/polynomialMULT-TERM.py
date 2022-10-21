class Term:
    def __init__(self, coef=0, exp=0):
        self.coef = coef
        self.exp = exp

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.coef, self.exp}"

class Polynomial1:
    """Polynomial using array."""

    def __init__(self):
        self.bgn = 0
        self.end = 0
        self.terms = []

    def attach(self, coef=0, exp=0):
        self.terms.append(Term(coef, exp))
        return self

    def evaluate(self, x):
        return sum((i.coef * (x ** i.exp) for i in self.terms))

    # -> 이거 없애도 된다.
    '''
    같아지는 케이스는 None을 리턴하고 아닌 경우는 적법한 놈을 찾은 것이다. 
    '''
    def find_term(self, exp):
        # 제공된 exp 에 상응하는 Term 을 반환한다.
        i = 0
        while i < len(self.terms) and self.terms[i].exp != exp:
            i += 1

        return self.terms[i] if i < len(self.terms) else None

    def __add__(self, other):
        poly = Polynomial1()
        terms_a = self.terms
        terms_b = other.terms

        pos_a, pos_b = 0, 0
        while pos_a < len(terms_a) and pos_b < len(terms_b):
            term_a, term_b = terms_a[pos_a], terms_b[pos_b]

            if term_a.exp > term_b.exp:
                poly.attach(term_a.coef, term_a.exp)
                pos_a += 1
            elif term_a.exp < term_b.exp:
                poly.attach(term_b.coef, term_b.exp)
                pos_b += 1
            else:
                coef = term_a.coef + term_b.coef
                if coef != 0:
                    poly.attach(coef, term_a.exp)
                pos_a += 1
                pos_b += 1

        '''
        이 두 파트를 놓치면 안된다. 내 함수가 차수가 다 똑같으면 괜찮은데 그렇지 않은 경우 문제가 생기기 때문이다.
        '''
        while pos_a < len(terms_a):
            term = terms_a[pos_a]
            poly.attach(term.coef, term.exp)
            pos_a += 1
        while pos_b < len(terms_b):
            term = terms_b[pos_b]
            poly.attach(term.coef, term.exp)
            pos_b += 1

        return poly


    def __str__(self):
        ret = ""
        terms = sorted(self.terms, key=lambda x: x.exp, reverse=True)
        for i in terms:
            ret += f"({i.coef})x^{i.exp} + "
        return f"{ret}\b\b\b"

if __name__ == "__main__":
    poly1 = Polynomial1()
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)

    poly2 = Polynomial1()
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)

    poly = poly1 + poly2
    print("poly =\n", poly)