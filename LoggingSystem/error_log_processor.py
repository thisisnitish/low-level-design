from log_processor import LogProcessor

class ErrorLogProcessor(LogProcessor):
    def handler(self, request):
        if request == "ERROR":
            return "ERROR Logger Processed"
        else:
            return super().handler(request)