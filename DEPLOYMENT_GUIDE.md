# 🌿 AgriVision Pro - Plant Disease Detection System

A FastAPI-based web application for real-time plant disease detection using TensorFlow Lite models trained on the PlantVillage dataset (38 disease classes). Includes comprehensive treatment recommendations for each detected disease.

## Features

✅ **Real-time Disease Detection** - TensorFlow Lite model for fast, CPU-friendly inference  
✅ **38 Plant Disease Classes** - Trained on PlantVillage dataset covering:
   - Apple (Scab, Black Rot, Cedar Apple Rust)
   - Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

✅ **Treatment Recommendations** - Detailed treatment guidance for every detected disease  
✅ **Modern Web Interface** - Responsive HTML5 UI with drag-and-drop image upload  
✅ **Confidence Scoring** - Visual confidence indicator for predictions  
✅ **Fast Processing** - TFLite optimized model for edge deployment  

## Project Structure

```
Crop_Diagnostic/
├── main.py                          # FastAPI application
├── static/
│   └── index.html                   # Web interface
├── models/
│   └── agrivision_edge_model.tflite # TFLite model (38 classes)
├── requirements.txt                 # Python dependencies
├── run_app.bat                      # Windows startup script
└── README.md                        # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Verify Model File

Ensure the TFLite model is present at:
```
models/agrivision_edge_model.tflite
```

## Running the Application

### Option 1: Windows (Batch Script)
Double-click `run_app.bat` to start the application.

### Option 2: Command Line
```bash
python main.py
```

The application will start on `http://localhost:8000`

### Option 3: Custom Port
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

## Usage

1. **Open Browser**: Navigate to `http://localhost:8000`
2. **Upload Image**: Click the upload area or drag-and-drop a plant image
3. **Initialize Scan**: Click "🔍 Initialize Scan" button
4. **View Results**: 
   - Detected plant and disease
   - Confidence score
   - 💊 **Comprehensive treatment recommendations** below the Initialize Scan button

## Supported Plant Classes (38 Total)

### Class Mapping:
- **0-3**: Apple (Scab, Black Rot, Cedar Rust, Healthy)
- **4**: Blueberry (Healthy)
- **5-6**: Cherry (Powdery Mildew, Healthy)
- **7-10**: Corn (3 diseases, Healthy)
- **11-14**: Grape (Black Rot, Esca, Leaf Blight, Healthy)
- **15**: Orange (Huanglongbing)
- **16-17**: Peach (Bacterial Spot, Healthy)
- **18-19**: Pepper (Bacterial Spot, Healthy)
- **20-22**: Potato (Early Blight, Late Blight, Healthy)
- **23**: Raspberry (Healthy)
- **24**: Soybean (Healthy)
- **25**: Squash (Powdery Mildew)
- **26-27**: Strawberry (Leaf Scorch, Healthy)
- **28-37**: Tomato (8 diseases, Healthy)

## API Endpoints

### POST `/predict`
Upload an image for disease prediction

**Request:**
```bash
curl -X POST "http://localhost:8000/predict" -F "file=@plant.jpg"
```

**Response:**
```json
{
  "success": true,
  "class": 29,
  "confidence": 0.9234,
  "plant": "Tomato",
  "disease": "Early Blight",
  "full_name": "Tomato - Early Blight",
  "confidence_percentage": "92.34%",
  "treatment": [
    "Apply fungicide (Chlorothalonil or Mancozeb) starting at first branch",
    "Repeat every 7-10 days, more frequently in wet weather",
    "Remove lower infected leaves manually",
    ...
  ]
}
```

### GET `/health`
Health check endpoint

```bash
curl http://localhost:8000/health
```

### GET `/`
Serve the web interface

## Treatment Recommendations Feature

Each disease comes with actionable treatment steps including:
- **Fungicide/Pesticide Applications** - Specific product recommendations and schedules
- **Cultural Practices** - Pruning, spacing, irrigation techniques
- **Preventive Measures** - Resistance variety selection, sanitation
- **Environmental Control** - Humidity, air circulation management

Example for Tomato Early Blight:
1. Apply fungicide (Chlorothalonil or Mancozeb) starting at first branch
2. Repeat every 7-10 days, more frequently in wet weather
3. Remove lower infected leaves manually
4. Improve air circulation by removing lower foliage
5. Use drip irrigation instead of overhead
6. Plant certified disease-free seed potatoes
7. Avoid working in field when wet

## Model Details

- **Name**: agrivision_edge_model.tflite
- **Framework**: TensorFlow Lite
- **Training Data**: PlantVillage Dataset
- **Classes**: 38 disease/healthy conditions
- **Input Shape**: 224×224 RGB images (typically)
- **Optimization**: Quantized for edge devices

## Troubleshooting

### Model Not Loading
```
ERROR: Error loading model
```
**Solution**: Ensure `models/agrivision_edge_model.tflite` exists in the correct location.

### Port Already in Use
```
Address already in use
```
**Solution**: Change the port in your command:
```bash
python -m uvicorn main:app --port 8001
```

### Image Upload Issues
**Solution**: 
- Ensure image is under 5MB
- Supported formats: JPG, PNG, GIF
- Image resolution should be reasonable (not too small)

### Low Confidence Predictions
- Ensure the image clearly shows the plant
- Provide images in good lighting
- Multiple angles/views may help verify results

## Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## Performance Tips

1. **GPU Acceleration** (Optional): For faster inference, install TensorFlow GPU:
   ```bash
   pip install tensorflow-gpu==2.13.0
   ```

2. **Model Optimization**: TFLite already provides:
   - Quantization
   - Model compression
   - CPU-optimized inference

3. **Batch Processing**: For multiple images, use the API in a loop

## Deployment Options

### Heroku/Railway
1. Create `Procfile`:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
2. Deploy with git

### Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

Build and run:
```bash
docker build -t agrivision .
docker run -p 8000:8000 agrivision
```

### Local Network Access
Run with:
```bash
python main.py
```
Access from another device using your machine's IP:
```
http://YOUR_IP:8000
```

## Security Notes

- Model path is hardcoded for security
- File upload limited to 5MB
- Input validation on image files
- CORS not enabled (modify if needed for cross-origin requests)

## License

Include your license information here.

## Support

For issues or improvements, please contact the development team.

## Version

**AgriVision Pro v1.0**  
*TensorFlow Lite Edition*  
Released: 2024

---

**Happy farming! 🌾** Let AgriVision Pro help you maintain healthy crops.
