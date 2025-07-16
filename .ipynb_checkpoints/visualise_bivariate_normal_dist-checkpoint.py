import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Define grid
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# Define parameters of a bivariate normal distribution
mu = [0, 0]
cov = [[1, 0.6], [0.6, 1]]  # correlated variables

# Get the joint distribution
rv = multivariate_normal(mu, cov)
Z = rv.pdf(pos)

# Marginal distribution of X: integrate out Y (approximate via trapezoidal rule)
f_X = np.trapz(Z, y, axis=0)
f_Y = np.trapz(Z, x, axis=1)

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Joint PDF contour
axs[0].contourf(X, Y, Z, levels=20, cmap='viridis')
axs[0].set_title("Joint PDF of X and Y")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")

# Marginal PDF of X
axs[1].plot(x, f_X, color='blue')
axs[1].set_title("Marginal PDF of X (∫ f(x, y) dy)")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Density")

# Marginal PDF of Y
axs[2].plot(y, f_Y, color='green')
axs[2].set_title("Marginal PDF of Y (∫ f(x, y) dx)")
axs[2].set_xlabel("Y")
axs[2].set_ylabel("Density")

plt.tight_layout()
plt.show()