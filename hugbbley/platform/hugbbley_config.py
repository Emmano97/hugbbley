from hugbbley import MODULE_NAME, MODULE_HOME_DIR
from string import Template
from functools import lru_cache
import os

DEFAULT_CONFIG_FILE_NAME = f".{MODULE_NAME}_config.toml"
SQLITE_DATABASE_FILE_NAME = f"{MODULE_NAME}_db.sqlite"
KEEPS_FILE_NAME = f"{MODULE_NAME}_keeps.txt"
DATABASE_PASSWORD_CONFIG_PATH = "db.password"
FASTAPI_ENTRY_FILE_PATH = "fastapi.path_to_entry_file"
SQLITE_DATABASE_FILE_PATH = os.path.join(MODULE_HOME_DIR, 'data', SQLITE_DATABASE_FILE_NAME)

DEFAULT_CONFIG_FILE_CONTENT = f"""
[db]
password=""

[logging]
level = "INFO"
format = "%(asctime)s - %(levelname)s - %(message)s"
file_path = "/path/to/log/file.log"

[fastapi]
path_to_entry_file = "asgi.py"

[dashboard]
port = 8766
"""

KEEP_CONFIG_PATH_CONTENT = Template("""
[config]
path = $config_file_path
""")


@lru_cache(maxsize=None)
def get_required_config_keys(config):
    all_keys = []

    def traverse_dict(dictionary, prefix=""):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                traverse_dict(value, f"{prefix}{key}.")
            else:
                all_keys.append(f"{prefix}{key}")

    traverse_dict(config)
    return all_keys
