import os

# Create a virtual environment named 'object_detection_env'
os.system('python3 -m venv object_detection_env')

# Check if the virtual environment was created successfully
if os.path.exists('object_detection_env'):
    print("Virtual environment created successfully.")
else:
    print("Failed to create virtual environment.")

# Activate the virtual environment and install required libraries
activation_command = 'source object_detection_env/bin/activate && '
install_command = activation_command + 'pip install ultralytics'
os.system(install_command)

print(os.path)

print("Step 1 okay")



from ultralytics import YOLO

print("Step 2 okay")
# Load a pretrained YOLO model (e.g., yolov8n.pt)
model = YOLO("yolov8n.pt")
results = model.predict(source=0, show =True)

""" print("Step 3 okay")
# Perform object detection on an image
results = model("https://ultralytics.com/images/bus.jpg")

# Visualize results
for result in results:
    result.show() """

#results = model.predict(source=0, show =True)
print(results)