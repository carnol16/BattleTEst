import os
import time
from audioMixer import SoundManager

sm = SoundManager()

def play_ascii_video(folder_path, fps=30):
    #sm.play_music("animeHorse")
    # Get sorted list of text files
    frames = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')])
    
    frame_duration = 1 / fps
    
    for frame_file in frames:
        with open(os.path.join(folder_path, frame_file), 'r') as f:
            # Clear the terminal screen
            print("\033[H\033[J", end="") 
            # Print the frame
            print(f.read())
            
        time.sleep(0.025)

# Usage
play_ascii_video('/Users/coltonarnold/Documents/GitHub/OFFICAL_BattleTEst/ascii_frames', fps=30)