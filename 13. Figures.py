# Интерфейс для фигур
class Shape:
    def accept(self, visitor):
        pass


# Конкретные реализации фигур
class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def accept(self, visitor):
        # Принимаем посетителя для круга
        return visitor.visit_circle(self)


class Square(Shape):
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def accept(self, visitor):
        # Принимаем посетителя для квадрата
        return visitor.visit_square(self)


class Star(Shape):
    def __init__(self, area):
        self.area = area

    def accept(self, visitor):
        # Принимаем посетителя для звезды
        return visitor.visit_star(self)


# Интерфейс для посетителя
class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass

    def visit_star(self, star):
        pass


# Конкретные реализации посетителей
class AreaVisitor(Visitor):
    def visit_circle(self, circle):
        # Вычисляем площадь круга
        return 3.14 * circle.radius ** 2

    def visit_square(self, square):
        # Вычисляем площадь квадрата
        return square.size ** 2

    def visit_star(self, star):
        # Возвращаем площадь звезды
        return star.area


class ColorVisitor(Visitor):
    def visit_circle(self, circle):
        # Возвращаем цвет круга
        return circle.color

    def visit_square(self, square):
        # Возвращаем цвет квадрата
        return square.color

    def visit_star(self, star):
        # Возвращаем жёлтый цвет для звезды
        return "yellow"


class CornerVisitor(Visitor):
    def visit_circle(self, circle):
        # Возвращаем количество углов круга (ноль)
        return 0

    def visit_square(self, square):
        # Возвращаем количество углов квадрата (четыре)
        return 4

    def visit_star(self, star):
        # Возвращаем количество углов звезды (пять)
        return 5


# Использование
if __name__ == "__main__":
    circle = Circle(5, "red")
    square = Square(7.0, "blue")
    star = Star(36.0)

    # Создаем посетителей для каждого типа операции
    area_visitor = AreaVisitor()
    color_visitor = ColorVisitor()
    corner_visitor = CornerVisitor()

    # Выводим результаты для каждой фигуры
    print(f"Площадь круга: {circle.accept(area_visitor)}")
    print(f"Площадь квадрата: {square.accept(area_visitor)}")
    print(f"Площадь звезды: {star.accept(area_visitor)}")

    print(f"Цвет круга: {circle.accept(color_visitor)}")
    print(f"Цвет квадрата: {square.accept(color_visitor)}")
    print(f"Цвет звезды: {star.accept(color_visitor)}")

    print(f"Количество углов круга: {circle.accept(corner_visitor)}")
    print(f"Количество углов квадрата: {square.accept(corner_visitor)}")
    print(f"Количество углов звезды: {star.accept(corner_visitor)}")
