"""
Pre-download model script

This script downloads and caches the Hugging Face model locally
so that users don't need to download it every time the app starts.

Run this script once before deploying or running the app:
    python download_model.py
"""

from transformers import pipeline
import os

# Configuration
MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"
TASK = "text-classification"
MODEL_CACHE_DIR = "./model_cache"

def download_model():
    """Download and cache the model locally."""
    print(f"📥 Downloading model: {MODEL_NAME}")
    print(f"📁 Cache directory: {MODEL_CACHE_DIR}")
    
    # Create cache directory
    os.makedirs(MODEL_CACHE_DIR, exist_ok=True)
    
    # Set the Hugging Face cache directory via environment variable
    os.environ['TRANSFORMERS_CACHE'] = MODEL_CACHE_DIR
    
    try:
        # Download model
        print("⏳ This may take a few minutes on first run...")
        classifier = pipeline(
            task=TASK,
            model=MODEL_NAME,
            device=-1  # CPU
        )
        
        # Test the model
        print("\n🧪 Testing model...")
        test_text = "This is a test sentence to verify the model works correctly."
        result = classifier(test_text)
        print(f"✅ Model test successful!")
        print(f"   Result: {result}")
        
        print(f"\n✅ Model downloaded and cached successfully!")
        print(f"📁 Cache location: {os.path.abspath(MODEL_CACHE_DIR)}")
        print(f"\n💡 You can now run: streamlit run app.py")
        
    except Exception as e:
        print(f"\n❌ Error downloading model: {e}")
        print("\nTroubleshooting:")
        print("- Check your internet connection")
        print("- Ensure you have enough disk space (~1.5GB)")
        print("- Try running: pip install --upgrade transformers torch")
        raise

if __name__ == "__main__":
    download_model()
