class School:
    """
    학교 명단 관리 시스템
    학생들을 학년별로 관리하는 클래스입니다.
    """
    
    def __init__(self):
        """
        School 객체를 초기화합니다.
        
        힌트: 학년(grade)을 키로, 학생 리스트를 값으로 하는 딕셔너리를 만드세요.
        예: {1: ["Anna", "Bob"], 2: ["Charlie"]}
        """
        # TODO: 학생 정보를 저장할 딕셔너리를 초기화하세요
        # self.students = ???
        self.students = {}
    
    def add_student(self, name: str, grade: int) -> bool:
        """
        학생을 특정 학년에 추가합니다.
        
        Parameters:
            name: 학생 이름 (예: "Anna")
            grade: 학년 (예: 1, 2, 3...)
            
        Returns:
            bool: 성공하면 True, 중복이면 False
            
        힌트: 
        1. 먼저 해당 학년이 딕셔너리에 있는지 확인
        2. 없으면 빈 리스트 생성
        3. 학생이 이미 있는지 확인 (중복 체크)
        4. 없으면 추가하고 True 반환
        """
        # TODO: 해당 학년이 딕셔너리에 없으면 빈 리스트 생성
        # if grade not in self.students:
        #      ???
        if grade not in self.students:
            self.students[grade] = []
        
        # TODO: 학생이 이미 해당 학년에 있는지 확인 (중복 체크)
        # if name in ???:
        #      return ???  # 중복이면 False 반환
        if name in self.students[grade]:
            return False
        
        # TODO: 학생을 해당 학년 리스트에 추가
        # self.students[grade].???
        self.students[grade].append(name)
        
        # TODO: 성공했으므로 True 반환
        # return ???
        return True
    
    def grade(self, grade_number: int) -> list:
        """
        특정 학년의 모든 학생을 알파벳 순으로 반환합니다.
        
        Parameters:
            grade_number: 조회할 학년
            
        Returns:
            list: 해당 학년 학생 이름 리스트 (알파벳순 정렬)
            
        힌트:
        1. 해당 학년이 딕셔너리에 있는지 확인
        2. 없으면 빈 리스트 반환
        3. 있으면 sorted() 함수로 정렬해서 반환
        """
        # TODO: 해당 학년이 딕셔너리에 없으면 빈 리스트 반환
        # if grade_number not in ???:
        #      return ???
        if grade_number not in self.students:
            return []
        
        # TODO: 해당 학년의 학생 리스트를 알파벳순으로 정렬해서 반환
        # return sorted(???)
        return sorted(self.students[grade_number])
    
    def roster(self) -> list:
        """
        전체 학교 명단을 반환합니다.
        학년 순서대로, 각 학년 내에서는 알파벳 순으로 정렬됩니다.
        
        Returns:
            list: 전체 학생 이름 리스트 (학년별, 알파벳순 정렬)
            
        힌트:
        1. 빈 결과 리스트 만들기
        2. 학년을 정렬해서 순서대로 처리 (sorted() 사용)
        3. 각 학년의 학생들을 알파벳순으로 정렬해서 결과에 추가
        """
        # TODO: 결과를 담을 빈 리스트 생성
        # result = ???
        result = []
        
        # TODO: 학년을 오름차순으로 정렬 (1, 2, 3, ...)
        # for current_grade in sorted(???):
        for current_grade in sorted(self.students.keys()):
        
            # TODO: 각 학년의 학생들을 알파벳순으로 정렬해서 가져오기
            # students_in_current_grade = sorted(???)
            students_in_current_grade = sorted(self.students[current_grade])
            
            # TODO: 정렬된 학생들을 결과 리스트에 추가
            # result.extend(???)  # 또는 for 루프 사용
            result.extend(students_in_current_grade)
        
        # TODO: 완성된 전체 명단 반환
        # return ???
        return result
