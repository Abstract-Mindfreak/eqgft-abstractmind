"""
Minimal lattice demo for the EQGFT rotor field Q(x).

This is NOT a full physical simulation. It is a toy model that:
- represents Q(x) on a 3D lattice as normalized 4-vectors (q0, q1, q2, q3),
- enforces the constraint Q† Q = 1 by renormalizing after each update,
- defines a simple nearest-neighbor energy ~ sum (dQ)^2,
- performs a few gradient-descent-like relaxation steps.

Intended as a starting point / scaffolding for future EQGFT lattice work.
"""

from __future__ import annotations

import numpy as np

Array = np.ndarray


def random_unit_quaternion(shape) -> Array:
    """Generate a field of random unit quaternions as 4D vectors.

    Parameters
    ----------
    shape : tuple[int, int, int]
        Lattice shape (Nx, Ny, Nz).

    Returns
    -------
    ndarray
        Array with shape (Nx, Ny, Nz, 4) of normalized quaternions.
    """
    q = np.random.normal(size=(*shape, 4))
    norm = np.linalg.norm(q, axis=-1, keepdims=True)
    return q / norm


def normalize_field(Q: Array) -> Array:
    """Enforce Q† Q = 1 pointwise by normalizing each 4-vector."""
    norm = np.linalg.norm(Q, axis=-1, keepdims=True)
    # avoid division by zero
    norm = np.where(norm == 0.0, 1.0, norm)
    return Q / norm


def laplacian_3d(Q: Array) -> Array:
    """Discrete 3D Laplacian with periodic boundary conditions.

    Parameters
    ----------
    Q : ndarray
        Field with shape (Nx, Ny, Nz, 4).

    Returns
    -------
    ndarray
        Discrete Laplacian of Q with the same shape.
    """
    # roll in each spatial direction (periodic BCs)
    Qx_p = np.roll(Q, shift=-1, axis=0)
    Qx_m = np.roll(Q, shift=+1, axis=0)
    Qy_p = np.roll(Q, shift=-1, axis=1)
    Qy_m = np.roll(Q, shift=+1, axis=1)
    Qz_p = np.roll(Q, shift=-1, axis=2)
    Qz_m = np.roll(Q, shift=+1, axis=2)

    lap = (Qx_p + Qx_m + Qy_p + Qy_m + Qz_p + Qz_m - 6.0 * Q)
    return lap


def energy_density(Q: Array) -> Array:
    """Simple nearest-neighbor gradient energy density ~ |∇Q|^2.

    This is not the full EQGFT action, but a standard rotor / sigma-model-like term.
    """
    # forward differences with periodic BCs
    dQx = np.roll(Q, -1, axis=0) - Q
    dQy = np.roll(Q, -1, axis=1) - Q
    dQz = np.roll(Q, -1, axis=2) - Q

    ed = 0.5 * (
        np.sum(dQx**2, axis=-1)
        + np.sum(dQy**2, axis=-1)
        + np.sum(dQz**2, axis=-1)
    )
    return ed


def total_energy(Q: Array) -> float:
    """Total gradient energy of the field."""
    return float(np.sum(energy_density(Q)))


def relax_field(
    Q: Array,
    num_steps: int = 100,
    dt: float = 0.05,
    M2: float = 1.0,
    verbose: bool = True,
) -> Array:
    """Toy gradient-descent-like relaxation for the rotor field.

    We use a discretized equation of motion of the form
        Q_{t+1} = Q_t - dt * M^2 * Laplacian(Q_t),
    followed by pointwise renormalization of Q.

    Parameters
    ----------
    Q : ndarray
        Initial field configuration, shape (Nx, Ny, Nz, 4).
    num_steps : int
        Number of relaxation steps.
    dt : float
        Time step (controls stability and speed).
    M2 : float
        Effective stiffness parameter (analog of M^2 in the action).
    verbose : bool
        If True, print energy every ~10 steps.

    Returns
    -------
    ndarray
        Relaxed field with the same shape as Q.
    """
    Q = normalize_field(Q)
    for step in range(num_steps):
        lap = laplacian_3d(Q)
        Q = Q - dt * M2 * lap
        Q = normalize_field(Q)

        if verbose and (step % max(1, num_steps // 10) == 0 or step == num_steps - 1):
            print(f"step {step+1:4d} / {num_steps:4d} | E = {total_energy(Q):.6e}")

    return Q


def main():
    # small demo lattice
    Nx = Ny = Nz = 16
    Q = random_unit_quaternion((Nx, Ny, Nz))

    print("Initial energy:", total_energy(Q))
    Q_relaxed = relax_field(Q, num_steps=50, dt=0.05, M2=1.0, verbose=True)
    print("Final energy:", total_energy(Q_relaxed))


if __name__ == "__main__":
    main()
