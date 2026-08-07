from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_texts = node.text.split(delimiter)
        if len(split_texts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        split_nodes = []
        is_delimited = False
        for text in split_texts:
            if text == "":
                is_delimited = not is_delimited
                continue
            if is_delimited:
                split_nodes.append(TextNode(text, text_type))
                is_delimited = not is_delimited
            else:
                split_nodes.append(TextNode(text, TextType.PLAIN))
                is_delimited = not is_delimited

        new_nodes.extend(split_nodes)

    return new_nodes
            

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text = node.text
        anchor_url_pairs = extract_markdown_images(text)
        if not anchor_url_pairs:
            new_nodes.append(node)
            continue
        split_nodes = [] 
        for anchor, url in anchor_url_pairs:
            substr = f"![{anchor}]({url})"
            split_text = text.split(substr, 1)
            if split_text[0]:
                split_nodes.append(TextNode(split_text[0], TextType.PLAIN))
            split_nodes.append(TextNode(anchor, TextType.IMAGE, url))
            text = split_text[-1]
        if text:
            split_nodes.append(TextNode(text, TextType.PLAIN))
        new_nodes.extend(split_nodes)
    return new_nodes
    


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text = node.text
        anchor_url_pairs = extract_markdown_links(text)
        if not anchor_url_pairs:
            new_nodes.append(node)
            continue
        split_nodes = [] 
        for anchor, url in anchor_url_pairs:
            substr = f"[{anchor}]({url})"
            split_text = text.split(substr, 1)
            if split_text[0]:
                split_nodes.append(TextNode(split_text[0], TextType.PLAIN))
            split_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = split_text[-1]
        if text:
            split_nodes.append(TextNode(text, TextType.PLAIN))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    text_nodes = split_nodes_delimiter([TextNode(text, TextType.PLAIN)], "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_image(text_nodes)

    return text_nodes

            
