import os
from fluent import handler
import logging
import pytest
from dotenv import load_dotenv

custom_log_format = {
    "host": "%(hostname)s",
    "where": "%(module)s.%(funcName)s",
    "type": "%(levelname)s",
    "stack_trace": "%(exc_text)s",
}

fluentd_tag = "pytest.logs"

@pytest.fixture(autouse=True)
def load_env():
   load_dotenv() 


def pytest_logger_config(logger_config):
    fluentd_host = os.environ.get("FLUENT_HOST_URL")
    fluentd_port = 24224
      
    logger_config.add_loggers(["http_logger", "default"], stdout_level="debug")
    logger_config.set_log_option_default("default")

    fluent_handler = handler.FluentHandler(
        fluentd_tag, host=str(fluentd_host), port=fluentd_port
    )
    log_formatter = handler.FluentRecordFormatter(custom_log_format)
    fluent_handler.setFormatter(log_formatter)

    logger = logging.getLogger("http_logger")

    logger.setLevel(logging.INFO)
    logger.addHandler(fluent_handler)