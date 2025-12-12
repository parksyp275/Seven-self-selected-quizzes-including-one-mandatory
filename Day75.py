def find_greatest_product(number_string: str, window_size: int) -> int:
    """
    긴 숫자 문자열에서 연속된 window_size개 숫자의 곱이 최대인 값을 찾습니다.
    
    Args:
        number_string: 분석할 숫자 문자열 (개행 문자 포함 가능)
        window_size: 연속해서 곱할 숫자의 개수
    
    Returns:
        최대 곱의 값
    """
    # TODO: 문자열에서 개행 문자와 공백 제거
    clean_string = number_string.replace('\n', '').replace(' ', '')

    # TODO: window_size보다 짧으면 에러 처리
    if len(clean_string) < window_size:
        raise ValueError("Window size cannot be larger than the string length.")

    # TODO: 최댓값을 저장할 변수 초기화
    max_product = 0

    # TODO: 가능한 모든 구간을 확인하는 반복문
    for i in range(len(clean_string) - window_size + 1):
        
        # TODO: 각 구간의 숫자들을 곱하기
        current_product = 1
        for char in clean_string[i : i + window_size]:
            current_product *= int(char)
        
        # TODO: 최댓값 업데이트
        if current_product > max_product:
            max_product = current_product

    # TODO: 최댓값 반환
    return max_product


def find_greatest_product_with_details(number_string: str, window_size: int) -> dict:
    """
    최대 곱뿐만 아니라 어떤 숫자들이었는지도 반환합니다.
    
    Returns:
        딕셔너리: {
            'product': 최대 곱,
            'digits': 해당 숫자들의 리스트,
            'position': 시작 위치
        }
    """
    # TODO: 기본 함수와 유사하지만 추가 정보도 저장
    clean_string = number_string.replace('\n', '').replace(' ', '')
    
    if len(clean_string) < window_size:
        raise ValueError("Window size cannot be larger than the string length.")

    best_result = {
        'product': 0,
        'digits': [],
        'position': 0
    }

    for i in range(len(clean_string) - window_size + 1):
        current_product = 1
        current_digits = []
        
        # 현재 윈도우의 숫자들을 곱하고 리스트에 저장
        for char in clean_string[i : i + window_size]:
            digit = int(char)
            current_product *= digit
            current_digits.append(digit)
        
        # 최댓값 발견 시 정보 업데이트
        if current_product > best_result['product']:
            best_result['product'] = current_product
            best_result['digits'] = current_digits
            best_result['position'] = i
            
    return best_result
