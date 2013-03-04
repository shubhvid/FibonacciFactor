
#
# Solution to Problem: https://amazon.interviewstreet.com/challenges/dashboard/#problem/4fd653336df28
#
# Author: Shubham Vidyarthi
# March 4, 2013
# EMail: shubhvid@gmail.com
#

import sys, os
TEST = True

def invalid():
    print "INVALID INPUT"
    sys.exit(1)

def getInput(file=sys.stdin):
    try:
        K_list = [int(x.strip()) for x in file.readlines()]
        T = K_list[0]   # Number of Testcases
        K_list = K_list[1:]

        for K in K_list:
            if not (K > 1 and K < 1000000):
                raise
        if not (T > 0 and T < 6):
            raise Exception ("Invalid number of testcases %s" % T)
        if not T == len(K_list) :
            raise ("Declared number of testcases(%s) inconsistent with the actual list(%s)." % (T, len(K_list)))
        return K_list
    except:
        invalid()

# Check whether a number is prime
def isPrime(number):
    for i in range (2, int((number**(0.5))) + 1):
        if number % i == 0:
            return False
    return True


# For any number, return a list of its factors (prime and non-prime)
def getFactors(number):
    factors_list = []

    if isPrime(number):
        return [number]

    for i in range (2, int((number**(0.5))) + 1):
        if number % i == 0:
            factors_list.append(i)
            factors_list.append(number / i)

    return list(set(factors_list))

# Return only prime factors from getFactors
def getPrimeFactors(number):
    factors_list = getFactors(number)
    prime_factors_list = [i for i in factors_list if isPrime(i)]
    return prime_factors_list

# Single pass on generated-on-the-fly Fibonacci sequence
# until all the testcases are solved.
def searchFibonacci(factor_to_K_map, problem_set):
    this = 2 # 'this' <- the current fibonacci number being evaluated
    prev = 1 # need this to calculate the next fibonacci number
    solution_dict = {}
    while problem_set:
        this = this + prev
        prev = this - prev

        # Catch an infinite loop
        if this > 10**18:
            raise Exception ("Fibonacci range exceeded.")
        
        pf_list = getPrimeFactors(this)

        # For each prime factor of the current Fibonacci number, 
        for pf in pf_list:
            # Check which of the problem numbers (K) in all testcases
            # has this as a factor, if any.
            if pf in factor_to_K_map.keys():
                for K in factor_to_K_map[pf]:
                    if K in problem_set:
                        problem_set.remove(K)
                        solution_dict[K] = (this, pf)
                del factor_to_K_map[pf]
    return solution_dict

def main():
    if TEST:
        with open ("input00.txt", "r") as f:
            K_list = getInput(f)
    else:
        K_list = getInput()


    factor_to_K_map = {}
    
    # Get prime factors of each of the testcase numbers (K)
    for K in K_list:
        pf_list = getPrimeFactors(K)
        for pf in pf_list:
            if factor_to_K_map.has_key(pf):
                factor_to_K_map[pf].append(K)
            else:
                factor_to_K_map[pf] = [K]

    problem_set = K_list[:] # copy by value (don't copy reference)
    solution_dict = searchFibonacci(factor_to_K_map, problem_set)

    for K in K_list:
        print solution_dict[K][0], solution_dict[K][1]

if __name__ == "__main__":
    main()