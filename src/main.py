from textnode import TextNode, TextType
from htmlnode import HTMLNode
from file_functions import copy_file_contents, clean_file
from markdown_functions import generate_pages_recursive

def main():
    try:
        print("started main")
        clean_file("public") 
        copy_file_contents("static", "public")
        
        generate_pages_recursive("content", "template.html", "public")
        print("finished main")
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
