# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts<max_retries:
    print("Attempt", attempts + 1, "-wait_time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1 #by putting 0 instead of 1 you can loop for infinte times. You may use this code on display some images that changes with time to time like silideshow but different time variation.
