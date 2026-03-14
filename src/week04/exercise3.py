from __future__ import annotations

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.circuit.library import CUGate


def build_decomposed_cu_circuit() -> object:
    """Build and decompose a parameterized 2-qubit CU circuit."""
    theta = Parameter("theta")
    phi = Parameter("phi")
    lam = Parameter("lam")
    gamma = Parameter("gamma")

    cu = CUGate(theta, phi, lam, gamma)
    cu_circuit = QuantumCircuit(2)
    cu_circuit.append(cu, [0, 1])

    return cu_circuit.decompose()


def exercise3() -> None:
    """Run Exercise 3 and display the decomposed CU circuit diagram."""
    decomposed = build_decomposed_cu_circuit()
    print(decomposed.draw(output="text"))  # noqa: T201


if __name__ == "__main__":
    exercise3()
