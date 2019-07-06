## ExampleScript running GoalSeek (Excel)
#   prepared by Hakan İbrahim Tol, PhD

## Required Python Library: NumPy

from WhatIfAnalysis import GoalSeek

## EXAMPLE 1
#   Finding the x value, its square results in goal = 10

# (i)   Define the formula that needs to reach the (goal) result
def fun(x):
    return x**2

# (ii)  Define the goal (result)
goal=10

# (iii) Define a starting point
x0=3

## Here is the result
Result=GoalSeek(fun,goal,x0)
print(Result)

## EXAMPLE 2
#   See Reference for the Excel tutorial: https://www.ablebits.com/office-addins-blog/2018/09/05/use-goal-seek-excel-what-if-analysis/

#   Problem: If you sell 100 items at $5 each, minus the 10% commission, you will make $450.
#   The question is: How many items do you have to sell to make $1,000?

# (i)   Define the formula that needs to reach the (goal) result
def Revenue(x):
    # x     : quantity of the items (to be solved)

    item_price=5    # [$]
    comission=0.1   # 10% comission

    return item_price*x*(1-comission)

# (ii)  Define the goal (result)
goal=1000           # [$]

# (iii) Define a starting point
x0=100

## Here is the result
Result=GoalSeek(Revenue,goal,x0)
print(Result)
