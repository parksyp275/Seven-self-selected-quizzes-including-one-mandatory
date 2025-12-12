import random

def estimate_pi(num_samples: int) -> float:
    """
    Monte Carlo 시뮬레이션을 사용하여 π를 추정합니다.
    
    Args:
        num_samples: 던질 다트(샘플)의 개수
    
    Returns:
        π의 추정값 (float)
    """
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / num_samples)
    
    return pi_estimate

if __name__ == "__main__":
    # 테스트 1: 소규모 시뮬레이션
    print("=== 100번 시뮬레이션 ===")
    pi_estimate_1 = estimate_pi(100)
    print(f"추정된 π 값: {pi_estimate_1}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_1 - 3.14159):.5f}\n")

    # 테스트 2: 중규모 시뮬레이션
    print("=== 10,000번 시뮬레이션 ===")
    pi_estimate_2 = estimate_pi(10000)
    print(f"추정된 π 값: {pi_estimate_2}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_2 - 3.14159):.5f}\n")

    # 테스트 3: 대규모 시뮬레이션
    print("=== 100,000번 시뮬레이션 ===")
    pi_estimate_3 = estimate_pi(100000)
    print(f"추정된 π 값: {pi_estimate_3}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_3 - 3.14159):.5f}\n")

    # 테스트 4: 여러 번 실행하여 일관성 확인
    print("=== 같은 횟수로 5번 반복 ===")
    for i in range(5):
        result = estimate_pi(10000)
        print(f"시도 {i+1}: {result}")
