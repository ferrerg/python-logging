import logging
import sys
from typing import Any, Optional

import picologging as logging


class PicoLoggerAdapter(object):
    _DEFAULT_FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    _DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

    _DEFAULT_LOGGER_LVL = logging.INFO
    _DEFAULT_STDOUT_LVL = logging.WARNING
    _DEFAULT_FILE_LVL = logging.INFO

    def __init__(self, log_lvl: Optional[int] = None):
        self._logger = logging.getLogger()
        self._logger.setLevel(log_lvl or self._DEFAULT_LOGGER_LVL)

    def _set_handler(
        self, handler: logging.Handler, log_lvl: Optional[int] = None
    ):
        handler.setLevel(log_lvl)
        formatter = logging.Formatter(
            fmt,
            datefmt=datefmt,
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def set_stdout_handler(
        self,
        log_lvl: Optional[int] = None,
        fmt: Optional[str] = None,
        datefmt: Optional[str] = None,
    ):
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(log_lvl or self._DEFAULT_STDOUT_LVL)
        formatter = logging.Formatter(
            fmt or self._DEFAULT_FMT,
            datefmt=datefmt or self._DEFAULT_DATEFMT,
        )
        stdout_handler.setFormatter(formatter)
        self._logger.addHandler(stdout_handler)

    def set_file_handler(
        self,
        filename: str,
        log_lvl: Optional[int] = None,
        fmt: Optional[str] = None,
        datefmt: Optional[str] = None,
    ):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(log_lvl or self._DEFAULT_FILE_LVL)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(
            fmt or self._DEFAULT_FMT,
            datefmt=datefmt or self._DEFAULT_DATEFMT,
        )
        file_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)

    def info(self, message: str, *args: Any, **kwargs: Any):
        self._logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any):
        self._logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any):
        self._logger.error(message, *args, **kwargs)

    def debug(self, message: str, *args: Any, **kwargs: Any):
        self._logger.debug(message, *args, **kwargs)

    def exception(self, message: str, *args: Any, **kwargs: Any):
        self._logger.exception(message, *args, **kwargs)


def main():
    logger = PicoLoggerAdapter()
    logger.set_stdout_handler(log_lvl=logging.WARNING)
    logger.set_file_handler("app.log", log_lvl=logging.INFO)
    logger.info("A log message!")
    logger.warning("A log message with %s", "arguments")


if __name__ == "__main__":
    main()
