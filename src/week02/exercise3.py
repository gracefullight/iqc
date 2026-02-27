import sympy as sp


def exercise3():
    """Goal: Convert Bloch-sphere angles to vector form and verify normalization.

    |ψ⟩ = cos(θ)|0⟩ + e^{iφ}sin(θ)|1⟩
    Substitute θ=π/6, φ=π/3 and check norm.
    """
    # 1. Define computational basis vectors |0⟩ and |1⟩
    ket_0 = sp.Matrix([1, 0])
    ket_1 = sp.Matrix([0, 1])

    # 2. Declare symbolic real parameters θ (theta), φ (phi)
    theta, phi = sp.symbols("theta phi", real=True)

    # 3. Construct the general qubit state on the Bloch sphere
    #    |ψ⟩ = cos(θ)|0⟩ + exp(iφ)sin(θ)|1⟩
    psi = sp.cos(theta) * ket_0 + sp.exp(sp.I * phi) * sp.sin(theta) * ket_1
    print("Symbolic state |ψ⟩ (Bloch form):")
    sp.pprint(psi)

    # 4. Compute and print the symbolic norm squared (should be 1 for all real θ, φ)
    norm2 = (psi.H * psi)[0]
    print("Norm squared (symbolic, before substitution):")
    sp.pprint(sp.simplify(norm2))

    # 5. Substitute specific values for θ and φ, e.g., θ=π/6, φ=π/3
    vals = {theta: sp.pi / 6, phi: sp.pi / 3}
    psi_num = psi.subs(vals).evalf()
    print("State with θ=π/6, φ=π/3:")
    sp.pprint(psi_num)

    # 6. Compute and print the norm squared for the substituted state
    norm2_num = (psi_num.H * psi_num)[0]
    print(f"Norm squared (numeric, after substitution): {norm2_num}")


if __name__ == "__main__":
    exercise3()
