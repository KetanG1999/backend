# multithreding: use of single core processor
# having multiple tread is working with the 
import threading
import time
def DisplayEven(no):
    for i in range(1,no):
        if(i%2==0):
            print('Even no:',i)

def DisplayOdd(no):
    for i in range(1,no):
        if(i%2!=0):
            print('Even no :',i)
def main():
    num=100
    t1 = threading.Thread(target=DisplayEven, args=(num,))
    t2 = threading.Thread(target=DisplayOdd, args=(num,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print('End of threading')

if __name__=="__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print('Exucation Time:',end_time-start_time)