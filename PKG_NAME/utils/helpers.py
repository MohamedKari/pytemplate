import datetime

def get_path_compatible_date():
    return datetime.datetime.now().isoformat().replace(":", "_").replace(".", "_")