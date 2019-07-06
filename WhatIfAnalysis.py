import numpy as np

def GoalSeek(fun,goal,x0,fTol=0.0001,MaxIter=1000):
    # Goal Seek function of Excel
    #   via use of Line Search and Bisection Methods

    # Inputs
    #   fun     : Function to be evaluated
    #   goal    : XXX
    #   x0      : Starting point

    # Initial check
    if fun(x0)==goal:
        print('Exact solution found')
        return x0

    # Line Search Method
    step_sizes=np.logspace(-1,4,6)
    scopes=np.logspace(1,5,5)

    vFun=np.vectorize(fun)

    for scope in scopes:
        break_nested=False
        for step_size in step_sizes:

            cApos=np.linspace(x0,x0+step_size*scope,int(scope))
            cAneg=np.linspace(x0,x0-step_size*scope,int(scope))

            cA=np.concatenate((cAneg[::-1],cApos[1:]),axis=0)

            fA=vFun(cA)-goal

            if np.any(np.diff(np.sign(fA))):

                index_lb=np.nonzero(np.diff(np.sign(fA)))

                if len(index_lb[0])==1:

                    index_ub=index_lb+np.array([1])

                    x_lb=np.asscalar(np.array(cA)[index_lb][0])
                    x_ub=np.asscalar(np.array(cA)[index_ub][0])
                    break_nested=True
                    break
                else: # Two or more roots possible

                    index_ub=index_lb+np.array([1])

                    print('Other solution possible at around, x0 = ', np.array(cA)[index_lb[0][1]])

                    x_lb=np.asscalar(np.array(cA)[index_lb[0][0]])
                    x_ub=np.asscalar(np.array(cA)[index_ub[0][0]])
                    break_nested=True
                    break

        if break_nested:
            break
    if not x_lb or not x_ub:
        print('No Solution Found')
        return

    # Bisection Method
    iter_num=0
    error=10

    while iter_num<MaxIter and fTol<error:
        
        x_m=(x_lb+x_ub)/2
        f_m=fun(x_m)-goal

        error=abs(f_m)

        if (fun(x_lb)-goal)*(f_m)<0:
            x_ub=x_m
        elif (fun(x_ub)-goal)*(f_m)<0:
            x_lb=x_m
        elif f_m==0:
            print('Exact spolution found')
            return x_m
        else:
            print('Failure in Bisection Method')
        
        iter_num+=1

    return x_m


