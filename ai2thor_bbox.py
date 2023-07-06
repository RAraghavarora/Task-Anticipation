from PIL import Image, ImageDraw
from ai2thor.controller import Controller
import ai2thor
print(ai2thor.__version__)
from ai2thor.platform import CloudRendering
from ai2thor.video_controller import VideoController
import cv2
import numpy as np

controller = Controller(platform=CloudRendering, renderInstanceSegmentation=True, scene='FloorPlan1', width=720, height=720, fieldOfView=90)
event = controller.step(
    action="GetReachablePositions"
)
frames = []
for _ in range(90//5):
    frames.append(controller.step(action="RotateLeft", degrees=5).frame)

event = controller.step(
    action='SetObjectStates', 
    SetObjectStates={
            'objectType': 'Bottle',
            'stateChange': 'canFillWithLiquid', 
            'isFilledWithLiquid': True,
        }
)

mask = np.array(event.instance_masks.mask('HousePlant|-01.95|+00.89|-02.52'))
detec = event.instance_detections2D
frame = event.frame

# Convert the instance segmentation frame to an image
segmentation_img = Image.fromarray(frame.astype(np.uint8))

# Create a new image with the bounding boxes
bbox_img = segmentation_img.copy()
draw = ImageDraw.Draw(bbox_img)

# Iterate over the detections and draw bounding boxes
obj_ids = [
    'Stove|0|0|0',
    'Window|-0.54|2.595|-1.5',
    'CoffeeMachine|-01.98|+00.90|-00.19',
    'Microwave|-00.24|+01.69|-02.53',
    'Apple|-00.47|+01.15|+00.48',
    'Tomato|-00.39|+01.14|-00.81',
    'HousePlant|-01.95|+00.89|-02.52',
]
for obj_id in obj_ids:
    detection = detec[obj_id]
    x1, y1, x2, y2 = detection
    label = obj_id
    draw.rectangle([(x1, y1), (x2, y2)], outline='red')
    draw.text((x1, y1-10), label, fill='green')

# Save the image with bounding boxes
bbox_img.save('bounding_boxes.png')


import numpy as np
from PIL import Image

mask = np.array(event.instance_masks.mask('Bread|-00.52|+01.17|-00.03'))
mask_img = Image.fromarray(mask.astype(np.uint8)*255)

mask = np.stack((mask,)*3, axis=-1)
image = event.cv2img
resultant = image*mask
inverse_mask = 1 - mask
inverse_mask = np.stack((inverse_mask,)*3, axis=-1)
background = 255 * inverse_mask
background = background[:, :, :, 0]
print(background.shape)
background = background.astype(np.uint8) # Convert data type to uint8
resultant += background

cv2.imwrite('mask.png', resultant)