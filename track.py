import datetime
import piexif
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from ultralytics import YOLO

# Load an official or custom model
model = YOLO('yolov8n.pt')  # Load an official Detect model
# model = YOLO('yolov8n-pose.pt')  # Load an official Pose model

# Perform tracking with the model
results = model.track(source="2023SkiMaal.mp4", show=True, stream=True, tracker='ski_tracker.yaml')
posFinishLine = 0.8 # position of the finish line, horisontal line at % of the height

crossedLineList = [] # list of people who crossed the line
for result in results:
    boxes = result.boxes
    if boxes:
        class_values = boxes.cls
        for y in range(len(class_values)):
            if class_values[y] == 0: # identify person
                try:
                    xyxyn = boxes.xyxyn[y]
                    yLowerPosition = xyxyn.tolist()[3]

                    id = boxes.id[y]
                    if yLowerPosition >= posFinishLine:
                        if not id in crossedLineList:
                            crossedLineList.append(id)
                            print(f"A person crossed the line! ID: {boxes.id[y]}, position: {xyxyn}")
                            # Show the results
                            im_array = result.plot()  # plot a BGR numpy array of predictions
                            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
                            # set a timestamp with font size 50
                            draw = ImageDraw.Draw(im)

                            # draw an horisontal line across the image to illustrate the finish line
                            draw.line((50, posFinishLine * im.size[1], im.size[0] - 50, posFinishLine * im.size[1]), fill=(255, 255, 0), width=3)
                            
                            # set the font size and color
                            font_size = 50
                            font_color = (255, 0, 0)  # red
                            font = ImageFont.truetype("arial.ttf", font_size)

                            # get the current time
                            current_time = datetime.datetime.now()
                            time_text = current_time.strftime('%Y:%m:%d %H:%M:%S')

                            draw.text((50, 50), time_text, font=font, fill=font_color)

                            # crop to only person in box
                            xyxy = boxes.xyxy[y]
                            imCrop = im.crop((xyxy.tolist()[0], xyxy.tolist()[1], xyxy.tolist()[2], xyxy.tolist()[3]))

                            # set the place
                            place = "Mål"

                            # create the EXIF data and convert to bytes
                            exif_dict = {"0th": {piexif.ImageIFD.ImageDescription: time_text,
                                                piexif.ImageIFD.Artist: place}}
                            exif_bytes = piexif.dump(exif_dict)

                            # im.show()  # show image
                            im.save(f"results{id}.jpg", exif=exif_bytes)  # save image to file - full size
                            imCrop.save(f"results{id}_crop.jpg", exif=exif_bytes)
                            
                except TypeError as e:
                    print(f"TypeError: {e}")
                    pass # ignore
