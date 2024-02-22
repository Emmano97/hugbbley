import re
from fastapi import FastAPI


def find_fastapi_app(file_path):
    # Regular expression to match FastAPI app object definition with any variable name
    pattern = r"(\w+)\s*=\s*FastAPI\(\s*.*?\)"

    with open(file_path, "r") as file:
        file_content = file.read()
        match = re.search(pattern, file_content, re.DOTALL)

        if match:
            variable_name = match.group(1)
            # Execute the FastAPI app object definition to get the app object
            globals_dict = {}
            exec(match.group(0), globals_dict)
            fastapi_app = globals_dict.get(variable_name)

            # Check if the object is an instance of FastAPI
            if isinstance(fastapi_app, FastAPI):
                return fastapi_app
            else:
                raise ValueError(f"The found object '{variable_name}' is not an instance of FastAPI.")
        else:
            raise ValueError("FastAPI app object not found in the file.")
