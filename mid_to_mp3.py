import os
import subprocess
import concurrent.futures
import multiprocessing

def convert_mid_to_mp3(mid_file, output_directory):
    # Define the .mp3 output file path
    mp3_file = os.path.join(output_directory, os.path.basename(mid_file).replace('.mid', '.mp3'))

    # Use timidity to convert .mid to .wav and then ffmpeg to convert .wav to .mp3
    wav_file = mid_file.replace('.mid', '.wav')
    subprocess.run(['timidity', mid_file, '-Ow', '-o', wav_file])

    # Convert the .wav file to .mp3 using ffmpeg
    subprocess.run(['ffmpeg', '-i', wav_file, mp3_file])

    # Remove the intermediate .wav file
    os.remove(wav_file)

def main():
    # Define the directory containing the .mid files and the output directory
    input_directory = os.path.dirname(os.path.realpath(__file__))
    output_directory = os.path.join(input_directory, 'MP3')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get all .mid files in the input directory
    mid_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.mid')]

    # Calculate the number of workers to use (2/3 of the total core count)
    num_workers = max(1, 2 * multiprocessing.cpu_count() // 3)

    # Use ThreadPoolExecutor to parallelize the conversion process
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        executor.map(lambda mid_file: convert_mid_to_mp3(mid_file, output_directory), mid_files)

    print("Conversion completed successfully.")

if __name__ == '__main__':
    main()
