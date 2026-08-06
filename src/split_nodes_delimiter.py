from textnode import TextNode, TextType

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
            
