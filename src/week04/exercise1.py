from __future__ import annotations

import json

import cirq
import requests

MIN_RECEIVED_BITS = 2


def superdense_coding_cirq(a1: int, a2: int, quokka_host: str = "quokka1") -> tuple[int, int]:
    """Encode two classical bits with Cirq superdense coding and run on Quokka."""
    alice = cirq.NamedQubit("alice")
    bob = cirq.NamedQubit("bob")
    superdense = cirq.Circuit()

    # Bell pair preparation.
    superdense.append([cirq.H(alice), cirq.CNOT(alice, bob)])

    # Alice encodes classical bits on her qubit.
    if a1 == 1:
        superdense.append(cirq.Z(alice))
    if a2 == 1:
        superdense.append(cirq.X(alice))

    # Bob decodes and measures.
    superdense.append([cirq.CNOT(alice, bob), cirq.H(alice)])
    superdense.append(cirq.measure(alice, bob, key="m_received"))

    qasm_program = cirq.qasm(superdense)
    request_http = f"http://{quokka_host}.quokkacomputing.com/qsim/qasm"
    payload = {"script": qasm_program, "count": 1}

    response = requests.post(
        request_http,
        json=payload,
        verify=False,  # noqa: S501
        timeout=30,
    )
    response.raise_for_status()
    json_obj = json.loads(response.content)

    measured: list[int] | None = None
    if "result" in json_obj and "m_received" in json_obj["result"]:
        measured = json_obj["result"]["m_received"][0]
    elif "result" in json_obj and "c" in json_obj["result"]:
        measured = json_obj["result"]["c"][0]

    if measured is None or len(measured) < MIN_RECEIVED_BITS:
        message = f"Unexpected Quokka response: {json_obj}"
        raise ValueError(message)

    bob_received = (int(measured[0]), int(measured[1]))
    print(f"Bob received bits: {bob_received[0]} {bob_received[1]}")  # noqa: T201
    return bob_received


def exercise1() -> None:
    """Run Exercise 1 with example input bits (1, 0)."""
    superdense_coding_cirq(1, 0)


if __name__ == "__main__":
    exercise1()
