# from multiprocessing import Pool
# import os

# def f(x):
#     print(f"Process {os.getpid()} handling {x}")
#     return x*x

# if __name__ == "__main__":
#     with Pool(processes=2) as p:
#         result = p.map(f, range(6))