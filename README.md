# PyTag

A minimal Python library for programmatic HTML generation. PyTag uses very simple, Pythonic syntax and pairs well with server-driven web architectures (FastAPI, HTMX).

## Features

- Simple API mirroring the HTML: `Div(...)`, `Button(...)`, etc.
- For example, `Div("Hello, world", cls = "blog-post").render()` results in `'<div class="blog-post">Hello, world</div>'`
- Automatic conversion of underscores to hyphens in attribute names (e.g., `hx_get` → `hx-get`)
- Special handling of reserved words (e.g., `cls` → `class`, `fr` → `for`)
- Lightweight, no dependencies
- Unlicense

## Installation

Pip and conda coming soon; for now clone the repo and add `pytag` (the outer directory) to your `PYTHONPATH`.

## Quick Start

```python
from pytag.tags import Div, Button, Span

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

## Why PyTag?
PyTag is for users who prefer to generate HTML directly in Python rather than with JavaScript or HTML templating libraries.

It complements HTMX nicely and was built for that purpose.

It is similar to the `Dominate` package, but with slightly nicer syntax (capitalized tag classes,
automatic conversion of underscores to hyphens).

The FastHTML library was another major inspiration. In fact, the syntax is stolen from FastHTML. This library, however,
provides just the HTML generation without wrapping server functionality.

## License

This project is licensed under the Unlicense - see the [UNLICENSE](UNLICENSE) file for details. 