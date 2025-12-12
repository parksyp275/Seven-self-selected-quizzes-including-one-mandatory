class Alien:
    """외계인을 나타내는 클래스"""
    
    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        """
        새로운 외계인을 만듭니다.
        
        Parameters:
            x_coordinate (int): 외계인의 x 좌표
            y_coordinate (int): 외계인의 y 좌표
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        
        Alien.total_aliens_created += 1
    
    def hit(self):
        """
        외계인이 공격을 받습니다. 체력이 1 감소합니다.
        """
        self.health -= 1
    
    def is_alive(self):
        """
        외계인이 살아있는지 확인합니다.
        
        Returns:
            bool: 살아있으면 True, 죽었으면 False
        """
        return self.health > 0
    
    def teleport(self, new_x, new_y):
        """
        외계인을 새로운 위치로 순간이동시킵니다.
        
        Parameters:
            new_x (int): 새로운 x 좌표
            new_y (int): 새로운 y 좌표
        """
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    
    def collision_detection(self, other_object):
        """
        충돌 감지 (나중에 구현할 예정)
        
        Parameters:
            other_object: 충돌을 확인할 다른 객체
        """
        pass

def new_aliens_collection(positions):
    """
    위치 리스트를 받아서 외계인들을 생성합니다.
    
    Parameters:
        positions (list): (x, y) 튜플들의 리스트
        
    Returns:
        list: 생성된 Alien 객체들의 리스트
    """
    return [Alien(x, y) for x, y in positions]
