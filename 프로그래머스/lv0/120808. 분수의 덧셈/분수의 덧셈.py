import fractions

def solution(numer1, denom1, numer2, denom2):
    x = fractions.Fraction(numer1, denom1)
    y = fractions.Fraction(numer2, denom2)
    
    result = x +y
    answer = [result.numerator, result.denominator]
    return answer