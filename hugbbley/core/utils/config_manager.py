from hugbbley.platform.hugbbley_config import (DATABASE_PASSWORD_CONFIG_PATH,
                                               DEFAULT_CONFIG_FILE_NAME, SQLITE_DATABASE_FILE_PATH,
                                               FASTAPI_ENTRY_FILE_PATH)

from functools import lru_cache
import traceback
import toml


@lru_cache(maxsize=None)
def read_toml_configs():
    try:
        with open(DEFAULT_CONFIG_FILE_NAME, 'r') as file:
            config = toml.load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{DEFAULT_CONFIG_FILE_NAME}' not found")
    except Exception as e:
        raise Exception(f"Error reading configuration file '{DEFAULT_CONFIG_FILE_NAME}': {e}")


def get_config(attribute_path, raise_exception=False):
    config = read_toml_configs()
    error_message = ""
    attributes = attribute_path.split('.')
    current_level = config

    try:
        for attribute in attributes:
            current_level = current_level[attribute]
    except Exception as error:
        error_message += f" {error} \n {traceback.format_exc()}"

        can_raise_exception = error_message and raise_exception
        if can_raise_exception:
            raise HugbbleyConfigNoFoundException(f"'{attribute_path}' not found in the " \
                                                 f"configuration: {DEFAULT_CONFIG_FILE_NAME}\n{error_message}")
        else:
            current_level = None

    return current_level


def get_database_password():
    return get_config(DATABASE_PASSWORD_CONFIG_PATH, raise_exception=True)


def get_database_url():
    return f"sqlite:///{SQLITE_DATABASE_FILE_PATH}?cipher=aes-256-cfb&key={get_database_password()}"


def get_fastapi_entry_path():
    p = get_config(FASTAPI_ENTRY_FILE_PATH)
    return

class HugbbleyConfigNoFoundException(Exception):
    pass
