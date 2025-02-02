This repository contains examples of a common error in Python when calculating the average of a list and its solution. The `bug.py` file shows the original code with the error, while `bugSolution.py` presents the corrected version. The error arises when attempting to calculate the average of an empty list or a list containing non-numeric values. The solution robustly handles both cases, returning 0 for empty lists and raising a TypeError for lists with non-numeric elements.