import sympy as sp
from sympy import pprint

from lib.quokka import send_to_quokka


def cell_1_vector() -> sp.Matrix:
    """코드 셀 1: 벡터 (ket) 정의."""
    psi_0, psi_1 = sp.symbols("psi_0 psi_1")
    ket_psi = sp.Matrix([psi_0, psi_1])

    print("=" * 60)
    print("코드 셀 1: 벡터 (ket) 정의")
    print("=" * 60)
    print("|ψ⟩ =", ket_psi)

    return ket_psi


def cell_2_basis_states(ket_0: sp.Matrix, ket_1: sp.Matrix) -> sp.Matrix:
    """코드 셀 2: basis states와 ket_phi 정의."""
    phi_0, phi_1 = sp.symbols("phi_0 phi_1")
    ket_phi = phi_0 * ket_0 + phi_1 * ket_1

    print("\n" + "=" * 60)
    print("코드 셀 2: Basis states와 ket_phi")
    print("=" * 60)
    print("φ₀|0⟩ + φ₁|1⟩ =")
    pprint(ket_phi)

    return ket_phi


def cell_3_matrix() -> sp.Matrix:
    """코드 셀 3: 일반 2x2 행렬 정의."""
    a00, a01, a10, a11 = sp.symbols("a00 a01 a10 a11")
    A = sp.Matrix([[a00, a01], [a10, a11]])

    print("\n" + "=" * 60)
    print("코드 셀 3: 일반 2x2 행렬")
    print("=" * 60)
    print("A =")
    pprint(A)

    return A


def cell_4_identity_matrix(ket_psi: sp.Matrix, I: sp.Matrix) -> None:
    """코드 셀 4: 항등 행렬 (Identity Matrix)."""
    I_psi = I * ket_psi
    I_squared = I * I

    print("\n" + "=" * 60)
    print("코드 셀 4: 항등 행렬 검증")
    print("=" * 60)
    print("I|ψ⟩ =")
    pprint(I_psi)
    print("I² =")
    pprint(I_squared)


def cell_5_inverse(A: sp.Matrix) -> None:
    """코드 셀 5: 행렬의 역행렬."""
    A_inverse = A.inv()

    print("\n" + "=" * 60)
    print("코드 셀 5: 역행렬")
    print("=" * 60)
    print("A⁻¹ =")
    pprint(A_inverse)

    A_times_A_inverse = A * A_inverse
    A_times_A_inverse_simplified = sp.simplify(A_times_A_inverse)

    print("AA⁻¹ =")
    pprint(A_times_A_inverse_simplified)


def cell_6_conjugate_transpose(ket_psi: sp.Matrix, A: sp.Matrix) -> None:
    """코드 셀 6: 켤레 전치 (Conjugate Transpose)."""
    psi_dagger = ket_psi.H
    A_dagger = A.H

    print("\n" + "=" * 60)
    print("코드 셀 6: 켤레 전치")
    print("=" * 60)
    print("|ψ⟩† =")
    pprint(psi_dagger)
    print("A† =")
    pprint(A_dagger)


def cell_7_hermitian(A: sp.Matrix) -> None:
    """코드 셀 7: 에르미션 행렬 검증."""
    AA_dagger = A * A.H
    is_hermitian = AA_dagger.is_hermitian

    print("\n" + "=" * 60)
    print("코드 셀 7: 에르미션 행렬 검증")
    print("=" * 60)
    print(f"AA† 에르미션 행렬?: {is_hermitian}")


def cell_8_rotation_matrix(I: sp.Matrix) -> None:
    """코드 셀 8: 회전 행렬의 유니타리 검증."""
    theta = sp.symbols("theta", real=True)
    U = sp.Matrix([[sp.cos(theta), sp.sin(theta)], [-sp.sin(theta), sp.cos(theta)]])

    U_dagger_U = U.H * U
    U_dagger_U_simplified = sp.trigsimp(U_dagger_U)
    is_unitary = U_dagger_U_simplified == I

    print("\n" + "=" * 60)
    print("코드 셀 8: 회전 행렬의 유니타리 검증")
    print("=" * 60)
    print(f"U 유니타리?: {is_unitary}")


def cell_9_inner_product(ket_psi: sp.Matrix, ket_phi: sp.Matrix) -> sp.Matrix:
    """코드 셀 9: 내적 (Inner Product)."""
    inner_product = ket_psi.H * ket_phi

    print("\n" + "=" * 60)
    print("코드 셀 9: 내적")
    print("=" * 60)
    print(f"|φ⟩의 형태: {ket_phi.shape}")
    print(f"내적 ⟨ψ|φ⟩의 형태: {inner_product.shape}")

    print("⟨ψ|φ⟩ =")
    pprint(inner_product[0])

    return inner_product


