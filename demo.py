from ultralytics import YOLO
from risk_engine import assess_risk
from pathlib import Path

# -------------------------------
# AI FACTORY SAFETY SYSTEM
# PPE Detection + Risk Assessment
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR
    / "runs"
    / "detect"
    / "runs"
    / "ppe"
    / "review2"
    / "weights"
    / "best.pt"
)

IMAGE_PATH = (
    BASE_DIR
    / "datasets"
    / "construction-ppe"
    / "images"
    / "test"
    / "image1.jpeg"
)

print("\n========================================")
print("     AI FACTORY SAFETY MONITOR")
print("========================================")

# Check required files
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found:\n{MODEL_PATH}")

if not IMAGE_PATH.exists():
    raise FileNotFoundError(f"Test image not found:\n{IMAGE_PATH}")

print("\nLoading PPE detection model...")

model = YOLO(str(MODEL_PATH))

print("Analyzing factory image...\n")

# Run YOLO detection
results = model.predict(
    source=str(IMAGE_PATH),
    conf=0.20,
    save=True,
    project=str(BASE_DIR / "demo_results"),
    name="ppe_detection",
    exist_ok=True
)

result = results[0]

print("\n========== SAFETY ANALYSIS ==========\n")

if result.boxes is None or len(result.boxes) == 0:
    print("No PPE objects detected.")
    print("Manual safety inspection recommended.")

else:
    for number, box in enumerate(result.boxes, start=1):

        class_id = int(box.cls.item())
        confidence = float(box.conf.item())

        detected_class = model.names[class_id]

        risk = assess_risk(detected_class)

        print(f"Detection #{number}")
        print(f"Object         : {detected_class}")
        print(f"Confidence     : {confidence * 100:.2f}%")
        print(f"Severity       : {risk['severity']}")
        print(f"Recommendation : {risk['recommendation']}")
        print("----------------------------------------")

print("\nAnalysis completed successfully.")

print("\nAnnotated image saved in:")
print(result.save_dir)

print("\n========================================")