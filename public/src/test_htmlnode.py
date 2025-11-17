import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode("p", "hehe", ["p", "a"], {"target": "_blank"})
        node.props_to_html()
    def test_none(self):
        node = HTMLNode()
        node.props_to_html()
    def test_multiprops(self):
        node = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        node.props_to_html()
