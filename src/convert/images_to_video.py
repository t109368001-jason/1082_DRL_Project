import os

import cv2

_index = 0
_fps = 10
_resolution = (640, 640)


def images_to_video(epoch, reward, steps, fps=10, resolution=(640, 640), output_dir='../output/'):
    image_folder = '{}/{}/'.format(output_dir, epoch)
    video_name = '{}/{}_{:.0f}_{}.mp4'.format(output_dir, epoch, reward, steps)
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    def comp(filename):
        return int(filename.split('.')[0])

    images.sort(key=comp)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    frame = cv2.resize(frame, resolution)
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = cv2.resize(frame, resolution)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()
