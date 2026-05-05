#  Multithreading

# Definition: Running multiple threads (tasks) simultaneously for concurrency.

# Module: threading

# Example:

# import threading

# import threading

# def task():
#     print(f"Running in thread: {threading.current_thread().getName()}")

# t = threading.Thread(target=task)
# t.setName("hulk")
# t.start()
# t.join()


def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]


    for num in arr:
        if num > max_val:
            max_val =num
        if num < min_val:
            min_val = num

    return max_val,min_val

arr = [10,3,5,19,3]
maximum, minimum = find_max_min(arr)
print(maximum,minimum)       

