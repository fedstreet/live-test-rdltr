import os
import time
import requests

from subprocess import Popen

PROCESS_TIMEOUT = 1.0

if os.name == "nt":
    PYTHON_EXECUTABLE = "python.exe"
else:
    PYTHON_EXECUTABLE = "python"


def get_resources_folder_path():
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    base_dir = os.path.split(current_dir)[0]
    return os.path.join(base_dir, "resources", "web_pages")


def get_default_page_url():
    return "{}/{}".format(get_stub_server_url(), "default.html")


def get_stub_server_url():
    return "http://localhost:8000"


__process = None


def wait_server_availability(timeout_sec: float = 5.0):
    end_time = time.time() + timeout_sec
    url = get_default_page_url()
    while time.time() < end_time:
        time.sleep(0.05)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return
        except ConnectionError:
            pass

    raise AssertionError(f"The stub server is not available in {timeout_sec:.1f} seconds.")


def start_server():
    global __process

    __process = Popen([PYTHON_EXECUTABLE, "-m", "http.server", "--directory", get_resources_folder_path()])
    if __process.poll() is not None:
        raise ChildProcessError("Process http.server was not started")
    wait_server_availability()


def stop_server():
    global __process

    if __process is not None:
        __process.terminate()
        __process.wait(timeout=PROCESS_TIMEOUT)
        __process = None
