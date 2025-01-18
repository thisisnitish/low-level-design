from log_processor import LogProcessor

class InfoLogProcessor(LogProcessor):
    def handler(self, request):
        if request == "INFO":
            return "INFO Logger Processed"
        else:
            return super().handler(request)