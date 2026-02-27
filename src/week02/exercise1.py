import sympy as sp


def exercise1():
    """Goal: Verify and fix normalization of a symbolic qubit state.

    Define a symbolic qubit state  |𝜓⟩=𝛼|0⟩+𝛽|1⟩ .
    Check whether  |𝜓⟩  is normalized. If not, normalize it to get a new state  |𝜓′⟩ .
    Verify that  |𝜓′⟩  has norm 1.
    Hint (click to expand)
    Import sympy and create symbolic variables for  𝛼  and  𝛽 .
    Construct the qubit vector in terms of  𝛼  and  𝛽 .
    Compute the norm  |||𝜓⟩||2=⟨𝜓|𝜓⟩ .
    If this norm is not 1, define  |𝜓′⟩=|𝜓⟩⟨𝜓|𝜓⟩√ .
    Confirm that  |𝜓′⟩  is normalized.
    """
    ket_0 = sp.Matrix([1, 0])
    ket_1 = sp.Matrix([0, 1])

    # Step 1: Define symbolic variables
    alpha, beta = sp.symbols("alpha beta", complex=True)

    # Step 2: Construct the qubit state |ψ⟩
    psi = alpha * ket_0 + beta * ket_1

    # Step 3: Compute the norm |||ψ⟩||^2 = ⟨ψ|ψ⟩
    norm_squared_scalar = (psi.H * psi)[0]  # Extract scalar from 1x1 Matrix

    # Step 4: Normalize (심볼릭에서는 if 비교 대신 항상 정의하는 게 안전)
    psi_prime = sp.simplify(psi / sp.sqrt(norm_squared_scalar))

    # Step 6: Verify that |ψ'⟩ is normalized
    norm_prime_squared = sp.simplify((psi_prime.H * psi_prime)[0])

    print("Original state |ψ⟩: ")
    sp.pprint(psi)
    print("Norm squared of |ψ⟩: ")
    sp.pprint(norm_squared_scalar)
    print("Normalized state |ψ'⟩: ")
    sp.pprint(psi_prime)
    print("Norm squared of |ψ'⟩: ")
    sp.pprint(norm_prime_squared)


if __name__ == "__main__":
    exercise1()
