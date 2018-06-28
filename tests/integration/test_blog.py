from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post(self):
        blog = Blog('Title', 'Author')
        blog.create_post('PostTitle', 'PostContent')
        expected = [{'Title': 'PostTitle',
                     'Content': 'PostContent',
                     }]

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'PostTitle')
        self.assertEqual(blog.posts[0].content, 'PostContent')

    def test_json(self):
        blog = Blog('Title', 'Author')
        blog.create_post('PostTitle', 'PostContent')
        expected = {
            'title': 'Title',
            'author': 'Author',
            'posts': [{'Title': 'PostTitle',
                       'Content': 'PostContent',
                       },
                      ]
        }

        self.assertEqual(blog.json(), expected)
