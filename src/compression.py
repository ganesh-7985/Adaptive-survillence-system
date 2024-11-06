import ffmpeg

# def compress_video(input_folder, output_file):
#     output_path = f'/Users/shankarganesh/Desktop/asc/output/{output_file}'
#     (
#         ffmpeg
#         .input(f'{input_folder}/*.jpg', pattern_type='glob', framerate=30)
#         .output(output_path, vcodec='libx265', crf=28)
#         .run()
#     )

def compress_video(input_folder, output_file):
    output_path = f'/Users/shankarganesh/Desktop/asc/output/{output_file}'
    (
        ffmpeg
        .input(f'{input_folder}/*.jpg', pattern_type='glob', framerate=30, analyzeduration=10000000, probesize=5000000)
        .output(output_path, vcodec='libx265', crf=28)
        .run()
    )
