import time

def wait(duration, finale):



    if time.time() >= finale + duration:
        return True
    return False


