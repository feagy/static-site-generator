from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node_test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node_test)

if __name__ == "__main__":
    main()
