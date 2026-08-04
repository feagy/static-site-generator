import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("What is this", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("This is a text node", TextType.CODE, "url.com")
        node2 = TextNode("This is a text node", TextType.CODE, "url.com")
        self.assertEqual(node, node2)

    def test_eq_5(self):
        node = TextNode("This is a text node", TextType.BOLD, "url1.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url2.com")
        self.assertNotEqual(node, node2)

    def test_to_html_1(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_to_html_2(self):
        node = TextNode("This is a text node", TextType.LINK, "url.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props_to_html(), " href=\"url.com\"")

    def test_to_html_3(self):
        node = TextNode("This is a text node", TextType.IMAGE, "url.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), " src=\"url.com\" alt=\"This is a text node\"")

    


if __name__ == "__main__":
    unittest.main()
