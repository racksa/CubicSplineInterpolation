import numpy as np
import matplotlib.pyplot as plt
from myCubicSpline import *
from myData import *
from myMacro import *

# Main
bodyX, bodyY = makeParametric( bodyx, bodyy )
reyeX, reyeY = makeParametric( reyex, reyey )
leyeX, leyeY = makeParametric( leyex, leyey )
noseX, noseY = makeParametric( nosex, nosey )
mouthX, mouthY = makeParametric( mouthx, mouthy )
mouth2X, mouth2Y = makeParametric( mouth2x, mouth2y )

# Plot
fig, ax = plt.subplots(subplot_kw=dict(polar=False))
plotParametric( bodyX, bodyY )
plotParametric( reyeX, reyeY )
plotParametric( leyeX, leyeY )
plotParametric( noseX, noseY )
plotParametric( mouthX, mouthY )
plotParametric( mouth2X, mouth2Y )
plt.plot( bodyx, bodyy, 'o', reyex, reyey, 'o', leyex, leyey, 'o', nosex, nosey, 'o', mouthx, mouthy, 'o', mouth2x, mouth2y, 'o' )
ax.axis('equal')
plt.title('Cubic spline of a panda cartoon')
plt.show()
