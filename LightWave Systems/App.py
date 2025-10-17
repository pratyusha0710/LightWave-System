import tkinter as tk
from tkinter import Button
import sounddevice as sd
import wave
import os
from PIL import Image, ImageTk  # For handling images
import pygame  # Import pygame for sound playback
import numpy as np

# Initialize pygame mixer for sound
pygame.mixer.init()



def play_sound(filename, loops=0):
    """Play the sound file with the option to loop."""
    if os.path.exists(filename):
        try:
            status_label.config(text=f"Playing {filename}...")
            app.update()  # Update UI to reflect status
            pygame.mixer.music.load(filename)  # Load the sound file
            pygame.mixer.music.play(loops=loops)  # Play the sound, with loops=0 for no loop or positive value for repetitions
            status_label.config(text="Playback finished.")
        except Exception as e:
            status_label.config(text=f"Error playing sound: {str(e)}")
    else:
        status_label.config(text=f"File {filename} not found!")


def record_sound():
    duration = 5  # Record for 5 seconds
    fs = 44100  # Standard CD quality sample rate
    filename = "recorded_sound.wav"

    try:
        # Delete the existing recording (if any) before recording a new one
        if os.path.exists(filename):
            os.remove(filename)

        status_label.config(text="Recording...")
        app.update()  # Update UI to reflect status
        # Record the audio (stereo, 2 channels)
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
        sd.wait()  # Wait until recording is complete
        
        # Only after the recording is complete, update status and save the file
        status_label.config(text="Recording complete. Saving...")

        # Normalize and convert the float data to 16-bit PCM
        recording = (recording * 32767).astype(np.int16)

        # Save the recorded audio, overwriting the previous file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)  # Stereo
            wf.setsampwidth(2)  # 2 bytes = 16 bits
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())  # Write the frames as bytes

        status_label.config(text=f"Recording saved as {filename}. Playing now...")

        # Play the recorded sound after the recording process is fully finished
        play_sound(filename, loops=2)  # Play the recorded sound 2 times

    except Exception as e:
        status_label.config(text=f"Error during recording: {str(e)}")

# GUI application
app = tk.Tk()
app.title("Accident Prevention App")
app.config(bg="#F5F5DC")

image_path_1 = "Emergency.png"  # Replace with your image file
image_path_2 = "bRAKES.png"  # Replace with your image file
image_path_4 = "Send message.png"
image_path_3 = "not starting.png"

img_1 = Image.open(image_path_1)
img_2 = Image.open(image_path_2)
img_3 = Image.open(image_path_3)
img_4 = Image.open(image_path_4)

# Resize images (optional, adjust to fit your button size)
img_1 = img_1.resize((100, 100))
img_2 = img_2.resize((100, 100))
img_3 = img_3.resize((100, 100))
img_4 = img_4.resize((100, 100))

# Convert images to Tkinter-compatible format
img_button_1 = ImageTk.PhotoImage(img_1)
img_button_2 = ImageTk.PhotoImage(img_2)
img_button_3 = ImageTk.PhotoImage(img_3)
img_button_4 = ImageTk.PhotoImage(img_4)

# Add space for logo
logo_frame = tk.Frame(app, height=150, bg="#F5F5DC")
logo_frame.pack(fill="x")

# Load and display the logo
try:
    # Load the image
    img = Image.open("logo.png")  # Replace 'logo.png' with the path to your logo
    img = img.resize((400, 154))  # Resize if needed
    logo_img = ImageTk.PhotoImage(img)

    # Add the image to the label
    logo_label = tk.Label(logo_frame, image=logo_img, bg="#F5F5DC")
    logo_label.image = logo_img  # Keep a reference to avoid garbage collection
    logo_label.pack(expand=True)
except Exception as e:
    # If image fails to load, show a fallback text
    logo_label = tk.Label(logo_frame, text="Logo Here", font=("Arial", 24), bg="#F5F5DC")
    logo_label.pack(expand=True)

# Buttons to play specific sounds
button_frame = tk.Frame(app)
button_frame.pack(pady=20)

sound1_button = tk.Button(button_frame, image=img_button_1, command=lambda: play_sound("/Users/pooja/Documents/LightWave Systems/Emergency! Please get help.wav", loops=2))
sound1_button.grid(row=0, column=0, padx=10,)

sound2_button = tk.Button(button_frame, image=img_button_2, command=lambda: play_sound("/Users/pooja/Documents/LightWave Systems/Urgent Brake Assistance Needed!.wav", loops=2))
sound2_button.grid(row=0, column=1, padx=10)

sound3_button = tk.Button(button_frame, image=img_button_3, command=lambda: play_sound("/Users/pooja/Documents/LightWave Systems/Preventing Rear-End Collisions_ Troubleshooting Car Start-up.wav",loops=2))
sound3_button.grid(row=0, column=2, padx=10, )

# Button to record and play back sound
record_button = tk.Button(app, image=img_button_4, command=record_sound)
record_button.pack(pady=20)

# Label for status updates
status_label = tk.Label(app, text="Select message you want to send", font=("Arial", 14), fg="blue")
status_label.pack(pady=20)

# Run the app
app.geometry("400x400")
app.mainloop()
