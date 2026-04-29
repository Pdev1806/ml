import numpy as np
import matplotlib.pyplot as plt
photo = plt.imread(r"c:\ml\basics\photo.jpeg")
plt.imshow(photo[:,:,0].T)
plt.show()
