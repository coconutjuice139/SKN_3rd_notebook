
class Person:
    def __init__(self, p_name, p_age) -> None:
        self.name = p_name 
        self.age = p_age

    def hello(self) -> None:
        print(f"저의 이름은 {self.name}입니다.\n나이는 {self.age}입니다.")

        