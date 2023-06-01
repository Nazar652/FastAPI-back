class CustomError(Exception):
    message: str
    status_code: int

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
