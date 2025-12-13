from textnode import TextNode, TextType
from regexsearch import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        if n.text.count(delimiter) % 2 != 0:
            raise Exception("invalid Mardown syntax")
        splits = n.text.split(delimiter)
        for s in splits:
            if s != "":
                new_nodes.append(s)
        for t in range(0, len(new_nodes), 2 ): 
            new_nodes[t] = TextNode(new_nodes[t], TextType.TEXT)
        for s in range(1, len(new_nodes), 2):
            new_nodes[s] = TextNode(new_nodes[s], text_type)
    return new_nodes

def split_img_helper(text: str, new_nodes: list):
    markdowns = extract_markdown_images(text)
    print(markdowns)
    if markdowns == []:
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
        return
    sections = text.split(f"![{markdowns[0][0]}]({markdowns[0][1]})", 1)
    new_nodes.append(TextNode(sections[0], TextType.TEXT))
    new_nodes.append(TextNode(markdowns[0][0], TextType.IMAGE, markdowns[0][1]))
    split_img_helper(sections[1], new_nodes)
        

def split_link_helper(text: str, new_nodes: list):
    markdowns = extract_markdown_links(text)
    if markdowns == []:
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
        return
    else:
        sections = text.split(f"[{markdowns[0][0]}]({markdowns[0][1]})", 1)
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(markdowns[0][0], TextType.LINK, markdowns[0][1]))
        split_link_helper(sections[1], new_nodes)


def split_nodes_image(old_nodes):
    final = []
    for n in old_nodes:
        if extract_markdown_images(n.text) == []:
            if n.text == "":
                continue
            else:
                final.append(n)
                continue
        split_img_helper(n.text, final)
    return final


def split_nodes_link(old_nodes):
    final = []
    for n in old_nodes:
        if extract_markdown_links(n.text) == []:
            if n.text == "":
                continue
            else:
                final.append(n)
                continue
        split_link_helper(n.text, final)
    return final








        

    
