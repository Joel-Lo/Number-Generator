import random
import time

# For range value add 1 to the last number in the number rang expected  E.g. Final number expected: 9999 -> Range: 10000
for i in random.sample(range(10000), k=10000):
    print(i)
    time.sleep(0.01)  #1000ms = 1s