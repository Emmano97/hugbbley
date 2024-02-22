import multiprocessing
import time

from hugbbley.core.http.finder import find_fastapi_app
from hugbbley.core.utils.config_manager import get_fastapi_entry_path

def monitor_fastapi_endpoints():
    fastapi_app = find_fastapi_app(get_fastapi_entry_path())
    routes = fastapi_app.routes




def task():
    while True:
        print("Doing something in the new process...")
        time.sleep(1)


def start_new_process():
    new_process = multiprocessing.Process(target=task)
    new_process.start()
    new_process.join()


if __name__ == "__main__":
    start_new_process()
