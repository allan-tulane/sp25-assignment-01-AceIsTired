"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

'''\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\
~~~~~~~~~~~~ra + rb\\
~~~~~~~~\texttt{end}{}.\\
\end{array}'''
def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x - 1) + foo(x - 2)
    pass

def longest_run(mylist, key):
    max = 0
    ind = 0

    for i in range(len(mylist)):
        if mylist[i] == key:
            ind += 1 
            if ind > max:
                max = ind
        else:
            run = 0
        return max

    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    
    # Base Cases
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True) # Return proper Result dependinf on case
        else:
            return Result(0, 0, 0, False)
    
    mid = len(mylist) // 2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)

    lcount = left.right_size if mylist[mid - 1] == key else 0
    rcount = right.left_size if mylist[mid] == key else 0
    cross_run = lcount + rcount if lcount and rcount else 0

    longest_size = max(left.longest_size, right.longest_size, cross_run)
    left_size = left.left_size + right.left_size if left.is_entire_range else left.left_size
    right_size = right.right_size + left.right_size if right.is_entire_range else right.right_size

    return Result(left_size, right_size, longest_size, left.is_entire_range and right.is_entire_range)

    pass



