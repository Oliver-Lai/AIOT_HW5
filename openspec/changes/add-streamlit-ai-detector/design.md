# Design: AI vs Human Text Detector

## Architecture Overview

This is a single-page web application built with Streamlit that integrates a pre-trained machine learning model for text classification. The architecture follows a simple client-server pattern where Streamlit handles both the frontend and backend.

```
┌─────────────────────────────────────────────────┐
│           Streamlit Application                  │
│  ┌───────────────────────────────────────────┐  │
│  │  User Interface Layer                      │  │
│  │  - Text input widget                       │  │
│  │  - Analysis button                         │  │
│  │  - Progress bars & status messages         │  │
│  └───────────────────────────────────────────┘  │
│                     │                            │
│                     ▼                            │
│  ┌───────────────────────────────────────────┐  │
│  │  Application Logic Layer                   │  │
│  │  - Input validation                        │  │
│  │  - Result interpretation                   │  │
│  │  - UI state management                     │  │
│  └───────────────────────────────────────────┘  │
│                     │                            │
│                     ▼                            │
│  ┌───────────────────────────────────────────┐  │
│  │  Model Layer (Cached)                      │  │
│  │  - Hugging Face pipeline                   │  │
│  │  - RoBERTa model inference                 │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

## Component Design

### 1. Model Loading (`load_model`)
- **Purpose**: Load and cache the Hugging Face model pipeline
- **Implementation**: Decorated with `@st.cache_resource` to ensure single initialization
- **Model**: "Hello-SimpleAI/chatgpt-detector-roberta"
- **Pipeline Type**: "text-classification"
- **Return Type**: Hugging Face pipeline object

**Rationale**: Using `@st.cache_resource` instead of `@st.cache` or `@st.cache_data` because:
- The model is a non-serializable resource (PyTorch/TensorFlow model)
- Should be loaded once per session and shared across reruns
- Critical for Streamlit Cloud memory management

### 2. Text Analysis (`analyze_text`)
- **Purpose**: Process text through the model and return structured results
- **Input**: String (user-provided text)
- **Output**: Dictionary with keys: `ai_probability`, `human_probability`, `classification`, `confidence_level`
- **Classification Logic**:
  - "AI Generated": AI probability > 70%
  - "Human Written": Human probability > 70%
  - "Mixed/Uncertain": Neither exceeds 70%

**Rationale**: Providing structured output makes it easier to render different UI components and add future enhancements like logging or analytics.

### 3. User Interface Components

#### Input Section
- **Title**: "AI Content Detector" (h1)
- **Subtitle**: Brief description of functionality
- **Text Area**: `st.text_area` with placeholder text
- **Character Limit**: Recommended 5000 characters (configurable)
- **Button**: "Analyze Text" triggers analysis

#### Results Section
- **Progress Bar**: `st.progress` showing AI probability (0.0 to 1.0)
- **Percentage Display**: Large text showing "XX% AI Generated" or "XX% Human Written"
- **Status Message**: 
  - `st.success` for Human (> 70%)
  - `st.warning` for Mixed (30-70%)
  - `st.error` for AI (> 70%)
- **Confidence Indicator**: Additional context on prediction reliability

## Data Flow

1. **User Input**: User pastes text into text area
2. **Validation**: Check for empty input → display error if invalid
3. **Model Loading**: Cached pipeline loads (only first time)
4. **Inference**: Text passed to pipeline → returns label scores
5. **Processing**: Extract probabilities for "ChatGPT" and "Human" labels
6. **Normalization**: Convert scores to percentages
7. **Classification**: Determine category based on thresholds
8. **Display**: Render progress bars and status messages

## Error Handling Strategy

### User Input Errors
- Empty text → `st.error("Please enter some text to analyze")`
- Text too long (>5000 chars) → `st.warning("Text is very long, results may take longer")`

### Model Errors
- Model loading failure → Display friendly error with troubleshooting tips
- Inference timeout → Show loading spinner with timeout message
- Unexpected output format → Fallback to displaying raw probabilities

### Deployment Errors
- Memory issues → Use `@st.cache_resource` and consider model quantization if needed
- Missing dependencies → Comprehensive `requirements.txt` with pinned versions

## Performance Considerations

### Model Optimization
- **Caching**: `@st.cache_resource` prevents re-loading on every interaction
- **Device Selection**: Use CPU for Streamlit Cloud (GPU not available)
- **Batch Size**: Single input processing (no batching needed)

### UI Responsiveness
- **Loading Indicators**: `st.spinner` during model inference
- **Async Considerations**: Streamlit runs synchronously; ensure inference < 10 seconds
- **State Management**: Minimal session state (input text only)

### Memory Management
- Model stays in memory after first load (RAM footprint ~500MB for RoBERTa)
- No persistent data storage (stateless application)
- Clear large variables after use if needed

## Configuration

### Thresholds (Configurable Constants)
```python
AI_THRESHOLD = 0.70        # 70% for "AI Generated"
HUMAN_THRESHOLD = 0.70     # 70% for "Human Written"
MAX_CHAR_LIMIT = 5000      # Maximum input length
```

### Model Configuration
```python
MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"
TASK = "text-classification"
DEVICE = -1  # CPU (0 for GPU if available)
```

## UI/UX Design Decisions

### Color Scheme
- **Green** (`st.success`): Human written content (positive)
- **Yellow** (`st.warning`): Mixed/Uncertain (neutral)
- **Red** (`st.error`): AI generated (alert)

**Rationale**: Familiar traffic light metaphor for quick understanding

### Progress Bar
- Shows AI probability as a visual gauge
- Complements numerical percentage display
- Provides immediate visual feedback

### Text Area Sizing
- Height: 200px (approximately 10 lines)
- Allows comfortable paste of medium-length text
- Scrollable for longer content

## Testing Strategy

### Unit Testing (Future Enhancement)
- Test `analyze_text` with known AI/human samples
- Validate probability calculations
- Test edge cases (empty strings, special characters)

### Manual Testing Checklist
1. Empty input handling
2. Very short text (< 10 words)
3. Medium text (100-500 words)
4. Long text (> 1000 words)
5. Special characters and unicode
6. Known AI-generated text (ChatGPT output)
7. Known human-written text (literature excerpts)

### Deployment Testing
1. Verify model loads on Streamlit Cloud
2. Check memory usage stays under limits
3. Test first-run vs subsequent-run performance
4. Validate UI rendering across devices (desktop, mobile)

## Security Considerations

### Input Validation
- No code execution risk (text-only processing)
- No SQL injection risk (no database)
- XSS prevention via Streamlit's built-in sanitization

### Model Security
- Using official Hugging Face model (trusted source)
- No user data persistence or logging
- No sensitive information required

### Privacy
- Text processed in-memory only
- No data sent to external APIs beyond Hugging Face model download
- Recommend adding privacy notice in UI

## Future Enhancements (Out of Current Scope)

1. **Batch Processing**: Upload text files for analysis
2. **Model Comparison**: Compare multiple detector models
3. **Detailed Analysis**: Highlight specific sentences with high AI probability
4. **History**: Store recent analyses in browser local storage
5. **Export Results**: Download analysis report as PDF/JSON
6. **API Mode**: REST API for programmatic access
7. **Fine-tuning**: Allow users to provide feedback for model improvement

## Deployment Notes

### Streamlit Cloud Requirements
- `requirements.txt` in project root
- `app.py` as main application file
- Python 3.8+ runtime
- Automatic dependency installation

### Expected Resource Usage
- Memory: ~500MB (model) + ~100MB (runtime) = 600MB total
- CPU: 1-2 seconds per inference on typical text
- Storage: ~1.5GB (model cache)

### Environment Variables (None Required)
- No API keys needed
- No configuration secrets
- Fully self-contained application

## References
- Streamlit Documentation: https://docs.streamlit.io
- Hugging Face Transformers: https://huggingface.co/docs/transformers
- Model Card: https://huggingface.co/Hello-SimpleAI/chatgpt-detector-roberta
