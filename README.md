# CraftCortex: CNN-Based Origami Recognition and Tutorial Curation

A web application that classifies origami creations from uploaded images using a custom-trained CNN model based on MobileNetV2 architecture. The application provides real-time classification with 76% accuracy and automatically scrapes relevant YouTube tutorials and Pinterest ideas for the predicted origami type.

![CraftCortex](https://github.com/user-attachments/assets/4e60994f-7654-47ec-a779-084ef0cdb7f9)

## Project Overview

CraftCortex represents a complete end-to-end machine learning pipeline, from data collection to deployment. The project evolved through multiple iterations, ultimately achieving a 245.45% improvement in accuracy from initial attempts.

### Key Features
- **Image Classification**: 76% accuracy on complex origami dataset with 3,657 training images
- **Automated Tutorial Discovery**: Real-time scraping of YouTube and Pinterest for relevant tutorials
- **Web Interface**: Clean Flask-based UI for easy image upload and classification
- **Robust Error Handling**: Graceful failure management and compatibility layers

## Technical Architecture

### Model Development
1. **Custom CNN**: Initial attempt with basic architecture achieved 22% accuracy
2. **Transfer Learning**: Switched to MobileNetV2 pre-trained weights, achieving ~60% accuracy
3. **Data Augmentation**: Enhanced performance through rotation, flipping, and geometric transformations
4. **EfficientNet Experiment**: Brief exploration of EfficientNetB0 resulted in 13% accuracy (abandoned)
5. **Optimized MobileNetV2**: Final model with hyperparameter tuning reached 76% accuracy

### Dataset Characteristics
- **Size**: 3,657 training images across multiple categories
- **Complexity**: Wide variety from simple cranes to complex dragons with 47+ individual scales
- **Challenges**: Varying lighting conditions, backgrounds, folding quality, and geometric complexity

### Model Architecture
- **Base Model**: MobileNetV2 with pre-trained ImageNet weights
- **Input Shape**: 128x128x3 RGB images
- **Training Strategy**: Transfer learning with strategic layer unfreezing
- **Optimization**: Learning rate scheduling, batch size optimization, early stopping

## Demonstration
A detailed demonstration of the complete application workflow can be viewed here:
[CraftCortex Demo Video](https://vimeo.com/1089616246/282b95b981)


The demo showcases:
- Real-time image upload and classification
- Live tutorial scraping from Pinterest and YouTube
- Complete Flask interface functionality

## Repository Structure

### Core Files

- **`app.py`**: Main Flask application server for running the web interface locally
- **`index.html`** (in `templates/`): HTML template for the web interface UI
- **`ModelTraining.ipynb`**: Jupyter notebook containing the complete model training pipeline and experimentation
- **`CraftCortex.h5`**: Trained and saved model
- **`label_encoder.pkl`**: Serialized label encoder for class predictions

### Utility Scripts
- **`get-pip.py`**: Python package installer utility
- **`pinterest_search.py`**: Web scraping module for Pinterest tutorial discovery
- **`youtube_search.py`**: YouTube API integration for tutorial recommendations

## Dataset Information

The model was trained on the **Origami Models Dataset** available on Kaggle:
- **Dataset URL**: https://www.kaggle.com/datasets/karthikssalian/origami-models/data
- **Size**: 3,657 images across multiple origami categories
- **Complexity**: Ranges from simple cranes to intricate dragons with detailed geometric patterns
- **Preprocessing**: Images standardized to 128x128 RGB format with data augmentation

## Setup

### Prerequisites
- Python 3.8+
- Virtual environment support
- Chrome browser (for Selenium web scraping)
- Kaggle account (for dataset access)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone [your_repository_url]
    cd [your_project_directory]
    ```

2. **Create and activate virtual environment:**
    ```bash
    python -m venv tf-env
    
    # On Windows:
    .\tf-env\Scripts\activate
    
    # On macOS/Linux:
    source tf-env/bin/activate
    ```

3. **Install dependencies:**

   The versions are noted in requirements.txt
   
   ```bash
    pip install Flask tensorflow keras scikit-learn opencv-python selenium webdriver-manager
    ```

5. **Setup project structure:**
    ```bash
    mkdir uploads templates static
    ```

6. **Place model files:**
    - Ensure `CraftCortex.h5` (trained model) is in the root directory
    - Ensure `label_encoder.pkl` (label encoder) is in the root directory
    - Place `index.html` in the `templates/` directory

## Running the Application

1. **Activate virtual environment:**
    ```bash
    # Windows:
    .\tf-env\Scripts\activate
    
    # macOS/Linux:
    source tf-env/bin/activate
    ```

2. **Start the Flask server:**
    ```bash
    python app.py
    ```

3. **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:5000`

## Technical Implementation Details

### Web Scraping Architecture
The application uses advanced Selenium configurations to bypass bot detection:
```python
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--window-size=1920,1080')
options.add_argument('--user-agent=Mozilla/5.0...')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
```

### Model Compatibility
Custom compatibility layers handle TensorFlow version conflicts:
- Support for TensorFlow 2.10+ through 2.16+
- Custom dtype policy management
- Graceful degradation for older versions

### Data Augmentation Pipeline
```python
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)
```

## Performance Metrics

| Metric | Value |
|--------|-------|
| **Final Accuracy** | 76% |
| **Training Images** | 3,657 |
| **Improvement** | 245.45% from initial attempt |
| **Categories** | Multiple (apples, cranes, flowers, etc.) |
| **Processing Time** | ~5-10 seconds per image (CPU) |

## Libraries and Dependencies

### Core ML Stack
- **TensorFlow/Keras**: Deep learning framework and high-level API
- **scikit-learn**: Label encoding and preprocessing utilities
- **OpenCV**: Image processing and computer vision operations
- **NumPy**: Numerical computing foundation

### Web Framework
- **Flask**: Lightweight web application framework
- **Werkzeug**: WSGI utilities and secure filename handling

### Web Scraping
- **Selenium**: Automated browser control for tutorial scraping
- **WebDriver Manager**: Automatic browser driver management

### Data Processing
- **PIL/Pillow**: Image manipulation and processing
- **pickle**: Model serialization and deserialization

## Troubleshooting

### Common Issues
1. **TensorFlow Version Conflicts**: Ensure compatible TensorFlow version (2.10+)
2. **Missing Dependencies**: Install all requirements in virtual environment
3. **Chrome Driver Issues**: Update Chrome and chromedriver versions
4. **Model Loading Errors**: Verify model file integrity and path

---

**Note**: This application demonstrates a complete end-to-end machine learning pipeline. While achieving 76% accuracy on complex origami classification, it represents a significant technical achievement in transfer learning, web scraping integration, and full-stack development.

[*"Sometimes the best projects teach you that initial plans were adorably naive, but persistence, proper tools, and a healthy relationship with error messages can transform optimistic beginnings into genuinely useful reality."*](https://medium.com/@manyapandey7842/the-76-solution-why-perfect-ai-is-the-enemy-of-good-ai-5861d9f550c1)
