"""
Simple visualization utilities for the rotor field Q(x).

- Sample random points on S^3 (unit quaternions).
- Plot their 3D projection (q1, q2, q3) with color-coded q0.
- Show a toy Hopf-like knotted curve in R^3 (not a full Hopfion solution).
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def generate_Q_field(N, amp=1.0):
    """Sample N random points on S^3 (unit quaternions)."""
    phi1 = np.random.uniform(0, 2 * np.pi, N)
    phi2 = np.random.uniform(0, 2 * np.pi, N)

    q0 = amp * np.cos(phi1)
    q1 = amp * np.sin(phi1) * np.cos(phi2)
    q2 = amp * np.sin(phi1) * np.sin(phi2)
    q3 = amp * np.sin(phi2)

    Q = np.stack([q0, q1, q2, q3], axis=1)
    # optional: normalize explicitly
    Q /= np.linalg.norm(Q, axis=1, keepdims=True)
    return Q


def plot_Q_projection(Q):
    """3D scatter plot of (q1, q2, q3) with color-coded q0."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(Q[:, 1], Q[:, 2], Q[:, 3], c=Q[:, 0], cmap="viridis", alpha=0.8)
    ax.set_xlabel("q1")
    ax.set_ylabel("q2")
    ax.set_zlabel("q3")
    plt.title("Quaternion field Q(x) on S^3 (projection), color: q0")
    plt.show()


def plot_toy_hopf_curve(N=1000):
    """Plot a toy knotted curve reminiscent of a Hopf-type object."""
    t = np.linspace(0, 2 * np.pi, N)
    x = np.cos(t)
    y = np.sin(t)
    z = np.sin(2 * t)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z, color="red", linewidth=2)
    plt.title("Toy Hopf-like curve in R^3")
    plt.show()


def main():
    N = 1000
    Q = generate_Q_field(N)
    plot_Q_projection(Q)
    plot_toy_hopf_curve(N)


if __name__ == "__main__":
    main()
