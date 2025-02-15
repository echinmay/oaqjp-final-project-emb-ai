import pytest
import os
import sys

# Ensure 'final_project' is in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EmotionDetection import emotion_detector

# Test cases with expected dominant emotions
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

@pytest.mark.parametrize("text, expected_emotion", test_cases)
def test_emotion_detection(text, expected_emotion):
    """
    Test the emotion_detector function for expected dominant emotions.
    """
    result = emotion_detector(text)
    
    # Ensure the response is a dictionary with a 'dominant_emotion' key
    assert isinstance(result, dict)
    assert "dominant_emotion" in result
    
    # Check if the detected emotion matches the expected emotion
    assert result["dominant_emotion"] == expected_emotion, f"Failed for input: {text}"