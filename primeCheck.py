class PrimeSolution:

    def isPrime(self, num):
        if num % 1 or num <= 1:
            # print ("Need integral number greater than 1")
            # return False
            return "Need integral number greater than 1"
        factors = set()
        for dividend in range(1,int(num**0.5)+1):
            if not num%dividend:
                for factor in {dividend, num//dividend}:
                    factors.add(factor)
                if len(factors) > 2:
                    print(f'NOT prime. {set((dividend, num//dividend))}')
                    return False
        print(f'Prime!')
        return True

# while True:
#     PrimeSolution.isPrime(int(input('\nEnter number to check primality: ')))