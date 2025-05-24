class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @staticmethod
    def suma(num1, num2):
        # Los estudiantes completan este método
        pass

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    result = Operaciones.suma(num1, num2)
    print(result)
