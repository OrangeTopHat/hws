
import time


def time_calc(func):
    def ihavenoidea(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час - {execution_time} секунд")
        return result
    return wrapper


@ihavenoidea
def some_function():
    time.sleep(2)

some_function()









