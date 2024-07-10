class CloudLogger:
    def __init__(self):
        print("Using Cloud Logger")

    def write_log(self, message):
        print(f"Successfully uploaded: {message}")
        return True

class FileLogger:
    def __init__(self):
        print("Using File Logger")

    def write_log(self, message):
            with open("filelogger.txt", "w") as file:
                file.write(message)
            print("Log written Successfully")
            return True

class LogManager:
    def __init__(self, logger):
        self._logger = logger

    def write_log(self, message):
        return self._logger.write_log(message)

def get_log():
    log = "File"
    if log == "File":
        return FileLogger()
    else:
        return CloudLogger()

if __name__ == "__main__":
    logger = get_log()
    log_manager = LogManager(logger)
    log_manager.write_log("Finally Creating Log after 999+ exceptions")
    

