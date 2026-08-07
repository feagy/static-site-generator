import unittest
from split_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestSplitBlock(unittest.TestCase):
        def test_markdown_to_blocks_1(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_2(self):
            md = """
This is **bolded** paragraph







This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line







- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_block_type_1(self):
            block = "### Heading 3"
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.HEADING)

        def test_block_type_2(self):
            block = """> This is a single line quote.
> And this is the second line of the same quote block."""
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.QUOTE)

        def test_block_type_3(self):
            block = """- Apple
- Banana
- Orange"""
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.UNORDERED_LIST)

        def test_block_type_4(self):
            block = """1. First ordered item
2. Second ordered item
3. Third ordered item"""
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.ORDERED_LIST)

        def test_block_type_5(self):
            block = "This is a standard paragraph block containing some regular text. It does not match any special markdown block types."
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.PARAGRAPH)

        def test_block_type_6(self):
            block = """```
python print("hello")
```"""
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.CODE)
if __name__ == "__main__":
    unittest.main()
