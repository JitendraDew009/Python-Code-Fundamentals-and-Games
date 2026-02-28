# Generate a fuction with yield
#  Write a generator fuction that yields even numbers up to specified limit.

#final solution is last end




def even_generator(limit):
    
    for i in range(2, limit + 1, 2):
        print(i)

even_generator(10)
# Output is ->
# 2
# 4
# 6
# 8
# 10

print("/////Only return first object of i which is 2 because you have added return i so it just return the value of i in fist step/////////")
def even_generator2(limit):
    
    for i in range(2, limit + 1, 2):
        return i

print(even_generator2(10))

print("//////This gives you list////////")
def even_generator3(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

print(even_generator3(10)) #[2, 4, 6, 8, 10]

print("/////// Final Answer by using yield//////////")

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i #put yield instead of return because it stores the function and its state in memory like check point.
for num in even_generator(10):
    print(num)

# - return → ends the function immediately and hands back a single value.
# - yield → pauses the function, saves its state (like a checkpoint), and hands back one value at a time. When you call the function again, it resumes right where it left off.
# That’s why generators are perfect for producing sequences without storing everything in memory.

# Step-by-Step Execution
# - even_generator(10) creates a generator object.
# - The for num in even_generator(10) loop starts pulling values from it.
# - First iteration: i = 2 → yields 2.
# - Next iteration: resumes at i = 4 → yields 4.
# - Continues until i = 10.
# - When the loop ends, the generator is exhausted.

