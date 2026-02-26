"""
Quokka quantum simulator client module

Quokka 시뮬레이터와 연동하여 QASM 프로그램을 실행하는 함수를 제공합니다.
"""

import json
import requests


def send_to_quokka(program: str, my_quokka: str = "quokka1"):
    """
    QASM 프로그램을 Quokka 시뮬레이터로 전송하는 함수

    Args:
        program: QASM 형식의 양자 프로그램 문자열
        my_quokka: 사용할 Quokka 서버 (기본값: 'quokka1')

    Returns:
        측정 결과 (클래식 비트 리스트)
    """
    # 단계 1: 서버 주소 정의
    request_http = f"http://{my_quokka}.quokkacomputing.com/qsim/qasm"

    # 단계 2: 전송할 데이터 준비
    data = {"script": program, "count": 1}

    # 단계 3: POST 요청 전송
    result = requests.post(request_http, json=data, verify=False)

    # 단계 4: 응답을 Python 사전으로 변환
    json_obj = json.loads(result.content)

    # 결과 반환
    return json_obj["result"]["c"]