def cell_10_inner_product_order(
    ket_psi: sp.Matrix, ket_phi: sp.Matrix
) -> tuple[sp.Matrix, sp.Matrix]:
    """코드 셀 10: 내적의 순서."""
    inner_product_psi_phi = ket_psi.H * ket_phi
    inner_product_phi_psi = ket_phi.H * ket_psi

    print("\n" + "=" * 60)
    print("코드 셀 10: 내적의 순서")
    print("=" * 60)

    are_equal = sp.simplify(inner_product_psi_phi - inner_product_phi_psi) == 0

    print(f"⟨ψ|φ⟩ = ⟨φ|ψ⟩?: {are_equal}")

    return inner_product_psi_phi, inner_product_phi_psi


def cell_11_complex_magnitude_left(inner_product_psi_phi: sp.Matrix) -> sp.Expr:
    """코드 셀 11: 복소수 크기 (왼쪽)."""
    leftside = sp.sqrt(sp.simplify(inner_product_psi_phi * inner_product_psi_phi.H))
    leftside = leftside.expand(complex=True)

    print("\n" + "=" * 60)
    print("코드 셀 11: 복소수 크기 (왼쪽)")
    print("=" * 60)
    print("|⟨ψ|φ⟩| =")
    pprint(leftside)

    return leftside


def cell_12_complex_magnitude_right(inner_product_phi_psi: sp.Matrix, leftside: sp.Expr) -> None:
    """코드 셀 12: 복소수 크기 (오른쪽)."""
    rightside = sp.sqrt(sp.simplify(inner_product_phi_psi * inner_product_phi_psi.H))
    rightside = rightside.expand(complex=True)

    print("\n" + "=" * 60)
    print("코드 셀 12: 복소수 크기 (오른쪽)")
    print("=" * 60)
    print(f"왼쪽 = 오른쪽?: {leftside == rightside}")


def cell_13_magnitude(ket_psi: sp.Matrix) -> None:
    """코드 셀 13: 크기 (Magnitude)."""
    inner_product_psi_psi = ket_psi.H * ket_psi

    print("\n" + "=" * 60)
    print("코드 셀 13: 벡터의 크기")
    print("=" * 60)
    print("||ψ⟩||² =")
    pprint(inner_product_psi_psi[0])


def cell_14_outer_product(ket_0: sp.Matrix, ket_1: sp.Matrix) -> None:
    """코드 셀 14: 외적 (Outer Product)."""
    outer_product_0_1 = ket_0 * ket_1.H
    outer_product_1_0 = ket_1 * ket_0.H

    print("\n" + "=" * 60)
    print("코드 셀 14: 외적")
    print("=" * 60)
    print("|0⟩⟨1| =")
    pprint(outer_product_0_1)
    print("|1⟩⟨0| =")
    pprint(outer_product_1_0)


def cell_15_qubit_normalization(ket_0: sp.Matrix, ket_1: sp.Matrix) -> tuple:
    """코드 셀 15: 큐비트 상태와 정규화."""
    theta, phi = sp.symbols("theta phi", real=True)

    qubit_state = sp.cos(theta / 2) * ket_0 + sp.exp(sp.I * phi) * sp.sin(theta / 2) * ket_1

    norm = (qubit_state.H * qubit_state)[0, 0]
    is_normalized = sp.simplify(norm) == 1

    print("\n" + "=" * 60)
    print("코드 셀 15: 큐비트 상태 정규화")
    print("=" * 60)
    print(f"정규화됨?: {is_normalized}")

    return theta, phi


def cell_16_measurement_probability(theta, phi) -> None:
    """코드 셀 16: 측정 확률."""
    prob_0 = sp.simplify(sp.Abs(sp.cos(theta / 2)) ** 2)
    prob_1 = sp.simplify(sp.Abs(sp.sin(theta / 2)) ** 2)

    print("\n" + "=" * 60)
    print("코드 셀 16: 측정 확률")
    print("=" * 60)
    print(f"P(|0⟩) = {prob_0}")
    print(f"P(|1⟩) = {prob_1}")


def cell_17_pauli_x(I: sp.Matrix) -> None:
    """코드 셀 17: Pauli-X 게이트 검증."""
    X = sp.Matrix([[0, 1], [1, 0]])

    is_unitary = sp.simplify(X.H * X) == I

    print("\n" + "=" * 60)
    print("코드 셀 17: Pauli-X 게이트 검증")
    print("=" * 60)
    print(f"X 에르미션?: {X.is_hermitian}")
    print(f"X 유니타리?: {is_unitary}")


def cell_18_pauli_linear_combination(I: sp.Matrix) -> None:
    """코드 셀 18: Pauli 행렬의 선형 결합."""
    a, b, c = sp.symbols("a b c", real=True)

    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    L = a * I + b * X + c * Y

    print("\n" + "=" * 60)
    print("코드 셀 18: Pauli 행렬의 선형 결합")
    print("=" * 60)
    print(f"L 에르미션?: {L.is_hermitian}")


def cell_19_qasm_basic() -> str:
    """코드 셀 19: 기본 QASM 프로그램."""
    print("\n" + "=" * 60)
    print("Part 7: QASM와 Quokka 시뮬레이터")
    print("=" * 60)

    program = """
OPENQASM 2.0;
"""

    program += """
qreg q[1];
"""

    program += """
creg c[1];
"""

    print("기본 QASM 프로그램:")
    print(program)

    program += """
measure q[0] -> c[0];
"""

    print("측정 추가 후 QASM 프로그램:")
    print(program)

    return program


