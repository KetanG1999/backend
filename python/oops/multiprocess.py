# multiprocessing : performing task in multiple core
# processor in multiple form

# normal process 
# def DisplatEven(no):
#     for i in range(1,no):
#         if(i%2==0):
#             print('Even no:',i)

# def DisplayOdd(no):
#     for i in range(1,no):
#         if(i%2!=0):
#             print('Even no :',i)
# def main():
#     num = 50
#     DisplatEven(num)
#     DisplayOdd(num)
# if __name__:='__main__':
#     main()

# using the multiprocessing in python

import multiprocessing
# import multiprocessing.process
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
    num = 50
    p1 = multiprocessing.Process(target=DisplayEven, args=(num,))
    p2 = multiprocessing.Process(target=DisplayOdd,args=(num,))
# start of process excution
    p1.start()
    p2.start()
#   End of proccess exuecution
    p1.join()
    p2.join()

    print('End of processing')
if __name__=='__main__':
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print('Exucation Time:',end_time-start_time)
