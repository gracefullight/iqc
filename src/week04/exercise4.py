from __future__ import annotations

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import MCXGate


def mcx_gate_counts(min_controls: int = 2, max_controls: int = 15) -> tuple[list[int], list[int]]:
    """Return total transpiled gate counts for MCXGate as controls increase."""
    control_counts: list[int] = []
    total_gate_counts: list[int] = []

    for n_controls in range(min_controls, max_controls + 1):
        gate = MCXGate(n_controls)
        circuit = QuantumCircuit(n_controls + 1)
        circuit.append(gate, list(range(n_controls + 1)))

        compiled = transpile(circuit, basis_gates=["u", "cx"])
        total_gates = sum(compiled.count_ops().values())

        control_counts.append(n_controls)
        total_gate_counts.append(total_gates)

    return control_counts, total_gate_counts


def plot_mcx_gate_counts(control_counts: list[int], total_gate_counts: list[int]) -> None:
    """Plot total gate count versus number of MCX control qubits."""
    plt.figure(figsize=(8, 5))
    plt.plot(control_counts, total_gate_counts, marker="o")
    plt.title("MCXGate Total Gate Count vs Number of Control Qubits")
    plt.xlabel("Number of control qubits")
    plt.ylabel("Total gates after transpile (basis: u, cx)")
    plt.grid(visible=True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def exercise4() -> None:
    """Run Exercise 4: MCX transpilation gate-count scaling study."""
    control_counts, total_gate_counts = mcx_gate_counts(2, 15)

    plot_mcx_gate_counts(control_counts, total_gate_counts)


if __name__ == "__main__":
    exercise4()