def cell_20_quokka_test(program: str) -> None:
    """코드 셀 20: Quokka 테스트."""
    try:
        result = send_to_quokka(program)
        print(f"\nQuokka 반환값 (|0⟩ 초기화 후 측정): {result}")
    except Exception as e:
        print(f"\nQuokka 연결 오류 (예상대로): {e}")
        print("(로컬 환경에서는 Quokka 서버에 연결할 수 없습니다.)")


def cell_21_x_gate() -> None:
    """코드 셀 21: X 게이트 (NOT 게이트) 추가."""
    program_x = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
x q[0];
measure q[0] -> c[0];
"""

    print("\n" + "=" * 60)
    print("X 게이트가 적용된 QASM 프로그램:")
    print("=" * 60)
    print(program_x)

    try:
        result_x = send_to_quokka(program_x)
        print(f"\nQuokka 반환값 (X 게이트 후 측정): {result_x}")
    except Exception as e:
        print(f"\nQuokka 연결 오류 (예상대로): {e}")


def quiz_answers(ket_0: sp.Matrix, ket_1: sp.Matrix, theta) -> None:
    """Quiz 정답 확인."""
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])

    print("\n" + "=" * 60)
    print("Quiz 정답 확인")
    print("=" * 60)

    print("Q1: True - |α|² + |β|² = 1 (양자 상태의 정규화 조건)")
    print("Q2: False - α와 β가 모두 0이 아니면 확률적으로 같은 결과")
    print("Q3: False - 전역 위상 e^(iγ)는 측정 확률에 영향을 준다")
    print("Q4: False - Bloch 구의 표면상의 점만 가능 (단위 벡터)")
    print("Q5: False - unitary 행렬만 양자 게이트로 유효")
    print("Q6: True - X 게이트는 |0⟩ ↔ |1⟩ 교환")
    print("Q7: True - 측정 시 상태가 기준 상태로 붕괴")
    print("Q8: True - unitary 행렬은 벡터의 규범을 보존")
    print("Q9: False - P(0) = cos²(θ/2), not cos²(θ)")

    state_10 = sp.Matrix([sp.Rational(1, 2), sp.sqrt(3) / 2])
    norm_10 = sp.simplify(state_10.H * state_10)[0]
    print(f"Q10: {norm_10 == 1} - norm = {norm_10}")

    alpha_11 = 1 / sp.sqrt(3)
    prob_0_11 = sp.simplify(sp.Abs(alpha_11) ** 2)
    print(f"Q11: {prob_0_11} = 1/3 ✓")

    phi_state = (ket_0 + ket_1) / sp.sqrt(2)
    chi_state = (ket_0 - ket_1) / sp.sqrt(2)
    orthogonality = sp.simplify(phi_state.H * chi_state)[0]
    print(f"Q12: {orthogonality == 0} - 내적 = {orthogonality}")

    X_squared = X * X
    print(f"Q13: {sp.simplify(X_squared) == Z} - X² =")
    pprint(X_squared)

    psi_14 = (ket_0 + sp.I * ket_1) / sp.sqrt(2)
    Z_psi = Z * psi_14
    expected_14 = (ket_0 - sp.I * ket_1) / sp.sqrt(2)
    print(f"Q14: 예상 결과와 일치: {sp.simplify(Z_psi - expected_14) == sp.Matrix([0, 0])}")

    print("Q15: X-Z-X = Z이므로 결과는 |1⟩이 아닌 |0⟩ - False")


def main() -> None:
    ket_0 = sp.Matrix([1, 0])
    ket_1 = sp.Matrix([0, 1])
    I = sp.eye(2)

    ket_psi = cell_1_vector()
    ket_phi = cell_2_basis_states(ket_0, ket_1)
    A = cell_3_matrix()
    cell_4_identity_matrix(ket_psi, I)
    cell_5_inverse(A)
    cell_6_conjugate_transpose(ket_psi, A)
    cell_7_hermitian(A)
    cell_8_rotation_matrix(I)
    cell_9_inner_product(ket_psi, ket_phi)
    inner_product_psi_phi, inner_product_phi_psi = cell_10_inner_product_order(ket_psi, ket_phi)
    leftside = cell_11_complex_magnitude_left(inner_product_psi_phi)
    cell_12_complex_magnitude_right(inner_product_phi_psi, leftside)
    cell_13_magnitude(ket_psi)
    cell_14_outer_product(ket_0, ket_1)
    theta, phi = cell_15_qubit_normalization(ket_0, ket_1)
    cell_16_measurement_probability(theta, phi)
    cell_17_pauli_x(I)
    cell_18_pauli_linear_combination(I)
    program = cell_19_qasm_basic()
    cell_20_quokka_test(program)
    cell_21_x_gate()
    quiz_answers(ket_0, ket_1, theta)

    print("\n" + "=" * 60)
    print("모든 코드 셀 실행 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
