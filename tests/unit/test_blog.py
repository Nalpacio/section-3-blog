from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Title', 'Author')

        self.assertEqual(blog.title, 'Title')
        self.assertEqual(blog.author, 'Author')
        self.assertListEqual(blog.posts, [])
        self.assertEqual(len(blog.posts), 0)

    def test_repr(self):
        blog = Blog('Title', 'Author')
        self.assertEqual(blog.__repr__(), 'Title by Author, 0 posts currently')

        blog.posts.append('Post_one')
        self.assertEqual(blog.__repr__(), 'Title by Author, 1 post currently')

        blog.posts.append('Post_two')
        self.assertEqual(blog.__repr__(), 'Title by Author, 2 posts currently')
