class BowlingGame:
    def __init__(self):
        """새 볼링 게임 초기화"""
        self.rolls = []

    def roll(self, pins: int) -> None:
        """
        플레이어가 공을 던질 때마다 호출됩니다.
        
        Args:
            pins: 쓰러뜨린 핀의 개수 (0-10)
        
        Raises:
            ValueError: 유효하지 않은 입력인 경우
        """
        if not isinstance(pins, int) or pins < 0 or pins > 10:
            raise ValueError("쓰러뜨린 핀은 0-10 사이여야 합니다")

        temp_score = 0
        roll_index = 0
        for frame in range(10):
            if roll_index >= len(self.rolls):
                break
            if self.rolls[roll_index] == 10:
                temp_score += 10
                if roll_index + 1 < len(self.rolls):
                    temp_score += self.rolls[roll_index + 1]
                if roll_index + 2 < len(self.rolls):
                    temp_score += self.rolls[roll_index + 2]
                roll_index += 1
            elif roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                temp_score += 10
                if roll_index + 2 < len(self.rolls):
                    temp_score += self.rolls[roll_index + 2]
                roll_index += 2
            else:
                if roll_index + 1 < len(self.rolls):
                    temp_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        
        if roll_index >= len(self.rolls) and frame == 9:
             # Check if game is complete logic needed for precise game-over check
             # Simplified check based on rolls count is difficult due to strikes
             # Using score method to validate if game is finished
             try:
                 self.score()
                 raise ValueError("게임이 이미 끝났습니다")
             except ValueError as e:
                 if str(e) == "게임이 이미 끝났습니다":
                     raise e
                 pass

        self.rolls.append(pins)

    def score(self) -> int:
        """
        게임이 완전히 끝난 후에만 호출됩니다.
        
        Returns:
            게임의 총점
        
        Raises:
            ValueError: 게임이 아직 끝나지 않은 경우
        """
        total_score = 0
        roll_index = 0
        
        for frame in range(10):
            if roll_index >= len(self.rolls):
                raise ValueError("게임이 아직 끝나지 않았습니다")

            if self.rolls[roll_index] == 10:
                if roll_index + 2 >= len(self.rolls):
                    raise ValueError("게임이 아직 끝나지 않았습니다")
                total_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                if roll_index + 2 >= len(self.rolls):
                    raise ValueError("게임이 아직 끝나지 않았습니다")
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                if roll_index + 1 >= len(self.rolls):
                    raise ValueError("게임이 아직 끝나지 않았습니다")
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
                
        return total_score

if __name__ == "__main__":
    # 테스트 1: 모두 거터볼
    game = BowlingGame()
    for _ in range(20):
        game.roll(0)
    print(f"Test 1 Score: {game.score()}")

    # 테스트 2: 모두 1개씩
    game = BowlingGame()
    for _ in range(20):
        game.roll(1)
    print(f"Test 2 Score: {game.score()}")

    # 테스트 3: 하나의 스페어
    game = BowlingGame()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    print(f"Test 3 Score: {game.score()}")

    # 테스트 4: 하나의 스트라이크
    game = BowlingGame()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    print(f"Test 4 Score: {game.score()}")

    # 테스트 5: 완벽한 게임
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    print(f"Test 5 Score: {game.score()}")
