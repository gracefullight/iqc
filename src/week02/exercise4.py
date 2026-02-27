import sympy as sp


# Helper function: compute norm squared of a state vector
def norm2(v):
    return sp.simplify((v.H * v)[0])


def exercise4():
    """Goal: Apply Z, X, H gates in sequence and track the state.

    Start with |ψ⟩ = 1/√2 (|0⟩ + i|1⟩)
    Apply Z, then X, then H. Check state and normalization after each.
    """
    # 1. Define computational basis vectors |0⟩ and |1⟩
    ket_0 = sp.Matrix([1, 0])
    ket_1 = sp.Matrix([0, 1])
    i = sp.I
    sqrt2 = sp.sqrt(2)

    # 2. Define the initial state |ψ⟩ = 1/√2 (|0⟩ + i|1⟩)
    psi = (ket_0 + i * ket_1) / sqrt2
    print("Initial state |ψ⟩:")
    sp.pprint(psi)

    # 3. Apply Z gate: Z = diag(1, -1)
    Z = sp.Matrix([[1, 0], [0, -1]])
    psi_z = Z * psi
    print("After Z gate:")
    sp.pprint(psi_z)
    print("Norm squared after Z:", norm2(psi_z))

    # 4. Apply X gate: X = [[0, 1], [1, 0]]
    X = sp.Matrix([[0, 1], [1, 0]])
    psi_x = X * psi_z
    print("After X gate:")
    sp.pprint(psi_x)
    print("Norm squared after X:", norm2(psi_x))

    # 5. Apply H gate: H = (1/√2) * [[1, 1], [1, -1]]
    H = (1 / sqrt2) * sp.Matrix([[1, 1], [1, -1]])
    psi_h = H * psi_x
    print("After H gate:")
    sp.pprint(psi_h)
    print("Norm squared after H:", norm2(psi_h))


if __name__ == "__main__":
    exercise4()
