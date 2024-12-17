import os
from typing import Optional, List, Dict, Any
from PIL import Image
import google.generativeai as genai
import numpy as np
import cv2
from dotenv import load_dotenv

class SmartVisualAssistant:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Smart Visual Learning Assistant.
        
        Args:
            api_key: Optional Google Cloud API key. If not provided, will look for GOOGLE_API_KEY env variable.
        """
        # Load environment variables
        load_dotenv()
        
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        
        if not self.api_key:
            raise ValueError("API key must be provided or set in GOOGLE_API_KEY environment variable")
            
        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        
        # Initialize the Gemini model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def analyze_image(self, image_path: str, prompt: str) -> str:
        """Analyze an image with a specific prompt.
        
        Args:
            image_path: Path to the image file
            prompt: Specific instruction or question about the image
            
        Returns:
            str: Generated response about the image
        """
        try:
            # Load and prepare the image
            image = Image.open(image_path)
            
            # Generate response
            response = self.model.generate_content(
                [prompt, image],
                generation_config={
                    "max_output_tokens": 1024,
                    "temperature": 0.4,
                }
            )
            
            # Get the response text
            if response.text:
                return response.text
            else:
                return "No response generated from the model."
            
        except Exception as e:
            raise Exception(f"Error analyzing image: {str(e)}")
            
    def explain_diagram(self, image_path: str) -> Dict[str, Any]:
        """Analyze and explain a diagram or chart.
        
        Args:
            image_path: Path to the diagram image
            
        Returns:
            Dict containing explanation and identified components
        """
        prompt = """Analyze this diagram and provide:
        1. A clear explanation of what it shows
        2. Key components and their relationships
        3. Any important patterns or insights
        Please structure the response clearly."""
        
        explanation = self.analyze_image(image_path, prompt)
        return {
            "explanation": explanation,
            "image_path": image_path
        }
    
    def generate_quiz(self, image_path: str, difficulty: str = "medium") -> Dict[str, Any]:
        """Generate an interactive quiz based on an image.
        
        Args:
            image_path: Path to the image
            difficulty: Difficulty level (easy, medium, hard)
            
        Returns:
            Dict containing quiz questions and answers
        """
        prompt = f"""Generate a {difficulty}-level quiz about this image with:
        1. 3 multiple choice questions
        2. The correct answer for each question
        3. A brief explanation for each answer
        Format as a structured response."""
        
        quiz_content = self.analyze_image(image_path, prompt)
        return {
            "quiz_content": quiz_content,
            "difficulty": difficulty,
            "image_path": image_path
        }
    
    def identify_key_concepts(self, image_path: str) -> List[Dict[str, str]]:
        """Identify and explain key concepts in an educational image.
        
        Args:
            image_path: Path to the image
            
        Returns:
            List of dictionaries containing concepts and explanations
        """
        prompt = """Identify the main educational concepts in this image.
        For each concept provide:
        1. The concept name
        2. A brief explanation
        3. How it relates to the overall topic"""
        
        concepts = self.analyze_image(image_path, prompt)
        return {
            "concepts": concepts,
            "image_path": image_path
        } 