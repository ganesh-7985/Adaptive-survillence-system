import ffmpeg

def compress_video(input_folder, output_file):
    (
        ffmpeg
        .input(f'{input_folder}/*.jpg', pattern_type='glob', framerate=30)
        .output(f'../output/{output_file}', vcodec='libx265', crf=28)
        .run()
    )
