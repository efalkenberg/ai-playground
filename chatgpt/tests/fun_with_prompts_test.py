import unittest
import 

class TestFunWithPrompts(unittest.TestCase):
    HACKERNEWS_HTML_FILE = "hackernews_html_test.txt"
    def test_result(self):
        hackernews_html = open(HACKERNEWS_HTML_FILE, 'r').read()
        result = prompt_translate_hackernews(hackernews_html)

        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()