def aerror(old,new):
    return abs((new-old)/float(new))*100
    
def f(x):
    y=x**3-9*(x**2)+3.8197
    return y

def sec(x0,x1,tol=0.005,maxiter=10):    
    
    for i in range (maxiter):
        x=x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        err=aerror(x1,x)
        if err<tol:
            return x
        x0=x1
        x1=x
        print 'x = %f error = %f'%(x,err)
    print 'maxiter exceeded'
    
sec(1,2)
