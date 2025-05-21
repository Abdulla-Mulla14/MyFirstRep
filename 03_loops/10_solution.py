import time

wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print("Attempt", attempts + 1, "-WaitTime", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1