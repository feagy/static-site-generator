import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def _value_test(self, tag: str|None, value: str, props: str|None = None):
        node = LeafNode(tag = tag, value = value, props = props)
        text = f"LeafNode({tag}, {value}, {props})"
        self.assertEqual(str(node), text)

    def test_value_2(self):
        self._value_test(tag = "h", value = "this is a leafnode")

    def test_value_3(self):
        self._value_test(
            tag = "a",
            value = "this is a htmlnode",
            props = {"href": "https://www.google.com", "target": "_blank",}
        )

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_2(self):
        node = LeafNode(           
            tag = "a",
            value = "this is a leafnode",
            props = {"href": "https://www.google.com", "target": "_blank",})

        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">this is a leafnode</a>")

if __name__ == "__main__":
    unittest.main()
