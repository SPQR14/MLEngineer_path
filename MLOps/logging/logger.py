import logging
from pathlib import Path

def setup_logger(name):

    """
    Configure the application's root logger.

    This function creates a dedicated ``logs`` directory in the same
    directory as this module if it does not already exist. It then configures
    the root logger with a DEBUG logging level and two handlers:

    - A FileHandler that writes log messages to ``logs/<name>.log``.
    - A StreamHandler that outputs log messages to the console.

    Any existing logging configuration is replaced to ensure that the
    specified handlers and logging level are applied.

    Args:
        name (str): Name used to generate the log file. The resulting log
            file will be created as ``logs/<name>.log``.

    Returns:
        None
    """

    # Defines the root directory of tis file
    BASE_DIR = Path(__file__).resolve().parent
    # Defines log directory and creates it if it doesn't exist
    LOG_DIR = BASE_DIR / f"{name.capitalize()}logs"
    LOG_DIR.mkdir(exist_ok=True)
    # Complete path to the log file
    LOG_FILE = LOG_DIR / f"{name}.log"

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler()
        ],
        force=True
    )

    logging.debug(f"Logger '{name}' has been set up with DEBUG level and file handler '{name}.log'")

