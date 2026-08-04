from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str|None, value: str, props: str|None = None) -> None:
        super().__init__(tag = tag, value = value, props = props)

    def __repr__(self) -> None:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        
        if not self.tag:
            return self.value
    
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
