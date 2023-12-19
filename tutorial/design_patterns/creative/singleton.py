"""
Singleton Design Pattern
"""


# Logging example
import logging


class Logger:
    _instance = None # holds the single instance of the class

    def __new__(cls, module_name=None, log_file=None):
        """This method controls the instantiation process"""

        # Create new instance if no instance of the logger already exists
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(module_name or __name__)
            cls._instance._configure_logger(log_file)        
        return cls._instance

    def _configure_logger(self, log_file):
        """This method configures the logger instance"""
        # Additional setup for the logger can be done here
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file) if log_file else logging.StreamHandler()
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

# Example usage:

# Create two instances of Logger with different log files
logger_module1 = Logger(module_name="module1", log_file="module1.log")
logger_module2 = Logger(module_name="module2", log_file="module2.log")

# Log a message using the first instance
logger_module1.logger.warning("Warning message for module 1.")

# Log a message using the second instance
logger_module2.logger.error("Error message for module 2.")



# Configuration example
from decouple import Config, RepositoryIni

class ConfigManager:
    _instance = None

    def __new__(cls, config_file=".ini"):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = Config(RepositoryIni(config_file))
        return cls._instance

    def get_config_value(self, key, default=None):
        # Retrieve a configuration value based on the key
        return self._config.get(key, default)

# Example usage:

# Create an instance of ConfigManager
config_manager = ConfigManager()

# Access configuration values
db_url = config_manager.get_config_value("DATABASE_URL")
api_key = config_manager.get_config_value("API_KEY", default="")

print("Database URL:", db_url)
print("API Key:", api_key)
