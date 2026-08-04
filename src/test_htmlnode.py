import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def _value_test(self, tag: str|None = None, value: str|None = None, children: list["HTMLNode"]|None = None, props: dict[str, str]|None = None):
        node = HTMLNode(tag = tag, value = value, children = children, props = props)
        text = f"HTMLNode({tag}, {value}, {children}, {props})"
        self.assertEqual(str(node), text)

    def test_value_1(self):
        self._value_test()

    def test_value_2(self):
        self._value_test(tag = "a")

    def test_value_3(self):
        self._value_test(value = "this is a htmlnode")

    def test_value_4(self):
        self._value_test(children = [HTMLNode(), HTMLNode(tag = "h1")])

    def test_value_5(self):
        self._value_test(props = {"href": "https://www.google.com", "target": "_blank",})

    def test_value_6(self):
        self._value_test(
            tag = "a",
            value = "this is a htmlnode",
            children = [HTMLNode(), HTMLNode(tag = "h1")],
            props = {"href": "https://www.google.com", "target": "_blank",}
        )

    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()
