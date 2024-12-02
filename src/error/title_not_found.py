class TitleNotFoundError(Exception):
    def __init__(self) -> None:
        super().__init__("Title not found!")

    def __str__(self) -> str:
        return super().__str__()
