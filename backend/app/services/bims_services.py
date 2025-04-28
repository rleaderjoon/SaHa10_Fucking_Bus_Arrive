"""
TIP
가상환경 활성화 코드
source .venv/bin/activate
"""

import requests
from typing import List, Dict, Any, Optional
from app.core.config import settings
from app.utils.xml_parser import parse_bims_xml

# TODO: BIMS API 기본 URL 설정 (문서 확인 필요)
BIMS_BASE_URL = "http://data.busan.go.kr/openBusDataService/..." # 실제 URL로 변경

def call_bims_api(endpoint: str, params: Dict[str, Any]) -> Optional[str]:
    """BIMS API를 호출하고 응답 텍스트를 반환합니다."""
    params['serviceKey'] = settings.BIMS_API_KEY # 공통 파라미터: 서비스 키 추가
    try:
        response = requests.get(f"{BIMS_BASE_URL}/{endpoint}", params=params, timeout=10) # 타임아웃 설정
        response.raise_for_status() # 오류 발생 시 예외 발생 (4xx, 5xx)
        # TODO: API 응답 인코딩 확인 및 처리 (예: euc-kr -> utf-8 변환 필요 시)
        # response.encoding = 'euc-kr' # 만약 EUC-KR이라면
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"BIMS API 호출 오류 ({endpoint}): {e}")
        # TODO: 오류 로깅 및 예외 처리 강화
        return None

def get_bus_arrival_list(station_id: str, line_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """특정 정류소의 버스 도착 정보를 조회합니다."""
    endpoint = "getBusArriveList" # TODO: 실제 엔드포인트 명칭 확인
    params = {
        "bstopid": station_id,
        # "lineid": line_id, # line_id가 있으면 특정 노선만 필터링 (API 명세 확인)
        # TODO: API 명세에 따른 추가 파라미터 ( numOfRows, pageNo 등)
    }
    if line_id:
        params["lineid"] = line_id

    xml_response = call_bims_api(endpoint, params)
    if xml_response:
        # TODO: getBusArriveList 응답에서 필요한 필드 이름 리스트 정의
        required_fields = ['arrTime', 'busNo', 'lowPlate', 'lineId', 'stationId'] # 예시 필드명, 실제 명칭으로 수정!
        return parse_bims_xml(xml_response, required_fields)
    return []

def get_bus_line_info(line_id: str) -> List[Dict[str, Any]]:
    """특정 버스 노선 정보를 조회합니다."""
    endpoint = "getBusLneInfoIem" # TODO: 실제 엔드포인트 명칭 확인
    params = {"lineid": line_id}
    # TODO: API 명세에 따른 추가 파라미터

    xml_response = call_bims_api(endpoint, params)
    if xml_response:
        # TODO: getBusLneInfoIem 응답에서 필요한 필드 이름 리스트 정의
        required_fields = ['lineNo', 'firstTime', 'lastTime'] # 예시 필드명, 실제 명칭으로 수정!
        return parse_bims_xml(xml_response, required_fields)
    return []

def get_bus_line_stops(line_id: str) -> List[Dict[str, Any]]:
    """특정 버스 노선의 경유 정류소 목록을 조회합니다."""
    endpoint = "getBusLneStopList" # TODO: 실제 엔드포인트 명칭 확인
    params = {"lineid": line_id}
    # TODO: API 명세에 따른 추가 파라미터

    xml_response = call_bims_api(endpoint, params)
    if xml_response:
        # TODO: getBusLneStopList 응답에서 필요한 필드 이름 리스트 정의
        required_fields = ['bstopId', 'bstopNm', 'stoptype'] # 예시 필드명, 실제 명칭으로 수정!
        return parse_bims_xml(xml_response, required_fields)
    return []