# Exception Handling

a = 5
b = 0

try:
    print("Resource Open")
    print(a/b)      # Directly jumps in except block
    print("Won't print")
except Exception as e:
    print("Error:", e)

# Always executes this block whether or not you get error.
finally:
    print("Resource Close")
