# -*- coding: utf-8 -*-
"""
Developed on 2019

@author: Dr. Hakan İbrahim Tol (thanks to ChatGPT for optimization revision)

"""

""" LIBRARIES """

import numpy as np
import math

class GoalSeekError(Exception):
    pass

def GoalSeek(fun, goal, x0, fTol=1e-6, MaxIter=200, positive_only=False, bracket=None):
    """
    Excel-like goal seek: solves fun(x) = goal.
    Returns the root x (float). Raises GoalSeekError on failure.

    Parameters
    ----------
    fun : callable
        Function of a single variable.
    goal : float
        Target value for fun(x).
    x0 : float
        Initial guess (used if bracket is not provided).
    fTol : float
        Absolute tolerance on |fun(x) - goal|.
    MaxIter : int
        Max iterations for bisection after bracketing.
    positive_only : bool
        If True, only search x > 0.
    bracket : tuple(a, b) or None
        Optional explicit bracketing interval with a sign change for
        g(x) = fun(x) - goal. If None, a bracket is auto-built around x0.
    """

    def g(x):
        val = fun(x) - goal
        if not np.isfinite(val):
            raise GoalSeekError(f"Non-finite function value at x={x}.")
        return val

    # --- Build or validate bracket [a,b] with sign change ---
    if bracket is not None:
        a, b = float(bracket[0]), float(bracket[1])
        if a == b:
            raise GoalSeekError("Invalid bracket: endpoints are identical.")
        if a > b:
            a, b = b, a
        if positive_only and b <= 0:
            raise GoalSeekError("Positive root requested, but bracket is non-positive.")
        if positive_only:
            a = max(a, np.finfo(float).tiny)
        ga, gb = g(a), g(b)
        if ga == 0.0:
            return a
        if gb == 0.0:
            return b
        if np.sign(ga) == np.sign(gb):
            raise GoalSeekError("Provided bracket does not contain a sign change.")
    else:
        # Auto-bracket by expanding around x0
        a = float(x0) - 1.0
        b = float(x0) + 1.0
        if positive_only:
            a = max(a, np.finfo(float).tiny)
            if b <= a:
                b = a * 2.0

        expand_factor = 2.0
        max_span = 1e16
        tries = 0

        while True:
            tries += 1
            ga, gb = g(a), g(b)
            if ga == 0.0:
                return a
            if gb == 0.0:
                return b
            if np.sign(ga) != np.sign(gb):
                break  # bracket found

            width = b - a
            if width <= 0:
                width = abs(a) + abs(b) + 1.0
            expand = width * (expand_factor - 1.0)

            if positive_only:
                a = max(a, np.finfo(float).tiny)
                b = b + expand if b > 0 else a * (1.0 + expand_factor)
            else:
                a -= expand
                b += expand

            if (b - a) > max_span or tries > 200:
                raise GoalSeekError(
                    "Failed to bracket a root. Provide a better x0 or an explicit bracket."
                )

        # fallthrough with valid a,b,ga,gb
    # --- Bisection ---
    iterations = 0
    while iterations < MaxIter:
        m = 0.5 * (a + b)
        gm = g(m)
        if abs(gm) <= fTol:
            return m
        # shrink to side with sign change
        if np.sign(g(a)) != np.sign(gm):
            b = m
        else:
            a = m
        iterations += 1

    # If here, return best midpoint even if not within tolerance
    return 0.5 * (a + b)
