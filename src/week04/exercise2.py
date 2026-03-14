from __future__ import annotations

import pennylane as qml
from pennylane.tape import make_qscript


def superdense_circuit(a1: int, a2: int) -> object:
    """PennyLane quantum function for superdense coding with two message bits."""
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

    if a1 == 1:
        qml.PauliZ(wires=0)
    if a2 == 1:
        qml.PauliX(wires=0)

    qml.CNOT(wires=[0, 1])
    qml.Hadamard(wires=0)

    return qml.sample(wires=[0, 1])


def export_superdense_to_qasm(a1: int, a2: int) -> str:
    """Export the PennyLane superdense circuit to OPENQASM 2.0 text."""
    qscript = make_qscript(superdense_circuit)(a1, a2)
    qasm_str = qml.to_openqasm(qscript)
    return str(qasm_str)


def exercise2() -> None:
    """Run Exercise 2 with sample message bits and print OPENQASM 2.0 output."""
    qasm_str = export_superdense_to_qasm(1, 1)
    print(qasm_str)  # noqa: T201


if __name__ == "__main__":
    exercise2()
