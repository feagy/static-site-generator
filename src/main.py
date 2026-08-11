from textnode import TextNode, TextType
from htmlnode import HTMLNode
from file_functions import copy_file_contents, clean_file
from markdown_functions import generate_pages_recursive
import sys


def main():
    try:
        basepath = sys.argv[0] if sys.argv[0] else "/"
        clean_file("public") 
        copy_file_contents("static", "docs")
        
        generate_pages_recursive("content", "template.html", "docs", basepath)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
