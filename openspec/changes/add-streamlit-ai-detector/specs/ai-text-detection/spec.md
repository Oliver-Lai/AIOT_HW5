# Specification: AI Text Detection

## ADDED Requirements

### Requirement: Model Integration
The system SHALL integrate the "Hello-SimpleAI/chatgpt-detector-roberta" pre-trained model from Hugging Face for text classification.

#### Scenario: Model Loading
**Given** the application starts for the first time  
**When** the `load_model()` function is called  
**Then** the Hugging Face transformers pipeline is initialized  
**And** the model "Hello-SimpleAI/chatgpt-detector-roberta" is downloaded and loaded  
**And** the pipeline task type is set to "text-classification"  
**And** the model is configured to use CPU (device=-1)

#### Scenario: Model Cached Loading
**Given** the model has been loaded previously  
**When** the `load_model()` function is called again  
**Then** the cached model pipeline is returned  
**And** no network request is made to Hugging Face  
**And** loading completes in under 100ms

---

### Requirement: Text Classification
The system SHALL classify input text as AI-generated, Human-written, or Mixed based on model predictions.

#### Scenario: AI-Generated Text Detection
**Given** a user submits text that is AI-generated  
**When** the model analyzes the text  
**Then** the AI probability is greater than 70%  
**And** the classification result is "AI Generated"  
**And** the result is displayed with an error-style indicator (red)

#### Scenario: Human-Written Text Detection
**Given** a user submits text that is human-written  
**When** the model analyzes the text  
**Then** the Human probability is greater than 70%  
**And** the classification result is "Human Written"  
**And** the result is displayed with a success-style indicator (green)

#### Scenario: Mixed or Uncertain Detection
**Given** a user submits text with ambiguous authorship  
**When** the model analyzes the text  
**Then** neither AI nor Human probability exceeds 70%  
**And** the classification result is "Mixed/Uncertain"  
**And** the result is displayed with a warning-style indicator (yellow)

---

### Requirement: Probability Extraction
The system SHALL extract and normalize probability scores from the model's output.

#### Scenario: Extract Label Probabilities
**Given** the model returns prediction results  
**When** the results are processed  
**Then** the probability for the "ChatGPT" label is extracted  
**And** the probability for the "Human" label is extracted  
**And** both probabilities are normalized to percentages (0-100)  
**And** the percentages sum to approximately 100%

#### Scenario: Handle Missing Labels
**Given** the model output does not contain expected labels  
**When** the results are processed  
**Then** a default probability of 0.0 is assigned to missing labels  
**And** an error message is logged or displayed  
**And** the application does not crash

---

### Requirement: Analysis Function
The system SHALL provide a text analysis function that processes input and returns structured results.

#### Scenario: Successful Text Analysis
**Given** a valid text input is provided  
**When** the `analyze_text()` function is called  
**Then** the text is passed to the model pipeline  
**And** predictions are returned within 10 seconds  
**And** a structured dictionary is returned containing:
  - `ai_probability` (float, 0-100)
  - `human_probability` (float, 0-100)
  - `classification` (string: "AI Generated", "Human Written", or "Mixed/Uncertain")
  - `confidence_level` (string: "High", "Medium", or "Low")

#### Scenario: Short Text Analysis
**Given** a user submits text with fewer than 10 words  
**When** the analysis is performed  
**Then** the model processes the text  
**And** results are returned  
**And** a note about limited confidence for short text is displayed

#### Scenario: Long Text Analysis
**Given** a user submits text with more than 1000 words  
**When** the analysis is performed  
**Then** the model processes the text  
**And** analysis may take up to 10 seconds  
**And** a loading indicator is shown throughout processing

---

### Requirement: Confidence Level Determination
The system SHALL determine and display a confidence level based on the probability spread.

#### Scenario: High Confidence Classification
**Given** the analysis completes  
**When** the highest probability exceeds 85%  
**Then** the confidence level is set to "High"  
**And** this is displayed to the user

#### Scenario: Medium Confidence Classification
**Given** the analysis completes  
**When** the highest probability is between 70% and 85%  
**Then** the confidence level is set to "Medium"  
**And** this is displayed to the user

#### Scenario: Low Confidence Classification
**Given** the analysis completes  
**When** the highest probability is below 70%  
**Then** the confidence level is set to "Low"  
**And** this is displayed to the user  
**And** a message suggests the result may be uncertain

---

### Requirement: Model Performance
The system SHALL ensure the model performs efficiently within acceptable time and resource constraints.

#### Scenario: Inference Time
**Given** a typical text input (100-1000 words)  
**When** the analysis is performed  
**Then** the model inference completes in under 5 seconds on average  
**And** the first inference may take up to 10 seconds due to initialization

#### Scenario: Memory Usage
**Given** the model is loaded in memory  
**When** multiple inferences are performed  
**Then** memory usage remains stable  
**And** no memory leaks occur  
**And** the model footprint does not exceed 600MB

---

### Requirement: Model Output Interpretation
The system SHALL correctly interpret the model's output format and handle edge cases.

#### Scenario: Standard Model Output
**Given** the model returns a list of label-score pairs  
**When** the output is processed  
**Then** each label is correctly identified  
**And** each score is correctly extracted  
**And** scores are converted to probabilities correctly

#### Scenario: Single Label Output
**Given** the model returns only one label with high confidence  
**When** the output is processed  
**Then** the primary label's probability is used  
**And** the complementary probability is calculated (100 - primary)  
**And** results are displayed accurately

#### Scenario: Unexpected Output Format
**Given** the model returns an unexpected output format  
**When** the output is processed  
**Then** a graceful fallback is triggered  
**And** raw probabilities are displayed if possible  
**And** an error message explains the issue to the user
