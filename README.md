# Perfect Numbers

A **perfect number** is a positive integer that is equal to the sum of its proper divisors (excluding itself). In other words, if you sum all the divisors of a number, excluding the number itself, and the sum equals the original number, then the number is a perfect number.

## **Definition**

Given a number \( n \), it is considered a perfect number if:
\[
\text{Sum of proper divisors} = n
\]

### **Example**

The proper divisors of a number \( n \) are all the numbers less than \( n \) that divide \( n \) without leaving a remainder.

For example:
- For \( n = 6 \): Divisors are \( 1, 2, 3 \) (excluding 6 itself).  
  \( 1 + 2 + 3 = 6 \). Hence, \( 6 \) is a perfect number.

---

## **Properties of Perfect Numbers**

1. Perfect numbers are rare.
2. The first perfect number is 6.
3. The second perfect number is 28.
4. Every even perfect number can be expressed in the form \( 2^{p-1}(2^p - 1) \), where \( 2^p - 1 \) is a prime number (known as a Mersenne prime).

---

## **Examples of Perfect Numbers**

| **Number** | **Proper Divisors**  | **Sum of Divisors** | **Perfect?** |
|------------|-----------------------|---------------------|--------------|
| 6          | 1, 2, 3              | 6                   | Yes          |
| 28         | 1, 2, 4, 7, 14       | 28                  | Yes          |
| 12         | 1, 2, 3, 4, 6        | 16                  | No           |
| 496        | 1, 2, 4, 8, 16, 31, 62, 124, 248 | 496       | Yes          |

---

## **Python Implementation**

Here is a Python implementation to check if a number is a perfect number:

```python
def is_perfect_number(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Example Usage
print(is_perfect_number(6))   # Output: True
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(12))  # Output: False