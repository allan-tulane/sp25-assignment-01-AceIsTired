

# CMPS 2200 Assignment 1

**Name:** Jamari Ross


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository.


1. (2 pts ea) **Asymptotic notation** (12 pts)

  - **1a. Is $2^{n+1} \in O(2^n)$? Why or why not?**
Yes, because if we break it down into: 
    - $2^{n+1} \le c \times 2^n$
    which further breaks down to:
    - $2\times2^{n} \le c \times 2^n$
We can see that the inequality holds when $c \ge 2$.
.
  - **1b. Is $2^{2^n} \in O(2^n)$? Why or why not?**
No. Lets break $2^{2^n} \in O(2^n)$ down into $2^{2^n}\le c\times2^n$
Before we plug in values for c, we can analyze and compare the growth rates of these functions by using log.
$log2(2^{2^n}) = 2^n$
$log2(2^n) = n$
As we can see, the $2^{2^n}$ scales exponentially, which increases much quicker than $2^n$, which scales linearly. Because a constant cannot account for the curve of 2^n, there is no value that will allow n to bound $2^n$ for all values $n > n0$. Therefore, it is not $\in O(2^n)$.
.
  - **1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?**
No, because $n^{1.01}$ grows much faster than $\mathrm{log}^2 n$, and for a large enough $n$, it will always grow faster than $\mathrm{log}^2 n$, therefore it is not bound by $\in O(\mathrm{log}^2 n)$.
.
.
.

  - 1d. **Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?**
Yes becasue the limits of both of these functions approach infinity as $n$ grows, therefore it is bounded by $\in \Omega(\mathrm{log}^2 n)$.
.
.
.
  - 1e. **Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?**
No, because $\sqrt{n}$ grows significantly faster than $({log} n)^3$, therefore it is not bound by $\in O((\mathrm{log} n)^3)$.
.
.
.
  - 1f. **Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?**
Yes, because the limits of both of these functions approach zero as $n$ grows, therefore it is bounded by $\in \Omega((\mathrm{log} n)^3)$.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ...
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\
~~~~~~~~~~~~ra + rb\\
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`

  - 2b. (6 pts) What does this function do, in your own words?

This function returns the fibonacci sequence at a given index (x). If x is less than or equal to 1, it will return x, else it will return the sum of the two preceeding indexes by passing other itterations of the foo function.

.
.

3. **Parallelism and recursion** (26 pts)

Consider the following function:

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`

  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.

  DONE

  - 3b. (4 pts) What is the Work and Span of this implementation?

The work and span of this implementation is both O(n) since it will always iterate over the length of the list (or n).
.
.


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.

  DONE

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?
Since the calls are splitting at each level, the work of this algorithm is W(n) = O(n log n) and the span would be O(log n) due to the jobs being done in parallel.
.
.
.
.


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?

  The work being done at each tree is still constant, so O(n), and the span is O(log n) due to the depth of the tree.

.
.
