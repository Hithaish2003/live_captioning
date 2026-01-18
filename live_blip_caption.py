import cv2
import time
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8s.pt")

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

# Video Writer
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

out = cv2.VideoWriter(
    "scene_description_output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (frame_width, frame_height)
)

prev_time = 0
caption = "Analyzing scene..."

print("Recording started... Press 'q' to stop.")

# Caption generator
def generate_caption(objects):
    if "person" in objects:
        if "bottle" in objects:
            return "A person holding a bottle"
        elif "teddy bear" in objects:
            return "A person holding a teddy bear"
        elif "cell phone" in objects:
            return "A person using a mobile phone"
        elif "remote" in objects:
            return "A person holding a remote control"
        else:
            return "A person is present"
    else:
        return "No person detected"

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if time.time() - prev_time > 1:
        prev_time = time.time()

        results = model(frame, conf=0.6, iou=0.5, verbose=False)
        detected_objects = set()

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                detected_objects.add(model.names[cls_id])

        caption = generate_caption(detected_objects)

    # Overlay caption
    cv2.rectangle(frame, (10, 10), (frame_width - 10, 60), (0, 0, 0), -1)
    cv2.putText(frame, caption, (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Scene Description Captioning", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Saved as scene_description_output.mp4")
