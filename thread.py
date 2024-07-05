import threading
def cal_fun(n):
    print("hello",n)
t1=threading.Thread(target=cal_fun,args=(10,))
t1.start()