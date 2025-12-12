def get_student_plants(diagram: str, student_name: str, students: list[str] = None) -> list[str]:
    """
    정원 다이어그램에서 특정 학생의 식물들을 찾아 반환합니다.
    
    Args:
        diagram: 두 줄로 된 정원 다이어그램 (\n으로 구분)
        student_name: 식물을 찾을 학생 이름
        students: 학생 명단 (None이면 기본 12명 사용)
    
    Returns:
        해당 학생의 식물 이름 리스트 (4개)
    """
    # 기본 학생 명단 (알파벳 순서)
    default_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                       "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    
    # students가 None이면 기본 명단 사용
    if students is None:
        students = default_students
    else:
        # 학생 명단이 주어졌을 때, 문제 규칙에 따라 정렬이 필요할 수 있으나
        # 예제 3(사용자 지정 명단)의 규칙에 따라 주어진 리스트 순서를 그대로 사용합니다.
        # 만약 문제의 "알파벳 순서 배치" 규칙을 엄격히 따르려면 아래 주석을 해제하세요.
        # students = sorted(students)
        pass

    # TODO 1: 식물 코드를 전체 이름으로 변환하는 딕셔너리를 만드세요
    # 힌트: 'G' -> 'Grass', 'V' -> 'Violet' 등
    plant_codes = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radish',
        'V': 'Violet'
    }

    # TODO 2: 다이어그램 문자열을 줄 단위로 나누세요
    # 힌트: split() 메서드를 사용하세요
    rows = diagram.split('\n')

    # TODO 3: 학생 명단에서 찾으려는 학생의 인덱스(위치)를 찾으세요
    # 힌트: list.index() 메서드를 사용하세요
    try:
        student_index = students.index(student_name)
    except ValueError:
        return [] # 학생이 명단에 없는 경우 빈 리스트 반환

    # TODO 4: 학생의 인덱스를 사용하여 컵의 시작 위치를 계산하세요
    # 힌트: 각 학생은 2개의 열을 차지합니다 (인덱스 * 2)
    start_index = student_index * 2
    end_index = start_index + 2

    # TODO 5: 위 줄과 아래 줄에서 해당 학생의 식물 코드를 추출하세요
    # 힌트: 문자열 슬라이싱 [start:end]을 사용하세요
    # 힌트: 첫 번째 줄의 2개 + 두 번째 줄의 2개를 순서대로 가져와야 합니다
    codes = rows[0][start_index:end_index] + rows[1][start_index:end_index]

    # TODO 6: 추출한 코드를 식물 이름으로 변환하여 리스트로 반환하세요
    # 힌트: 리스트 컴프리헨션과 위에서 만든 딕셔너리를 사용하면 편해요
    return [plant_codes[code] for code in codes]
