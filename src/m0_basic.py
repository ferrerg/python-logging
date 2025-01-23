import picologging as logging


def main():
    # Configure basic logging for console output
    logging.basicConfig(level=logging.INFO)

    # Create and configure file handler
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.WARNING)

    # Create formatter and add it to the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    # Get logger and add file handler
    logger = logging.getLogger()
    logger.addHandler(file_handler)

    # ... rest of the logging calls remain the same ...
    logger.info("A log message!")
    logger.warning("A log message with %s", "arguments")


if __name__ == "__main__":
    main()
