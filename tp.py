import os,sys,subprocess
def isprime(n):
    for d in range(2,n//2 + 1):
        if n%d==0:
            return False
    return True
def primes(a,b):
    list=''
    for i in range(a,b):
        if isprime(i):
            list=list+" "+str(i)
    return list
def getprimes(a,b,n):
    print("parent :"+str(os.getpid()))
    print()
    print("process :")
    for i in range(a,b,int((a+b)/n)):
        fr,fw=os.pipe()
        pid=os.fork()
        if pid==0:
            print("pid :"+str(os.getpid())+" , ppid :"+str(os.getppid()))
            os.close(fr)
            f=os.fdopen(fw,'w')
            if i+int((a+b)/n)<=b:
                f.write(primes(i,i+int((a+b)/n)))
            else :
                f.write(primes(i,b))
            f.close()
            exit(0)
        elif pid>0:
            os.close(fw)
            f=os.fdopen(fr,'r')
            print(f.read())
            f.close()
a=input("veuillez saisir a :")
b=input("veuillez saisir b :")
c=input("veuillez saisir le nombre de process :")
getprimes(int(a),int(b),int(c))