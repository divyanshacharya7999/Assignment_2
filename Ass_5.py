import os
from typing import Any

class CloudLogger:
    def __init__(self):
        print("Using Cloud Logger")

    def write_log(self, message: str) -> bool:
        print(f"Successfully uploaded: {message}")
        return True

class FileLogger:
    def __init__(self):
        print("Using File Logger")

    def write_log(self, message: str) -> bool:
        try:
            with open("filelogger.txt", "w") as file:
                file.write(message)
            print("Log written Successfully")
        except Exception as ex:
            print(f"File not found: {ex.message}")
            return False
        return True

class LogManager:
    def __init__(self, logger: Any):
        self._logger = logger

    def write_log(self, message: str) -> bool:
        return self._logger.write_log(message)

def get_log() -> Any:
    log = "File"
    if log == "File":
        return FileLogger()
    else:
        return CloudLogger()

def main():
    logger = get_log()
    log_manager = LogManager(logger)
    log_manager.write_log("Finally Creating Log after 999+ exceptions")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()

