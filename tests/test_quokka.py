"""
Tests for lib.quokka.send_to_quokka function
"""
import pytest
from unittest.mock import Mock, patch
from lib.quokka import send_to_quokka


class TestSendToQuokka:
    """send_to_quokka 함수 테스트"""

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_success(self, mock_post):
        """정상적인 QASM 프로그램 전송 테스트"""
        # Mock 응답 설정
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[1]]}}'
        mock_post.return_value = mock_response

        # 테스트 실행
        result = send_to_quokka("test program")

        # 검증
        mock_post.assert_called_once()
        assert mock_post.call_args[0][0].startswith('http://quokka1.quokkacomputing.com/qsim/qasm')
        assert mock_post.call_args[1]['json']['script'] == "test program"
        assert mock_post.call_args[1]['json']['count'] == 1
        assert result == [[1]]

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_with_custom_quokka(self, mock_post):
        """다른 Quokka 서버 사용 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[0]]}}'
        mock_post.return_value = mock_response

        # 커스텀 Quokka 서버로 테스트
        result = send_to_quokka("test program", my_quokka="quokka2")

        # 검증
        mock_post.assert_called_once()
        assert mock_post.call_args[0][0].startswith('http://quokka2.quokkacomputing.com/qsim/qasm')

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_network_error(self, mock_post):
        """네트워크 오류 시나리오 테스트"""
        mock_post.side_effect = Exception("Network error")

        # 테스트 실행 시 예외 발생 확인
        with pytest.raises(Exception) as exc_info:
            send_to_quokka("test program")

        assert "Network error" in str(exc_info.value)

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_with_x_gate(self, mock_post):
        """X 게이트가 포함된 QASM 프로그램 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[1]]}}'
        mock_post.return_value = mock_response

        # X 게이트가 포함된 QASM 프로그램
        qasm_with_x = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
x q[0];
measure q[0] -> c[0];
"""

        result = send_to_quokka(qasm_with_x)

        # 검증
        assert "x q[0]" in mock_post.call_args[1]['json']['script']
        assert result == [[1]]

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_with_h_gate(self, mock_post):
        """H 게이트(Hadamard)가 포함된 QASM 프로그램 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[0]]}}'
        mock_post.return_value = mock_response

        # H 게이트가 포함된 QASM 프로그램
        qasm_with_h = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
h q[0];
measure q[0] -> c[0];
"""

        result = send_to_quokka(qasm_with_h)

        # 검증
        assert "h q[0]" in mock_post.call_args[1]['json']['script']
        assert result == [[0]]

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_with_multiple_gates(self, mock_post):
        """여러 게이트가 포함된 QASM 프로그램 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[0]]}}'
        mock_post.return_value = mock_response

        # 여러 게이트가 포함된 QASM 프로그램
        qasm_multi = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
h q[0];
x q[0];
z q[0];
measure q[0] -> c[0];
"""

        result = send_to_quokka(qasm_multi)

        # 검증
        assert "h q[0]" in mock_post.call_args[1]['json']['script']
        assert "x q[0]" in mock_post.call_args[1]['json']['script']
        assert "z q[0]" in mock_post.call_args[1]['json']['script']

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_with_multiple_qubits(self, mock_post):
        """여러 큐비트를 사용하는 QASM 프로그램 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[0, 1]]}}'
        mock_post.return_value = mock_response

        # 여러 큐비트를 사용하는 QASM 프로그램
        qasm_multi_qubits = """
OPENQASM 2.0;
qreg q[2];
creg c[2];
h q[0];
cx q[0], q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
"""

        result = send_to_quokka(qasm_multi_qubits)

        # 검증
        assert "qreg q[2]" in mock_post.call_args[1]['json']['script']
        assert "cx q[0], q[1]" in mock_post.call_args[1]['json']['script']

    @patch('lib.quokka.requests.post')
    def test_send_to_quokka_empty_program(self, mock_post):
        """빈 QASM 프로그램 테스트"""
        mock_response = Mock()
        mock_response.content = b'{"result": {"c": [[0]]}}'
        mock_post.return_value = mock_response

        # 빈 프로그램 (기본값만 있는 경우)
        empty_qasm = """
OPENQASM 2.0;
qreg q[1];
creg c[1];
measure q[0] -> c[0];
"""

        result = send_to_quokka(empty_qasm)

        # 검증
        mock_post.assert_called_once()
        assert "measure q[0] -> c[0]" in mock_post.call_args[1]['json']['script']
        assert result == [[0]]
