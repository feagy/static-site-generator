import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def _value_test(self, tag: str|None, children: list["HTMLNode"], props: str|None = None):
        node = ParentNode(tag = tag, children = children, props = props)
        text = f"ParentNode({tag}, {children}, {props})"
        self.assertEqual(str(node), text)

    def test_value_1(self):
        child_node = LeafNode("span", "child")
        self._value_test(tag = "div", children = [child_node])

    def test_value_2(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        self._value_test(tag = "div", children = [child_node])

    def test_parent_to_html(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_2(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
