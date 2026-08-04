from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str|None, children: list["HTMLNode"], props: str|None = None) -> None:
        super().__init__(tag = tag, children = children, props = props)

    def __repr__(self) -> None:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self) -> str:
        if not self.tag:
            return ValueError("All parent nodes must have a tag")

        if not self.children:
            return ValueError("All parent nodes must have children")   
        
        return f"<{self.tag}{self.props_to_html()}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"
