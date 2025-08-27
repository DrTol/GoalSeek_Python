[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F2F01JB1KE)

# Excel “Goal Seek” in Python
Find the input value that makes a function reach a target output (the “goal”), similar to Excel’s Goal Seek.

This repo provides a small, dependency-light helper you can call like:
<pre> ```python x = GoalSeek(fun, goal, x0) ``` </pre>
It solves fun(x) = goal and returns the x value.

## Algorithms used in Goal Seek - Python
This code involves of root finding methods; at a first step, via the Line Search method, and, at the second step, the Bisection method. 

## Requirements
This tool requires that `NumPy` be installed.

## How2Use
Please see [ExampleScript.py](https://github.com/DrTol/GoalSeek_Python/blob/master/ExampleScript.py)

## License
You are free to use, modify and distribute the code as long as authorship is properly acknowledged.
