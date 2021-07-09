from datetime import datetime
def get_time():
    """
    Returns xurrent time
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time