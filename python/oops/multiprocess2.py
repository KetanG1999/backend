from multiprocessing import process
import os

def DispalySqure(no):
    print(os.getpid)
    print('Suare no',no*no)

def DisplayCube(no):
    print(os.getid())
    print('cube is:',no**3)



def main():
    p1 = process(target= DispalySqure, args=(3,))
    p2 = process(target= DisplayCube, args=(3,))
    
    p1.start()
    p2.start()
    print('process id for p1:',p1.pid)
    print('process id for p1:',p2.pid)

    p1.join()
    p2.join()

if __name__=='__main__':
    main()