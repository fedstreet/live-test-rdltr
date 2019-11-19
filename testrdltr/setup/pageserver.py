from subprocess import Popen
import os

PROCESS_TIMEOUT = 1.0


def get_resources_folder_path():
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    base_dir = os.path.split(current_dir)[0]
    return os.path.join(base_dir, "resources", "web_pages")


def get_default_page_url():
    return "{}/{}".format(get_stub_server_url(), "default.html")


def get_stub_server_url():
    return "http://localhost:8000"


__process = None


def start_server():
    global __process

    __process = Popen(["python.exe", "-m", "http.server", "--directory", get_resources_folder_path()])
    if __process.poll() is not None:
        raise ChildProcessError("Process http.server was not started")


def stop_server():
    global __process

    if __process is not None:
        __process.terminate()
        __process.wait(timeout=PROCESS_TIMEOUT)
        __process = None
