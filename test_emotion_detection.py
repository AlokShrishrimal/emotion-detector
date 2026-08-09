import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am feeling very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_anger(self):
        result = emotion_detector("I am really angry")
        self.assertEqual(result["dominant_emotion"], "anger")

if __name__ == "__main__":
    unittest.main()
