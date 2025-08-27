## ExampleScript running GoalSeek (Excel) in Python
#   prepared by Dr. Hakan İbrahim Tol
#
#   Updated examples added for robustness and new features (thanks to ChatGPT)
#
#   Required Python Library: NumPy

from WhatIfAnalysis import GoalSeek
import math

## EXAMPLE 1
#   Finding the x value, its square results in goal = 10

def fun(x):
    return x**2

goal = 10
x0   = 3

Result_Example1 = GoalSeek(fun, goal, x0)
print('Result of Example 1 is = ', Result_Example1)


## EXAMPLE 2
#   Reference: https://www.ablebits.com/office-addins-blog/2018/09/05/use-goal-seek-excel-what-if-analysis/
#
#   Problem: If you sell 100 items at $5 each, minus the 10% commission, 
#   you will make $450. The question is: How many items do you have to 
#   sell to make $1,000?

def Revenue(x):
    item_price = 5    # [$]
    commission = 0.1  # 10%
    return item_price * x * (1 - commission)

goal = 1000
x0   = 100

Result_Example2 = GoalSeek(Revenue, goal, x0)
print('Result of Example 2 is = ', Result_Example2)


## EXAMPLE 3
#   Positive-only solution: solve x^2 = 9, expecting x = 3 (not -3)

def square(x):
    return x**2

goal = 9
x0   = 1

Result_Example3 = GoalSeek(square, goal, x0, positive_only=True)
print('Result of Example 3 (positive root only) is = ', Result_Example3)


## EXAMPLE 4
#   Bracketed solve for a function with a singularity.
#   f(x) = (10*x/(10 - x))^2   has a singularity at x=10.
#   Solve f(x) = 25 for x in (0,10).

def rational(x):
    return (10 * x / (10 - x))**2

goal = 25
# bracket must avoid x=10
Result_Example4 = GoalSeek(rational, goal, x0=1.0, bracket=(1e-6, 9.999), positive_only=True)
print('Result of Example 4 is = ', Result_Example4)


## EXAMPLE 5
#   Angles: atan(x) returns radians. To target 30 degrees, convert to radians.
#   Solve atan(x) = 30 degrees.

def atan_func(x):
    return math.atan(x)

goal_deg = 30.0
goal_rad = math.radians(goal_deg)

x0 = 0.5
Result_Example5 = GoalSeek(atan_func, goal_rad, x0, positive_only=True)
print('Result of Example 5 (atan target 30 deg) is = ', Result_Example5)
