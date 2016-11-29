'''
Google code jam - Minimum scalar product
http://code.google.com/codejam/contest/dashboard?c=32016#s=p0&a=2

Problem

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn).
The scalar product of these vectors is a single number,
calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish.
Choose two permutations such that the scalar product of your two new vectors is
the smallest possible, and output that minimum scalar product.

Input

<number of testcases>
<tescase 1 - vector size>
<v1>
<v2>
<tescase 2 - vector size>
<v1>
<v2>
...


One line per test cases :
Case #<index>: <result>

Usage:
    python solve.py < data/A-small-practice.in > data/A-small-practice.out
    python solve.py < data/A-large-practice.in > data/A-large-practice.out
'''


def minimum_scalar_product(v1, v2):
    return sum(a * b for a, b in zip(sorted(v1), sorted(v2, reverse=True)))


def run():
    nb_testcases = int(input())

    for index in range(1, nb_testcases + 1):
        input()  # ignore the vector size
        v1 = [int(val) for val in input().split(' ')]
        v2 = [int(val) for val in input().split(' ')]
        result = minimum_scalar_product(v1, v2)

        print('Case #{}: {}'.format(index, result))


if __name__ == '__main__':
    run()
