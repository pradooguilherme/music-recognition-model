import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
import librosa
import librosa.display
import os

directory_Classic_Music = '/home/pradooguilherme/PycharmProjects/PythonProject1/music/classic-music'
directory_Electronic_Music = '/home/pradooguilherme/PycharmProjects/PythonProject1/music/electronic-music'

output_directory = '/home/pradooguilherme/PycharmProjects/PythonProject1/music/output-audio'

a = 0

for filename in os.listdir(directory_Classic_Music):

    if filename.endswith(".mp3"):
        file_path = os.path.join(directory_Classic_Music, filename)

        data, fs = librosa.load(file_path, sr=None)

        plt.figure(figsize=(12,5))
        D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
        librosa.display.specshow(D, cmap='jet')

        output_file_path = os.path.join(output_directory, f'{a}classic_music_spectrogram.png')
        plt.savefig(output_file_path)

        plt.close()
        a = a + 1

for filename in os.listdir(directory_Electronic_Music):

    if filename.endswith(".mp3"):
        file_path = os.path.join(directory_Electronic_Music, filename)

        data, fs = librosa.load(file_path, sr=None)

        plt.figure(figsize=(12,5))
        D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
        librosa.display.specshow(D, cmap='jet')

        output_file_path = os.path.join(output_directory, f'{a}electronic_music_spectrogram.png')
        plt.savefig(output_file_path)

        plt.close()
        a = a + 1