n = int(input("Enter the number of terms to be displayed in the sequence: "))
fibonacci = [0, 1]
for i in range(n):
    nxt_term = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(nxt_term)

print(f"The Fibonacci numbers for {n} terms are {fibonacci}")