def find_fibonacci_with_n_digits(target_digits: int) -> int:
    """
    주어진 자릿수를 가진 첫 번째 피보나치 수의 인덱스를 찾습니다.
    
    매개변수:
        target_digits: 찾고자 하는 자릿수 (예: 1000)
    
    반환값:
        첫 번째로 target_digits 자릿수를 가진 피보나치 항의 인덱스
    """
    # TODO: 첫 두 피보나치 수 초기화
    # 힌트: fib1 = 1, fib2 = 1로 시작하고, index = 2
    fib1, fib2 = 1, 1
    index = 2
    
    # TODO: 현재 피보나치 수가 목표 자릿수에 도달할 때까지 반복
    # 힌트: while len(str(fib2)) < target_digits:
    while len(str(fib2)) < target_digits:
        # TODO: 다음 피보나치 수 계산
        # 힌트: fib1과 fib2를 업데이트하는 것을 잊지 마세요!
        fib1, fib2 = fib2, fib1 + fib2
        index += 1
    
    # TODO: 인덱스 반환
    return index
