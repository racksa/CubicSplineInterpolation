import numpy as np

# Cubic class
class myCubicSpline:
    def __init__( self, X, Y ):
        self.X = X
        self.Y = Y
        self.N = len(X)
        self.h = np.zeros( self.N )
        self.A = np.zeros( (self.N, self.N) )
        self.b = np.zeros( self.N )
        self.alpha = np.zeros( self.N )
        self.beta = np.zeros( self.N )

        # Construct h
        for i in range(1, self.N):
            self.h[i] = self.X[i] - self.X[i-1]
        self.h[0] = self.X[0] - self.X[-1]

        # Construct the matrix
        for i in range( self.N-1 ):
            self.A[i][i] = 2.*(self.h[i] + self.h[i+1])
            self.A[i+1][i] = self.h[i+1]
            self.A[i][i+1] = self.h[i+1]
        self.A[-1][-1] = 2.*(self.h[-1] + self.h[0])

        # Construct r.h.s. of the equation
        for i in range(1, self.N-1 ):
            self.b[i] = 6.*( (self.Y[i+1]-self.Y[i])/self.h[i+1] - (self.Y[i]-self.Y[i-1])/self.h[i] )

        # Solve for sigmas
        self.sigma = np.linalg.solve( self.A, self.b )

        # Compute alpha and beta
        for i in range(1, self.N ):
            self.alpha[i] = (self.Y[i] - 1./6*self.sigma[i]*self.h[i]**2)/self.h[i]
            self.beta[i] = (self.Y[i-1] - 1./6*self.sigma[i-1]*self.h[i]**2)/self.h[i]

    def spline( self, j, varx ):
        '''
        A function that returns s_j(varx).
        '''
        return self.sigma[j-1]*(self.X[j]-varx)**3/6./self.h[j] + self.sigma[j]*(varx-self.X[j-1])**3/6./self.h[j] + self.alpha[j]*(varx-self.X[j-1]) + self.beta[j]*(self.X[j]-varx)
