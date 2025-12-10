"""
Setup script for Streamlit Cloud deployment

This script is automatically run by Streamlit Cloud during deployment.
It downloads and caches the model before the app starts.
"""

import os
from transformers import pipeline

# Configuration
MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"
TASK = "text-classification"
MODEL_CACHE_DIR = "./model_cache"

def setup_model():
    """Download and cache the model for Streamlit Cloud."""
    print("🚀 Streamlit Cloud: Setting up model...")
    
    # Create cache directory
    os.makedirs(MODEL_CACHE_DIR, exist_ok=True)
    
    # Set cache directory
    os.environ['TRANSFORMERS_CACHE'] = MODEL_CACHE_DIR
    os.environ['HF_HOME'] = MODEL_CACHE_DIR
    
    try:
        print(f"📥 Downloading model: {MODEL_NAME}")
        print("⏳ This will only happen once during deployment...")
        
        # Download and cache the model
        classifier = pipeline(
            task=TASK,
            model=MODEL_NAME,
            device=-1  # CPU only
        )
        
        # Test the model
        test_result = classifier("This is a test.", top_k=None)
        print(f"✅ Model ready! Test result: {test_result[0][0]['label']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up model: {e}")
        return False

if __name__ == "__main__":
    success = setup_model()
    exit(0 if success else 1)
