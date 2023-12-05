# Патерн Сінглтон
class PageRegistry:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PageRegistry, cls).__new__(cls)
            cls._instance.pages = {}
        return cls._instance

    def register_page(self, page_id, content):
        self.pages[page_id] = content

    def get_page_content(self, page_id):
        return self.pages.get(page_id, None)


# Клас для представлення книги
class Book:
    def __init__(self, title, book_builder):
        self.title = title
        self.builder = book_builder

    def build_book(self):
        self.builder.build_title_page()
        self.builder.build_content()

    def get_book(self):
        return self.builder.get_book()


# Абстрактний клас для білдера книги
class BookBuilder:
    def build_title_page(self):
        pass

    def build_content(self):
        pass

    def get_book(self):
        pass


# Клас для конкретного білдера наукової книги
class ScientificBookBuilder(BookBuilder):
    def __init__(self):
        self.book = Book("Наукова книга", self)
        self.page_registry = PageRegistry()

    def build_title_page(self):
        self.page_registry.register_page(1, "Заголовок: Введення в науку")

    def build_content(self):
        self.page_registry.register_page(2, "Стр. 1: Теорія динамічних систем")
        self.page_registry.register_page(3, "Стр. 2: Методи математичного моделювання")
        self.page_registry.register_page(4, "Список використаної літератури")

    def get_book(self):
        return self.book


# Клас для конкретного білдера роману
class NovelBookBuilder(BookBuilder):
    def __init__(self):
        self.book = Book("Роман", self)
        self.page_registry = PageRegistry()

    def build_title_page(self):
        self.page_registry.register_page(1, "Заголовок: Таємниця високого замку")

    def build_content(self):
        self.page_registry.register_page(2, "Стр. 1: Вступний епізод")
        self.page_registry.register_page(3, "Стр. 2: Опис персонажів")
        self.page_registry.register_page(4, "Список персонажів")

    def get_book(self):
        return self.book


# Клас для конкретного білдера посібника
class HandbookBookBuilder(BookBuilder):
    def __init__(self):
        self.book = Book("Посібник", self)
        self.page_registry = PageRegistry()

    def build_title_page(self):
        self.page_registry.register_page(1, "Заголовок: Посібник з програмування")

    def build_content(self):
        self.page_registry.register_page(2, "Стр. 1: Основи програмування")
        self.page_registry.register_page(3, "Стр. 2: Приклади коду")
        self.page_registry.register_page(4, "Картинка з прикладом коду")

    def get_book(self):
        return self.book


# Приклад використання
def main():
    scientific_book_builder = ScientificBookBuilder()
    novel_book_builder = NovelBookBuilder()
    handbook_book_builder = HandbookBookBuilder()

    scientific_book = Book("Наукова книга", scientific_book_builder)
    novel = Book("Роман", novel_book_builder)
    handbook = Book("Посібник", handbook_book_builder)

    scientific_book.build_book()
    novel.build_book()
    handbook.build_book()

    print(scientific_book_builder.page_registry.pages)
    print(novel_book_builder.page_registry.pages)
    print(handbook_book_builder.page_registry.pages)


if __name__ == "__main__":
    main()
