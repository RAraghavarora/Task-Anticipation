from ai2thor.controller import Controller
import ai2thor
print(ai2thor.__version__)
from ai2thor.platform import CloudRendering
from ai2thor.video_controller import VideoController
import cv2
import numpy as np

def save_video(frames, filename='video.mp4', fps=20):
    import cv2
    size = frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, fps, size)

    for i in range(len(frames)):
        frame = frames[i]
        image_with_text = frame.copy()
        out.write(frames[i])

    out.release()
    cv2.destroyAllWindows()

def save_gif(frames, filename='animation.gif', duration=0.1):
    from PIL import Image

    # Convert frames to PIL Image objects
    image_frames = [Image.fromarray(frame) for frame in frames]

    # Save frames as GIF
    image_frames[0].save(
        filename,
        save_all=True,
        append_images=image_frames[1:],
        optimize=False,
        duration=int(duration * 1000),
        loop=0
    )

def write_image(frame, agent_pos):
    image_with_text = np.array(frame, copy=True)
    image_with_text = cv2.cvtColor(image_with_text, cv2.COLOR_BGR2RGB)
    text_position = (image_with_text.shape[1] - 250, image_with_text.shape[0] - 20)
    text_content = f"Agent Position: ({agent_pos['x']}, {round(agent_pos['y'], 2)}, {round(agent_pos['z'],2)})"
    font_scale = 0.4
    font_thickness = max(1, int(font_scale * 1.5))
    cv2.putText(image_with_text, text_content, text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,0,0), font_thickness, cv2.LINE_AA)
    return image_with_text


controller = Controller(platform=CloudRendering, scene='FloorPlan1')
frames = []
positions = controller.step(
    action="GetReachablePositions"
).metadata["actionReturn"]
frames.append(controller.last_event.frame)
fridge_instance = [obj for obj in controller.last_event.metadata["objects"] if "Fridge" in obj['objectId']]
obj_id = fridge_instance[0]['objectId']
event = controller.step(dict(action='OpenObject', objectId=obj_id))
frames.append(event.frame)
obj_in_fridge = [obj for obj in controller.last_event.metadata["objects"] if obj['parentReceptacles'] == [obj_id]]
event = controller.step(dict(action='PickupObject', objectId=obj_in_fridge[0]['objectId']))
frames.append(event.frame)
event = controller.step(dict(action='CloseObject', objectId=obj_id))
frames.append(event.frame)


for _ in range(90//5):
    frames.append(controller.step(action="RotateLeft", degrees=5).frame)

for _ in range(10):
    event = controller.step(action="MoveAhead")
    frames.append(write_image(event.cv2img, event.metadata['agent']['position']))

for _ in range(7):
    event = controller.step(dict(action='MoveLeft'))
    frames.append(write_image(event.cv2img, event.metadata['agent']['position']))

pan = [obj for obj in controller.last_event.metadata['objects'] if 'Pan' in obj['objectId']][0]
event = controller.step(dict(action='PutObject', objectId=pan['objectId']))
# print(event)
frames.append(event.frame)

event = controller.step(action="SliceObject", objectId=obj_in_fridge[0]['objectId'])
frames.append(event.frame)
event = controller.step(dict(action='PickupObject', objectId=pan['objectId']))
frames.append(event.frame)

for _ in range(4):
    event = controller.step(dict(action='MoveRight'))
    frames.append(write_image(event.cv2img, event.metadata['agent']['position']))


stove_burners = [obj for obj in event.metadata['objects'] if 'StoveBurner' in obj['objectId']]
stove_knobs = [obj for obj in event.metadata['objects'] if 'StoveKnob' in obj['objectId']]

event = controller.step(dict(action='PutObject', objectId=stove_burners[0]['objectId']))
frames.append(event.frame)

for _ in range(3):
    event = controller.step(action="MoveAhead")
    frames.append(write_image(event.cv2img, event.metadata['agent']['position']))


event = controller.step(dict(action='ToggleObjectOn', objectId=stove_knobs[2]['objectId']))
frames.append(event.frame)
event = controller.step(dict(action='LookDown'))
frames.append(event.frame)

event = controller.step(dict(action='ToggleObjectOn', objectId=stove_knobs[2]['objectId']))
frames.append(event.frame)


# save_video(frames, filename='video.mp4', fps=1)
save_gif(frames, 'animation.gif')