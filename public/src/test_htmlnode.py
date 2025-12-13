import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
   def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 
   def test_leaf_to_html_b(self):
        node = LeafNode("b", "bold")
        self.assertEqual(node.to_html(), "<b>bold</b>")
   def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", "https:link24234")
        self.assertEqual(node.to_html(), '<a href="https:link24234">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    # def test_to_html_without_children(self):
    #     parent_node = ParentNode("div", None)
    #     with self.assertRaises(ValueError("missing children"):
                # parent_node.to_html()
    def test_to_html_multiple_children(self):
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode("p", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual( parent_node.to_html(), "<div><b>child1</b><p>child2</p></div>")

