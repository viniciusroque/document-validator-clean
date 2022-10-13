class InvalidUuidException(Exception):
    def __init__(self, error='ID must be a UUID valid.') -> None:
        super().__init__(error)


class ValidationException(Exception):
    ...


class EntityValidationException(Exception):

    def __init__(self, error) -> None:
        self.error = error
        super().__init__('Entity Validation Error')
