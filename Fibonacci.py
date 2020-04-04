
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
            a, b = b, a+b
    return a
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument(-n, help="The Fibonacci number " + \
                       "you wish to calculate.", type=int)
    args = parser.parse_args()

    result = fib(args.list)
    print "The "+str(args.list)+"th fib number is "+str(result)

if __name__ == '__main__':
    Main()