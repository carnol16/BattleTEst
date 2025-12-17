import cv2
import os

def video_to_ascii(video_path, output_folder, width=240):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    cap = cv2.VideoCapture(video_path)
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Resize to terminal-friendly width while maintaining aspect ratio
        height = int(frame.shape[0] * (width / frame.shape[1]) * 0.5)
        img = cv2.resize(frame, (width, height))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        ascii_frame = ""
        for row in img_gray:
            for pixel in row:
                ascii_frame += chars[pixel // 25]
            ascii_frame += "\n"
            
        with open(f"{output_folder}/frame_{frame_count:04d}.txt", "w") as f:
            f.write(ascii_frame)
            
        frame_count += 1
        
    cap.release()
    print(f"Generated {frame_count} ASCII frames in {output_folder}")

video_to_ascii('/Users/coltonarnold/Documents/GitHub/OFFICAL_BattleTEst/video/animeHorse.mov', 'ascii_frames')
