# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21,
# 34, ... The next number is found by adding up the two numbers before it.
# Write a recursive method fib(n) that returns the nth Fibonacci number. n is 0
# indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# ..., n == 0 should return 0 and n == 3 should return 2.
# Assume n is less than 15.
# Even though this problem asks you to use recursion, more efficient ways to
# solve it include using an Array, or better still using 3 volatile variables to
# keep a track of all required values. Check out this blog post to examine
# better solutions for this problem.

# Examples:
# fib(0) ==> 0

# fib(1) ==> 1

# fib(3) ==> 2

def fib(n:int) -> int:
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    
    return a

if __name__ == '__main__':
    assert(fib(0) == 0)
    assert(fib(1) == 1)
    assert(fib(3) == 2)
    assert(fib(10) == 55)