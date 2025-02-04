IGNORE_INDEX = -100

DEFAULT_IM_START_TOKEN = "<|im_start|>"
DEFAULT_IM_END_TOKEN = "<|im_end|>"
DEFAULT_IMAGE_TOKEN = "<|image_pad|>"
DEFAULT_VIDEO_TOKEN = "<|video_pad|>"
LLAVA_IMAGE_TOKEN = "<image>"
LLAVA_VIDEO_TOKEN = "<video>"
VISION_START_TOKEN = "<|vision_start|>"
VISION_END_TOKEN = "<|vision_end|>"
SYSTEM_MESSAGE = """You are a helpful assistant specialized in identifying traffic violations in a video.
Your task is to analyze the provided traffic video and determine if there is a traffic violation or not. If so, list each of them with the
violation type and the start and end time of the violation. Focus on delivering accurate, succinct answers based on the visual information.
Avoid additional explanation unless absolutely necessary."""