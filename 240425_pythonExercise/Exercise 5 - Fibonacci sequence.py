a, b = 0, 1
nterms = int(input("Enter the number of terms: "))
for i in range(nterms):
    print(a, end=' ')
    a, b = b, a + b