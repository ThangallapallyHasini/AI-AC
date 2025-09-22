import time
start_time = time.time()
nums = [i for i in range(1, 1000000)]
squares = [n**2 for n in nums]
print(len(squares))
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")