from textnode import TextNode, TextType
from htmlnode import HTMLNode
from file_functions import copy_file_contents, clean_file

def main():
    try:
        clean_file("public") 
        copy_file_contents("static", "public")
    except Exception as e:
        return f'Error: {e}'


if __name__ == "__main__":
    main()
