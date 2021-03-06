from orthogonalization import *
import orthogonalization
from scipy import linalg as la
import time

if False:
    nlist = [1, 10, 100, 1000]
    norms = []
    i_divs = []
    eigs = []
    dets = []
    tol = 1e-6
    eps = 1e-7

    for n in nlist:
        A = np.vstack((np.ones(n), eps*np.eye(n))).T  
        O = Orthogonalization(A, assume_li = True)
        Q = O.gramschmidt()
        QTQ = np.dot(Q,Q.T)
        norms.append(np.linalg.norm(Q, ord=2))
        i_divs.append(np.linalg.norm(QTQ-eye(n), ord=2))
        dev = np.abs(np.linalg.eig(QTQ)[0]-ones(n))
        eigs.append(dev[dev>tol])
        dets.append(np.linalg.det(QTQ))

    print norms, "\n\n", i_divs, "\n\n", eigs, "\n\n", dets

if False:
    nlist = [1, 10, 100, 1000]
    norms = []
    i_divs = []
    eigs = []
    dets = []
    tol = 1e-6
    eps = 1e-7

    for n in nlist:
        A = np.vstack((np.ones(n), eps*np.eye(n))).T  
        Q, r = la.qr(A)
        QTQ = np.dot(Q,Q.T)
        norms.append(np.linalg.norm(Q, ord=2))
        i_divs.append(np.linalg.norm(QTQ-eye(n), ord=2))
        dev = np.abs(np.linalg.eig(QTQ)[0]-ones(n))
        eigs.append(dev[dev>tol])
        dets.append(np.linalg.det(QTQ))

    print norms, "\n\n", i_divs, "\n\n", eigs, "\n\n", dets

if False:
    n = 500
    A = np.random.rand(n, n)
    b = np.random.rand(n)
    t0 = time.time() 
    x = la.solve(A, b)
    print time.time()-t0
    print np.linalg.norm(dot(A, x)-b)

    t0 = time.time()
    Q, r = la.qr(A)
    QTb = np.dot(Q.T, b)

    x = zeros(n)

    for i in range(n):
        sum = 0

        for k in range(n-i, n):
            sum += r[n-i-1][k]*x[k]
        
        x[n-i-1] = (QTb[n-i-1]-sum)/r[n-i-1][n-i-1]
    
    print "\n", time.time()-t0
    print np.linalg.norm(dot(A,x)-b)

if False:
    A = np.random.rand(5, 8)
    o = Orthogonalization(A)
    Q, R = o.householder()
    print np.round(R, decimals = 3), "\n\n", np.round(np.dot(Q.T,Q), decimals = 3), "\n\n", np.round(o.A.T - np.dot(Q, R), decimals = 8) 


if False:
    nlist = [1, 10, 100, 1000]
    norms = []
    i_divs = []
    eigs = []
    dets = []
    tol = 1e-6
    eps = 1e-7

    for n in nlist:
        A = np.vstack((np.ones(n), eps*np.eye(n))).T  
        O = Orthogonalization(A, assume_li = True)
        Q, R = O.householder()
        QTQ = np.dot(Q,Q.T)
        norms.append(np.linalg.norm(Q, ord=2))
        i_divs.append(np.linalg.norm(QTQ-eye(O.m), ord=2))
        dev = np.abs(np.linalg.eig(QTQ)[0]-ones(O.m))
        eigs.append(dev[dev>tol])
        dets.append(np.linalg.det(QTQ))

    print norms, "\n\n", i_divs, "\n\n", eigs, "\n\n", dets

if False:
    n = 500
    A = np.random.rand(n+10, n)
    o = Orthogonalization(A.T)
    t0 = time.time()
    Q, R = o.householder(both = True)
    print "householder:\n", time.time()-t0, "\n"
    t0 = time.time()
    Q, R = la.qr(A)
    print "scipy's qr:\n", time.time()-t0
    

if True:
    A = np.random.rand(5, 5)
    o = Orthogonalization(A)
    Q, R = o.givens(both = True)
    print np.round(R, decimals = 3), "\n\n", np.round(np.dot(Q.T,Q), decimals = 5), "\n\n", np.round(o.A.T - np.dot(Q, R), decimals = 8)     

if True:
    n = 1000
    A = np.random.rand(n, n)
    o = Orthogonalization(A.T)
    t0 = time.time()
    Q, R = o.householder(both = True)
    print "householder:\n", time.time()-t0, "\n"
    t0 = time.time()
    Q, R = o.givens(both = True)
    print "givens:\n", time.time()-t0

if False:
    A = np.random.rand(5,8)
    o = Orthogonalization(A)
    q_list, R = o.givens(both = False)
    print np.round(q_list, decimals = 3)
