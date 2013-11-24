def aerror(old,new):
    return abs((new-old)/float(new))*100
    
def f(x):
    y=x**3-9*(x**2)+3.8197
    return y
    
def f1(x):
    h=0.1
    for i in range (5): h*=0.1
    
    y=(f(x+h)-f(x))/h
    return y

def np(x0,tol=0.005,maxiter=10):
    
    for i in range(maxiter):
        x=x0-f(x0)/f1(x0)
        err= aerror(x0,x)
        print 'x0 = %f x = %f error = %f'%(x0,x,err)
        if err<=tol:
            return x
        x0=x
    print 'exceeded maxiter'
    
np(1)
    
    
    
    
