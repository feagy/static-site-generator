from enum import Enum
import re
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode
from split_nodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

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

def markdown_to_html_node(markdown: str) -> HTMLNode:
    md_blocks = markdown_to_blocks(markdown)
    children = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block = " ".join(block.split("\n"))
                html_node = ParentNode(tag = "p", children = text_to_children(block))
                children.append(html_node)
            case BlockType.HEADING:
                split_block = block.split(" ", 1)
                html_node = ParentNode(tag = f"h{len(split_block[0])}", children = text_to_children(split_block[-1]))
                children.append(html_node)
            case BlockType.CODE:
                text_node = TextNode(text = block.strip("`").lstrip(), text_type = TextType.CODE)
                html_node = ParentNode(tag = "pre", children = [text_node_to_html_node(text_node)])
                children.append(html_node)
            case BlockType.QUOTE:
                lines = block.split("\n")
                lines = [line.lstrip(">").strip() for line in lines]
                block = " ".join(lines)
                html_node = ParentNode(tag = "blockquote", children = text_to_children(block))
                children.append(html_node)
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                lines = [line.lstrip("-").strip() for line in lines]
                html_node = ParentNode(tag = "ul", children = [])
                for line in lines:
                    html_node.children.append(ParentNode(tag = "li", children = text_to_children(line)))
                children.append(html_node)
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                lines = [line.split(".", 1)[-1].strip() for line in lines]
                html_node = ParentNode(tag = "ol", children = [])
                for line in lines:
                    html_node.children.append(ParentNode(tag = "li", children = text_to_children(line)))
                children.append(html_node)
    
    return ParentNode(tag = "div", children = children)

def text_to_children(text) -> list[HTMLNode]:
    child_textnodes = text_to_textnodes(text)  
    return [text_node_to_html_node(child_textnode) for child_textnode in child_textnodes]  


























    
