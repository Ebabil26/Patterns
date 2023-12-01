# Определение базового класса для всех выражений
class Expression:
    def accept(self, visitor):
        pass

# Класс для представления числовых литералов
class Literal(Expression):
    def __init__(self, value):
        self.value = value

    # Принятие посетителя для литерала
    def accept(self, visitor):
        return visitor.visit_literal(self)

# Класс для представления бинарных операций (+, *)
class BinaryOperation(Expression):
    def __init__(self, left, right, sign):
        self.left = left
        self.right = right
        self.sign = sign

    # Принятие посетителя для бинарной операции
    def accept(self, visitor):
        return visitor.visit_binary_operation(self)

# Класс для представления скобок
class Brackets(Expression):
    def __init__(self, inner_expression):
        self.inner_expression = inner_expression

    # Принятие посетителя для скобок
    def accept(self, visitor):
        return visitor.visit_brackets(self)

# Базовый класс для посетителей
class Visitor:
    # Методы для посещения литерала, бинарной операции и скобок
    def visit_literal(self, expression):
        pass

    def visit_binary_operation(self, expression):
        pass

    def visit_brackets(self, expression):
        pass

# Посетитель для печати выражения
class PrintExpression(Visitor):
    def __init__(self):
        self.srt = ""

    # Посещение литерала - добавление его значения в строку
    def visit_literal(self, expression):
        self.srt += str(expression.value)

    # Посещение бинарной операции - обход левой и правой частей выражения
    def visit_binary_operation(self, expression):
        expression.left.accept(self)
        self.srt += f" {expression.sign} "
        expression.right.accept(self)

    # Посещение скобок - добавление скобок в строку и обход внутреннего выражения
    def visit_brackets(self, expression):
        self.srt += "("
        expression.inner_expression.accept(self)
        self.srt += ")"

if __name__ == "__main__":
    # Создание выражений и их обработка посетителем PrintExpression
    expression = BinaryOperation(BinaryOperation(Literal(1), Literal(2), "+"), Literal(3), "+")
    print_expression = PrintExpression()
    expression.accept(print_expression)
    print(f"Результат: {print_expression.srt}")

    more_expression = BinaryOperation(Literal(3), Brackets(BinaryOperation(Literal(1), Literal(2), "+")), "*")
    more_print_expression = PrintExpression()
    more_expression.accept(more_print_expression)
    print(f"Результат: {more_print_expression.srt}")
