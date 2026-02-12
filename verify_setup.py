"""
AgriVision Pro - Setup Verification Script
Checks that all required files and dependencies are in place
"""

import os
import sys

def check_file_exists(path, description):
    """Check if a file exists"""
    if os.path.exists(path):
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ MISSING {description}: {path}")
        return False

def check_module(module_name, description):
    """Check if a Python module is installed"""
    try:
        __import__(module_name)
        print(f"✓ {description}: {module_name}")
        return True
    except ImportError:
        print(f"✗ MISSING {description}: {module_name}")
        return False

def main():
    print("=" * 60)
    print("AgriVision Pro - Setup Verification")
    print("=" * 60)
    print()

    all_good = True

    # Check files
    print("📁 Checking Project Files:")
    print("-" * 60)
    all_good &= check_file_exists("main.py", "FastAPI Application")
    all_good &= check_file_exists("static/index.html", "Web Interface")
    all_good &= check_file_exists("models/agrivision_edge_model.tflite", "TFLite Model")
    all_good &= check_file_exists("requirements.txt", "Requirements file")
    print()

    # Check Python modules
    print("📦 Checking Python Dependencies:")
    print("-" * 60)
    all_good &= check_module("fastapi", "FastAPI")
    all_good &= check_module("uvicorn", "Uvicorn")
    all_good &= check_module("tensorflow", "TensorFlow")
    all_good &= check_module("PIL", "Pillow")
    all_good &= check_module("numpy", "NumPy")
    all_good &= check_module("cv2", "OpenCV (optional)")
    print()

    # Check model details
    if os.path.exists("models/agrivision_edge_model.tflite"):
        print("🔍 Model Information:")
        print("-" * 60)
        try:
            import tensorflow as tf
            interpreter = tf.lite.Interpreter(model_path="models/agrivision_edge_model.tflite")
            interpreter.allocate_tensors()
            
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            
            print(f"✓ Model Loaded Successfully")
            print(f"  Input Shape: {input_details[0]['shape']}")
            print(f"  Input Type: {input_details[0]['dtype']}")
            print(f"  Output Shape: {output_details[0]['shape']}")
            print(f"  Output Type: {output_details[0]['dtype']}")
            print()
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            all_good = False
    
    # Summary
    print("=" * 60)
    if all_good:
        print("✓ All checks passed! Ready to run AgriVision Pro")
        print()
        print("To start the application, run:")
        print("  python main.py")
        print()
        print("Then open http://localhost:8000 in your browser")
    else:
        print("✗ Some checks failed. Please install missing dependencies:")
        print("  pip install -r requirements.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()
