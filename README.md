[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F2F01JB1KE)

# Excel “Goal Seek” in Python
Find the input value that makes a function reach a target output (the “goal”), similar to Excel’s Goal Seek.

This repo provides a small, dependency-light helper you can call like:
```python 
x = GoalSeek(fun, goal, x0)
```
It solves the function fun(x) = goal and returns the x value (that returns the value of the function as same/close as/to goal).

## Features
+ **Excel-like call:** `GoalSeek(fun, goal, x0)` returns a single number.
+ **Robust:** automatic interval bracketing + bisection (no fragile vectorization).
+ **Positive solutions (optional):** positive_only=True to restrict to x > 0.
+ **Custom interval (optional):** bracket=(a, b) if you know a safe interval.
+ **Helpful errors:** clear messages when no root is found or function is invalid.

## Algorithms/Methods used in Goal Seek - Python
1. **Auto-Bracketing (interval expansion)**
Starting from your initial guess x0, the code expands an interval until the difference g(x) = fun(x) - goal changes sign. A sign change means there is a root inside that interval.
You can also skip this step by supplying your own bracket=(a, b).

2. **Bisection**
After a valid interval is found, the classic bisection method is used to converge to the root. Bisection is simple and reliable when a root is bracketed.

**Note:** older versions used a vectorized “line search” to guess the bracket. That was replaced with deterministic interval expansion for reliability. Thanks to ChatGPT. :) 

## Requirements
This tool requires that `NumPy (1.20+)` be installed.

## API
```python 
GoalSeek(fun, goal, x0, fTol=1e-6, MaxIter=200, positive_only=False, bracket=None) -> float
```
+ `fun`: your function `f(x)`
+ `goal`: target value to reach (solve `f(x) = goal`)
+ `x0`: initial guess (used to build the interval if bracket is not given)
+ `fTol`: tolerance on `|f(x) - goal|`
+ `MaxIter`: maximum bisection iterations
+ `positive_only`: restrict to `x > 0` if `True`
+ `bracket`: optional `(a, b)` that already contains the root

Returns a **float** (the root).
Raises a **GoalSeekError** if it cannot find a valid interval or the function is not finite at sampled points.

## Example Problems (described)
> The concrete Python for these is in `ExampleScript.py` inside the repo: [ExampleScript.py](https://github.com/DrTol/GoalSeek_Python/blob/master/ExampleScript.py)

1. Square equals target
Find `x` such that `x^2 = 10`. (Classic root finding.)

2. Sales revenue
You sell items at $5 with 10% commission. How many items to make $1000 net revenue? (Based on an Excel Goal Seek tutorial.)

3. Positive root only
Solve `x^2 = 9` but return only the positive solution `x = 3` (the other solution is -3).

4. Function with a singularity
`f(x) = (10*x/(10 - x))^2` has a pole at `x = 10`. Solve `f(x) = 25` within `(0, 10)`. Here you pass a safe bracket like `(1e-6, 9.999)`.

5. Angles and units
Solve `atan(x) = 30°`. Since atan returns radians, convert the goal to radians first.

## Updates in This Version
+ **Removed deprecated** `np.asscalar`
Fixed `NumPy` deprecation that caused crashes in modern environments.

+ **Replaced vectorized line search with deterministic auto-bracketing**
Eliminates “`x_lb` referenced before assignment” and improves reliability.

+ **Added** `positive_only` **option**
Useful for domains where only positive solutions make sense (e.g., finance).

+ **Added optional** `bracket=(a, b)`
Lets you guide the solver in tricky cases (singularities, constrained domains).

+ **Kept the original call pattern**
Still `GoalSeek(fun, goal, x0, ...)` returning a scalar.

+ **Clearer error messages**
Better guidance when a root cannot be bracketed or function values are invalid.

## License
You are free to use, modify and distribute the code as long as **authorship is properly acknowledged**. Please reference this repository in derivative works.

## Acknowledgements
Above all, I give thanks to **Allah, The Creator (C.C.)**, and honor His name **Al-‘Alīm (The All-Knowing)**.

This repository is lovingly dedicated to my parents who have passed away, in remembrance of their guidance and support.

I would also like to thank **ChatGPT (by OpenAI)** for providing valuable support in updating and improving the Python implementation of Goal Seek.

Thanks to all users who provided feedback and reported issues, which directly contributed to making this tool more robust and user-friendly:
+ NumPy deprecation (asscalar) issues
+ “x_lb referenced before assignment” when bracketing failed
+ The need to restrict solutions to positive values

Your feedback directly shaped these improvements!
