# Pascal's Triangle
Pascal's triangle is a mathematical concept that generates a triangular array of numbers, with each row representing the coefficients of the binomial expansion (x + y)^n. The triangle starts with a single value of 1 at the top, and each subsequent row is constructed by summing adjacent elements from the row above.

## Task Overview
This task involves creating a Python function ```pascal_triangle(n)``` that generates Pascal's triangle up to the nth row. The function should return a list of lists of integers, where each inner list represents a row of the triangle.

## Function Specifications:
The function should return an empty list if ```n``` is less than or equal to 0.

```n``` is assumed to always be an integer.

**Example:**
For n = 5, the expected output would be:
```
     [1],
    [1, 1],
   [1, 2, 1],
  [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
```
