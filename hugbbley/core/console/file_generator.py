from hugbbley.core.utils.config_manager import get_database_password
from hugbbley.platform.hugbbley_config import (DEFAULT_CONFIG_FILE_NAME,
                                               DEFAULT_CONFIG_FILE_CONTENT,
                                               SQLITE_DATABASE_FILE_NAME, KEEPS_FILE_NAME,
                                               KEEP_CONFIG_PATH_CONTENT, )
from hugbbley import DATA_FOLDER_PATH

import sqlite3
import os


def create_config_file(args, **kwargs):
    with open(DEFAULT_CONFIG_FILE_NAME, "w") as default_config_file:
        default_config_file.write(DEFAULT_CONFIG_FILE_CONTENT)
        config_file_path = default_config_file.name

    keep_file_path = os.path.join(DATA_FOLDER_PATH, KEEPS_FILE_NAME)
    with open(keep_file_path, "a") as keep_file:
        keep_file.write(KEEP_CONFIG_PATH_CONTENT.substitute(config_file_path=config_file_path))


def create_sqlite_db_file(*args, **kwargs):
    # Get the directory of the current script
    os.makedirs(DATA_FOLDER_PATH, exist_ok=True)
    # Relative path to the database file
    db_file = os.path.join(DATA_FOLDER_PATH, SQLITE_DATABASE_FILE_NAME)
    password = get_database_password()
    try:
        conn = sqlite3.connect(db_file)

        # Set the password for the database
        conn.execute(f"PRAGMA key = '{password}'")
        # You can perform other operations on the database if needed
        conn.close()
        print(f"SQLite database file '{db_file}' created successfully with password.")
    except Exception as e:
        print(f"Error creating SQLite database file: {e}")
