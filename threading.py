import time
import threading
import os

def f1(a) :
    a= 0
    for i in range(10000,20000) :
        print("--F1--- " +str(i))
        print("---F1----"+str(os.getpid()))
        print("---F!----"+str(threading.current_thread()))
        time.sleep(1)

def f2() :
    for i in range(10000,20000) :
        print("--F2--- " +str(i))
        print("---F2----"+str(os.getpid()))
        print("---F2----"+str(threading.current_thread()))
        time.sleep(1)



if __name__ == "__main__" :
    print("hiiii")
    t1 = threading.Thread( target=f1,args=(2,))
    t1.start()
    t2 = threading.Thread( target=f2,args=())
    t2.start()
    for i in range(20000,30000) :
        time.sleep(1)
        print("--MAIN--- " +str(i))
        print("---MAIN----"+str(os.getpid()))
        print("---MAIN----"+str(threading.current_thread()))
