class Tag:
    # Mapping of Python attribute names to HTML attribute names
    RESERVED_ATTRS = {
        'cls': 'class',
        'class_': 'class',
        'fr': 'for',
        'for_': 'for',
        'async_': 'async'
    }

    def __init__(self, name, *children, **attrs):
        self.name = name
        self.children = children
        self.attrs = self._process_attrs(attrs)

    def _process_attrs(self, attrs):
        """Process attributes, handling special cases and conversions."""
        processed = {}
        
        for key, value in attrs.items():
            # Handle reserved words
            if key in self.RESERVED_ATTRS:
                key = self.RESERVED_ATTRS[key]
            
            # Convert underscores to hyphens
            key = key.replace('_', '-')
            
            # Handle boolean attributes
            if isinstance(value, bool):
                if value:
                    processed[key] = None
                continue
            
            processed[key] = value
            
        return processed
    
    def add(self, *children):
        """
        Add children, also of class Tag,to the tag.
        """
        self.children.extend(children)

    def render(self):
        """Render the tag and its children as HTML."""
        # Build attributes string
        attrs_str = []
        for key, value in self.attrs.items():
            if value is None:
                attrs_str.append(key)
            else:
                attrs_str.append(f'{key}="{value}"')
        
        attrs_html = " ".join(attrs_str)
        if attrs_html:
            attrs_html = " " + attrs_html

        # Process children
        inner_html = "".join(
            c.render() if isinstance(c, Tag) else str(c) 
            for c in self.children
        )

        return f"<{self.name}{attrs_html}>{inner_html}</{self.name}>"