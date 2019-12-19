#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt

if __name__ == '__main__':
    fmt = '%a %d %b %Y %H:%M:%S %z'
    for i in range(int(input())):
        print(int(abs((dt.strptime(input(), fmt) - 
                    dt.strptime(input(), fmt)).total_seconds())))
# Complete the time_delta function below.

