# Smart Visual Learning Assistant

A powerful tool that leverages Google's Gemini Pro Vision model to create interactive learning experiences from visual content.

## Features

- **Image Analysis**: Analyze any image with custom prompts
- **Diagram Explanation**: Get detailed explanations of diagrams and charts
- **Interactive Quizzes**: Generate quizzes based on image content
- **Concept Identification**: Extract and explain key educational concepts from images

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your Google Cloud API key:
```bash
export GOOGLE_API_KEY='your-api-key'
```

## Usage Example

```python
from smart_visual_assistant import SmartVisualAssistant

# Initialize the assistant
assistant = SmartVisualAssistant()

# Analyze an image
result = assistant.analyze_image("path/to/image.jpg", "What can you tell me about this image?")
print(result)

# Generate a quiz
quiz = assistant.generate_quiz("path/to/image.jpg", difficulty="medium")
print(quiz["quiz_content"])

# Explain a diagram
explanation = assistant.explain_diagram("path/to/diagram.jpg")
print(explanation["explanation"])

# Identify key concepts
concepts = assistant.identify_key_concepts("path/to/educational_image.jpg")
print(concepts["concepts"])
```

## Requirements

- Python 3.7+
- Google Cloud API key
- Required packages (see requirements.txt)

## Note

Make sure to replace "your-project-id" in the code with your actual Google Cloud project ID.

## License

MIT License 