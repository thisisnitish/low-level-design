from abc import ABC, abstractmethod

class LogProcessor(ABC):
    def __init__(self):
        self.logger = None

    def set_next(self, logger):
        self.logger = logger
        return logger

    @abstractmethod
    def handler(self, request):
        if self.logger:
            return self.logger.handler(request)
        # return None