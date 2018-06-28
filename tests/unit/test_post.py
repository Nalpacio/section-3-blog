from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        post = Post('Title', 'Content')

        self.assertEqual(post.title, 'Title')
        self.assertEqual(post.content, 'Content')

    def test_repr(self):
        post = Post('Title', 'Content')
        expected = 'Title'

        self.assertEqual(post.__repr__(), expected)

    def test_json(self):
        post = Post('Title', 'Content')
        expected = {'Title': 'Title',
                    'Content': 'Content',
                    }

        self.assertDictEqual(post.json(), expected)
