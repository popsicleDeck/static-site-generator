class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        if self.props == None:
            return ""
        final = ""
        for k in self.props:
            final += f' {k}="{self.props[k]}"'
    def __repr__(self):
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return str(value)
        if self.tag == "a":
            return f'<a href="{self.props}">{self.value}</a>'
        else: 
            return f'<{self.tag}>{self.value}</{self.tag}>'
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None ):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        if self.children == None: 
            raise ValueError("missing children")
        node = ""
        for c in self.children: 
            node += c.to_html()
        return f"<{self.tag}>{node}</{self.tag}>"





