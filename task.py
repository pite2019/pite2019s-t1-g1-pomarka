from matrix import Matrix

if __name__ == '__main__':
    m = Matrix(2, 2, 3, 4)
    m2 = Matrix(1, 1, 1, 1)

    print('First matrix: m:')
    print(m)

    print('Second matrix: m2:')
    print(m2)

    print('Adding matrixes: m3 = m + m2:')
    m3 = m + m2
    print(m3)

    print('Substracting matrixes: m4 = m - m2:')
    m4 = m - m2
    print(m4)

    print('Adding one matrix to another: m += m2:')
    m += m2
    print(m)

    print('Substracting one matrix from another: m -= m2:')
    m -= m2
    print(m)

    print('Adding value to matrix elements: m5 = m + 2')
    m5 = m + 2
    print(m5)

    print('Adding value to matrix elements: m6 = 2 + m')
    m6 = 2 + m
    print(m6)