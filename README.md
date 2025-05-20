# PyTag

A minimal Python library for programmatic HTML generation. PyTag prioritizes clean, Pythonic syntax and works seamlessly with server-driven web architectures (FastAPI, HTMX).

## Features

- Simple, readable API: `Div(...)`, `Button(...)`, or `tags.Div(...)`
- Automatic conversion of underscores to hyphens in attribute names (e.g., `hx_get` → `hx-get`)
- Special handling of reserved words (e.g., `cls` → `class`, `fr` → `for`)
- Lightweight, no dependencies
- Unlicense

## Installation

```bash
pip install pytag
```

## Quick Start

```python
from pytag import Div, Button, Span

# Create HTML elements
html = Div(
    Button("Click Me", hx_get="/api/data", hx_trigger="click", cls="btn"),
    Span("Status", id="status"),
    cls="container"
).render()

print(html)
# <div class="container">
#   <button hx-get="/api/data" hx-trigger="click" class="btn">Click Me</button>
#   <span id="status">Status</span>
# </div>
```

## Attribute Name Conventions

The library handles several special cases for attribute names:

1. Reserved Words:
   - `cls` or `class_` → `class` (since `class` is a Python keyword)
   - `fr` or `for_` → `for` (since `for` is a Python keyword)
   - `async_` → `async` (since `async` is a Python keyword)

2. Boolean Attributes:
   - `disabled=True` → `disabled`
   - `checked=True` → `checked`
   - `required=True` → `required`

3. Data Attributes:
   - `data_*` attributes are automatically converted (e.g., `data_user_id` → `data-user-id`)

4. ARIA Attributes:
   - `aria_*` attributes are automatically converted (e.g., `aria_label` → `aria-label`)

## Nonstandard Tag Creation

Although we have attempted to include all supported HTML tags, you may wish to define other, nonstandard tags.
You can create any tag using the `Tag` class:

```python
from pytag import Tag

# Create a nonstandard tag
bogus = Tag("bogus", "Hello, world!",
    cls="blog-post"
).render()

print(bogus)
# <bogus class="blog-post">Hello, world!</bogus>
```

## License

This project is licensed under the Unlicense - see the [UNLICENSE](UNLICENSE) file for details. 