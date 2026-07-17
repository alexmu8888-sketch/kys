import subprocess
import platform
import requests 

def download(url, output_path="alexmufavorite.mp4"):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return output_path

def play_video(path):
    system = platform.system()
    if system == "Windows":
        subprocess.run(["start", "", path], shell=True, check =True)
    elif system == "Darwin":  
        subprocess.run(["open", path], check=True)
    else:
        subprocess.run(["xdg-open", path], check=True)

def definetly_math_stuff(file_id, output_path="alexmufavorite.mp4"):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    download(url, output_path)
    play_video(output_path)
    return output_path
    

        