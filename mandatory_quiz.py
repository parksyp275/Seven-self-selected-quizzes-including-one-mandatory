import random

def estimate_pi(num_samples: int) -> float:
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / num_samples)
    
    return pi_estimate

if __name__ == "__main__":
    print("=== 100번 시뮬레이션 ===")
    pi_estimate_1 = estimate_pi(100)
    print(f"추정된 π 값: {pi_estimate_1}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_1 - 3.14159):.5f}\n")

    print("=== 10,000번 시뮬레이션 ===")
    pi_estimate_2 = estimate_pi(10000)
    print(f"추정된 π 값: {pi_estimate_2}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_2 - 3.14159):.5f}\n")

    print("=== 100,000번 시뮬레이션 ===")
    pi_estimate_3 = estimate_pi(100000)
    print(f"추정된 π 값: {pi_estimate_3}")
    print(f"실제 π 값: 3.14159...")
    print(f"오차: {abs(pi_estimate_3 - 3.14159):.5f}\n")

    print("=== 같은 횟수로 5번 반복 ===")
    for i in range(5):
        result = estimate_pi(10000)
        print(f"시도 {i+1}: {result}")
