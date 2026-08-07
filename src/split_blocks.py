from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    not_empty = []
    for block in blocks:
        if block:
            not_empty.append(block.strip())
    return not_empty

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines if line.strip()):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    current_number = 1
    for line in lines:
        if not line.strip():
            continue
        match = re.match(r"^(\d+)\.\s", line)
        if match and int(match.group(1)) == current_number:
            current_number += 1
            pass
        else:
            is_ordered = False
            break

    if is_ordered and any(line.strip() for line in lines):
        if re.match(r"^\d+\.\s", lines[0]):
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
    
