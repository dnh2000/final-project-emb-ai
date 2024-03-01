import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test1 = emotion_detector('I am overjoyed. ')
        self.assertEqual(test1['dominant_emotion'], 'joy')
        test2 = emotion_detector('I am very angry about this.')
        self.assertEqual(test2['dominant_emotion'], 'anger')
        test3 = emotion_detector('Broccoli disgusts me.')
        self.assertEqual(test3['dominant_emotion'], 'disgust')
        test4 = emotion_detector('Sad movies make me cry.')
        self.assertEqual(test4['dominant_emotion'], 'sadness')
        test5 = emotion_detector('Spiders really scare me.')
        self.assertEqual(test5['dominant_emotion'], 'fear')

unittest.main()