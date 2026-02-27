import os
import sys

import matplotlib.pyplot as plt

# Add project root to sys.path for direct script execution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.lib.quokka import send_to_quokka


def exercise5(N=1000):
    """Goal: QASM-based quantum random number generator (QRNG), plot histogram of output bits.

    Uses Quokka simulator to run QASM 2.0 code and collect N random bits.
    """
    # 1. QASM 2.0 프로그램 작성 (Hadamard -> 측정)
    qasm_code = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
h q[0];
measure q[0] -> c[0];
"""

    # 2. Quokka 시뮬레이터에 N번 실행 요청
    # send_to_quokka는 count=1이 기본이므로, N번 반복 호출
    results = []
    for _ in range(N):
        bits = send_to_quokka(qasm_code)
        # bits는 예: [[0]] 또는 [[1]]
        results.append(bits[0][0])

    # 3. 결과 집계 및 히스토그램 플롯
    count_0 = results.count(0)
    count_1 = results.count(1)
    print(f"Measurement outcomes: 0: {count_0}, 1: {count_1}")
    plt.bar([0, 1], [count_0, count_1], tick_label=["0", "1"])
    plt.xlabel("Bit value")
    plt.ylabel("Counts")
    plt.title(f"QRNG outcomes for N={N}")
    plt.text(0, count_0, str(count_0), ha="center", va="bottom")
    plt.text(1, count_1, str(count_1), ha="center", va="bottom")
    plt.show()


if __name__ == "__main__":
    exercise5()
