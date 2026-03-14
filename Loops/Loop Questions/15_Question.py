# You want to simulate tea heating. It starts at 40 degree Celcius an d boild at 100 degree celcius.
# Task : use while loop.
# Increase temperature by 15 until it reaches or exceeds 100.
# print each temperature step.

temperature = 40

while temperature <100:
    print(f"Current Temperature is {temperature}")
    temperature += 15
print(f"Now Tea is boiling at {temperature}")