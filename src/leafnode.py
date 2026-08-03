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
    
        props_str = f" {self.props_to_html()}" if self.props and self.props_to_html() else ""        
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
