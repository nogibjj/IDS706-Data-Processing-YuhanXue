from mylib.lib import get_mean, get_median, get_stddev
import time
import psutil
import pandas as pd


def test():
    start = time.time()
    data = pd.read_csv("diabetes.csv")
    get_mean(data, "Age")
    get_median(data, "Age")
    get_stddev(data, "Age")

    end = time.time()
    duration = end - start
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory()

    print(f"Elapsed time: {duration:.4f} seconds")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {mem_usage.percent}%")


if __name__ == "__main__":
    test()
    print("CICD Passed.")
