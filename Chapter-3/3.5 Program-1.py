import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,100,1000)
y=2*x
z=x**2
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(12,2))
axes[0].plot(x,y,color="green",lw=3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].plot(x,z,color="red",lw=2,ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.show()