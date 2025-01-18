from log_processor import LogProcessor

class DebugLogProcessor(LogProcessor):
    def handler(self, request):
        if request == "DEBUG":
            return "DEBUG Logger Processed"
        else:
            return super().handler(request)