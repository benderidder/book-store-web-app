from dataclasses import dataclass

@dataclass
class BookViewModel:
    id: int
    title: str
    author_name: str