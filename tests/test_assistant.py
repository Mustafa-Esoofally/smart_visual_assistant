import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add parent directory to path to import SmartVisualAssistant
sys.path.append(str(Path(__file__).parent.parent))
from smart_visual_assistant import SmartVisualAssistant

def print_section(title: str, content: str):
    """Print a section with a title and content."""
    print(f"\n{'='*20} {title} {'='*20}")
    print(content)
    print('='*50)

def test_image_analysis():
    """Test basic image analysis functionality."""
    try:
        # Load environment variables
        load_dotenv()
        
        # Initialize the assistant
        assistant = SmartVisualAssistant()
        
        # Test image path
        image_path = str(Path(__file__).parent / "images" / "test_image.jpg")
        
        if not os.path.exists(image_path):
            print(f"Please add a test image at: {image_path}")
            return
        
        # Test basic image analysis
        print_section("Basic Image Analysis", 
            assistant.analyze_image(image_path, "What can you tell me about this image?"))
        
        # Test quiz generation
        quiz_result = assistant.generate_quiz(image_path, difficulty="easy")
        print_section("Quiz Generation", quiz_result["quiz_content"])
        
        # Test diagram explanation
        explanation_result = assistant.explain_diagram(image_path)
        print_section("Diagram Explanation", explanation_result["explanation"])
        
        # Test concept identification
        concepts_result = assistant.identify_key_concepts(image_path)
        print_section("Concept Identification", concepts_result["concepts"])
        
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        raise e

if __name__ == "__main__":
    test_image_analysis() 