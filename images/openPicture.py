import subprocess
import sys, os


_current_image_process = None

def openIMG(imagePath=None, destroy=False):
    global _current_image_process

    # If destroy=True → close the running subprocess
    if destroy:
        if _current_image_process:
            _current_image_process.terminate()
            _current_image_process = None
        return

    # Destroy previous image if one is open
    if _current_image_process:
        _current_image_process.terminate()

    script_path = os.path.join(os.path.dirname(__file__), "openPicture_subprocess.py")
    abs_image_path = os.path.abspath(imagePath)

    # Start Tk process and keep the handle
    _current_image_process = subprocess.Popen([
        sys.executable,
        script_path,
        abs_image_path
    ])


        
    
    


