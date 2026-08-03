

class HTMLNode():
    def __init__(self, tag: str|None = None, value: str|None = None, children: list["HTMLNode"]|None = None, props: dict[str, str]|None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> None:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        return " ".join([f"{k}=\"{v}\"" for k, v in self.props.items()])

    
