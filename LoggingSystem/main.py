# Prerequisite for this is, you must know Chain of Responsibility design pattern

from log_processor import LogProcessor
from info_log_processor import InfoLogProcessor
from error_log_processor import ErrorLogProcessor
from debug_log_processor import DebugLogProcessor

def main(logprocesor: LogProcessor):
    for log in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        result = logprocesor.handler(log)
        if result:
            print(result)
        else:
            print(f"Logger can't process {log}")


if __name__ == "__main__":
    info = InfoLogProcessor()
    debug = DebugLogProcessor()
    error = ErrorLogProcessor()

    info.set_next(debug).set_next(error)
    main(info)
