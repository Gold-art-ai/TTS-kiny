import tkinter as tk
from tkinter import messagebox
import asyncio
import edge_tts
import tempfile
import os
import threading

# The fixed async function
async def speak_sw(text):
    try:
        # 1. Update your library first! (pip install --upgrade edge-tts)
        # 2. We use 'sw-KE-RafikiNeural' for phonetic similarity to Kinyarwanda
        communicate = edge_tts.Communicate(text, voice="sw-KE-RafikiNeural")
        
        # Create a temp file path safely
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "kinyarwanda_audio.mp3")

        # Save the audio
        await communicate.save(temp_path)

        # Play audio (Windows command)
        os.system(f'start "" "{temp_path}"')
        
    except Exception as e:
        # This will now catch the specific '403 Forbidden' or 'NoAudioReceived' error
        messagebox.showerror("System Error", f"Error from Microsoft: {str(e)}")

def start_speaking_thread():
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Error", "Injiza amagambo mbere!")
        return
    threading.Thread(target=lambda: asyncio.run(speak_sw(text)), daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Kinyarwanda TTS Fix")
root.geometry("400x200")

tk.Label(root, text="Injiza amagambo y'ikinyarwanda:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.insert(0, "Amakuru yanyu?")

btn = tk.Button(root, text="Vuga", command=start_speaking_thread, bg="green", fg="white")
btn.pack(pady=20)

root.mainloop()