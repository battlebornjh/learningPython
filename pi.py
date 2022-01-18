import time

start = time.time()
pi = 0
accuracy = 100000000
count = 0
countDisplay = 10
countStart = time.time()
print(countDisplay)
countDisplay = countDisplay - 1
for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))
    count = count + 1
    if count > (accuracy / 10):
        count = 0
        print(str(countDisplay) + " in " + str(time.time() - countStart) + " seconds.")
        countDisplay = countDisplay - 1
        countStart = time.time()
end = time.time()
print("Pi at " + str(accuracy) + " accuracy:" + " in " + str(end - start) + " seconds.")
print(pi)
