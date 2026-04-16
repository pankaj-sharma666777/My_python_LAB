from multiprocessing import Pool
import time


def f(x):
    sum = 0
    for i in range(1000):
        sum += i*i
    return sum

if __name__ == "__main__":

    t1=time.time()
    P = Pool()
    result = P.map(f,range(100000))
    P.close()
    P.join()


    print("Pool took: ",time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("serial processing took: ", time.time()-t2)



