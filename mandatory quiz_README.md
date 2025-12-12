# Day 69: Monte Carlo Simulation for Pi Estimation
**작성자:** 박소영 (2025006260)

## 📌 과제 개요
이 프로젝트는 Monte Carlo 시뮬레이션을 사용하여 원주율(π)을 추정하는 Python 프로그램.
랜덤하게 다트를 던져 원 안에 들어가는 비율을 계산하여 π 값을 근사함.

## 🛠️ 사용 기술 및 조건
- **Language:** Python
- **Core Logic:** `random.uniform(-1, 1)`을 사용한 좌표 생성
- **Math:** `x^2 + y^2 <= 1` 공식을 통한 영역 판별

## 🚀 실행 방법
`assignment_day69.py` 파일을 실행하면 100번, 10,000번, 100,000번 시뮬레이션 결과와 오차를 확인할 수 있음.
