
def aerror(old,new):
    return abs((new-old)/float(new))*100
    
def f(x):
    y=x**3-9*(x**2)+3.8197
    return y
    
def bisec(left,right,maxiter=10,tol=.005):
    
    if f(left)*f(right)>0:
        print 'no root or more than one root in region'
        return
        
    for i in range(1,maxiter):
        x=(left+right)/2.0
        
        if i>1:
            err=aerror(x_old,x)
            print '%d. x = %f error = %f'%(i,x,err)
            if err<tol: return x
            
        if f(x)*f(left)<0:
            #~ print '<'
            right = x
        elif f(x)*f(right)<0:
            left = x
        
        x_old=x
    print 'exceeded the maxiter'
    
print bisec(0,1,20)

    
