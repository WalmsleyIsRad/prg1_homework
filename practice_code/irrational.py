class Irrational:

    def __init__(self,iterations):
        self.iterations = iterations
        pass


    def factorial(self,n):
        if (n < 1):
            return 1
        else:
            return n * self.factorial(n-1)

    def pi(self,accuracy=10000):
        pi = 0
        for i in range(1,accuracy):
            pi += ((4.0 * (-1)**i)/(2*i-1))
        return pi * -1

    def e(self,places):
        e = 0
        for number in range(0,places):
            e = e + 1/self.factorial(number)
        return e

irrational = Irrational()
print(irrational.e(100))

    