"""
Unit tests for the Emotion Detection application.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Test cases for the emotion_detector function.
    """

    def test_emotion_joy(self):
        """
        Test that the dominant emotion for a joy statement is 'joy'.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        """
        Test that the dominant emotion for an anger statement is 'anger'.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        """
        Test that the dominant emotion for a disgust statement is 'disgust'.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_sadness(self):
        """
        Test that the dominant emotion for a sadness statement is 'sadness'.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        """
        Test that the dominant emotion for a fear statement is 'fear'.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
