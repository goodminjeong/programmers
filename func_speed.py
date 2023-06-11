from functools import wraps
import time


def func_speed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time_r = time.perf_counter()
        start_time_p = time.process_time()
        result = func(*args, **kwargs)
        end_time_r = time.perf_counter()
        end_time_p = time.process_time()
        print(
            f"\n{func.__qualname__} 실행 시간: {(end_time_r - start_time_r) * 1000:.2f}ms(real) / {(end_time_p - start_time_p) * 1000:.2f}ms(cpu)",
            flush=True,
        )
        return result

    return wrapper
