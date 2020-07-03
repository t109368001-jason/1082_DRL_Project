from convert import images_to_video
from convert import state_list_to_image

_index = 6000000
_reward = 8925
_steps = 35
_fps = 10.0
_resolution = (640, 640)
_map_filepath = '../image/map.png'
_output_dir = '../output/'


def state_list_to_video(index, reward, steps, fps, resolution, map_filepath, output_dir):
    state_list_to_image.state_list_to_image(index, reward, steps, map_filepath, output_dir)
    images_to_video.images_to_video(index, reward, steps, fps, resolution, output_dir)


state_list_to_video(_index, _reward, _steps, _fps, _resolution, _map_filepath, _output_dir)
