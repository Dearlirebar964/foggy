# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
utils/ initialization
"""


def notebook_init():
    # For use in YOLOv5 notebooks
    print('Checking setup...')
    from IPython.display import clear_output  # to display images
    from utils.general import emojis
    from utils.torch_utils import select_device  # YOLOv5 imports

    clear_output()
    select_device(newline=False)
    print(emojis('Setup complete ✅'))
