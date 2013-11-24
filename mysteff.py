def arerror(old,new):
    """
    return absolute relative error as percentage, considering new as the new guess and old as the previous guess
    """
    return abs((new-old)/float(new))*100

def sigdigit(err):
    """
    calculate # of signifficant digits in answer
    """
    sigdigit=0
    count=0
    
    while err<1:
        err*=10
        count+=1
        
    fact=err/5.0
    
    if fact<=1:  sigdigit=count+1
    else:       sigdigit=count
    
    return sigdigit

def f(x):
    """
    definition of the desired function to solve  
    """   
    y=x**3-9*(x**2)+3.8197
    
    return y

def steff(f,x0,tol=0.0005,maxiter=1024):
    """    
    REF: 
    """	
    for i in range(1,maxiter):
        x1=x0+f(x0)
        x2=x1+f(x1)
        x=x0-((x1-x0)**2/(x2-2*x1+x0))
        #~ print x
        err=arerror(x0,x)
        print '%d: x_old(x0) = %f x_new(x) = %f x1 = %f x2 = %f error = %f percent num of signifficant digits in x: %d' % (i,x0,x,x1,x2,err,sigdigit(err))
        if err<=tol:
            print 'converged to %e in %d iterations' % (x,i)
            return 
        x0=x
    print 'failed to converge in %d iterations' % maxiter
    return

steff(f,.7)

