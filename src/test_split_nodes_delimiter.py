import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This **is** a text node", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This ", TextType.PLAIN),
                TextNode("is", TextType.BOLD),
                TextNode(" a text node", TextType.PLAIN)
            ]
        )

    def test_2(self):
        node = TextNode("This **is** a **text** node", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This ", TextType.PLAIN),
                TextNode("is", TextType.BOLD),
                TextNode(" a ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" node", TextType.PLAIN)
            ]
        )

    def test_3(self):
        node = TextNode("This _is a_ text _node_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This ", TextType.PLAIN),
                TextNode("is a", TextType.ITALIC),
                TextNode(" text ", TextType.PLAIN),
                TextNode("node", TextType.ITALIC)
            ]
        )

    def test_4(self):
        node = TextNode("`This` is a text `node`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", TextType.CODE),
                TextNode(" is a text ", TextType.PLAIN),
                TextNode("node", TextType.CODE)
            ]
        )

    def test_5(self):
        node = TextNode("_italic_**bold**`code`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("italic", TextType.ITALIC),
                TextNode("bold", TextType.BOLD),
                TextNode("code", TextType.CODE)
            ]
        )

    def test_6(self):
        node = TextNode("_italic_ and **bold**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD)
            ]
        )

if __name__ == "__main__":
    unittest.main()
