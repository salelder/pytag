# Project Kickoff: PyTag

## Objective
Create a minimal Python library called **PyTag** for programmatic HTML generation. 
It should prioritize clean, Pythonic syntax and work seamlessly with server-driven web architectures (FastAPI, HTMX).

---

##  Target Features
- Simple, readable API: `Div(...)`, `Button(...)`, or `tags.Div(...)`.
- Automatic conversion of underscores to hyphens in attribute names (e.g., `hx_get` → `hx-get`).
- Special handling of reserved words (e.g., `cls` → `class`, `fr` → `for`).
- Output can be either a structured object or the corresponding HTML string `.render()`.
- Lightweight, no dependencies.
- Unlicense.

---

##  Attribute Name Conventions

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

Example:
```python
html = Button(
    "Submit",
    cls="btn-primary",  # becomes class="btn-primary"
    disabled=True,      # becomes disabled
    data_user_id=123,   # becomes data-user-id="123"
    aria_label="Submit form"  # becomes aria-label="Submit form"
).render()
```

---

##  API Example

```python
from pytag.tags import Div, Button

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

---

##  Implementation Notes

### Core Tag Class

```python
class Tag:
    def __init__(self, name, *children, **attrs):
        self.name = name
        self.children = children
        self.attrs = {k.replace('_', '-'): v for k, v in attrs.items()}

    def render(self):
        attrs = " ".join(f'{k}="{v}"' for k, v in self.attrs.items())
        inner_html = "".join(c.render() if isinstance(c, Tag) else str(c) for c in self.children)
        return f"<{self.name} {attrs}>{inner_html}</{self.name}>"
```

### Tag Factories

```python
def Div(*children, **attrs): return Tag("div", *children, **attrs)
def Button(*children, **attrs): return Tag("button", *children, **attrs)
def Span(*children, **attrs): return Tag("span", *children, **attrs)
```

### Tags Namespace

```python
class TagsFactory:
    def __getattr__(self, tag_name):
        return lambda *children, **attrs: Tag(tag_name.lower(), *children, **attrs)

Tags = TagsFactory()
```

---

##  Package Structure

```
pytag/
├── __init__.py
└── core.py
setup.py
LICENSE (MIT)
README.md
```

---

##  License
Unlicense. Include it explicitly in `UNLICENSE` and `setup.py`.

---

##  Next Steps
1. Implement the core functionality in `core.py`.
2. Add `setup.py` and publish to PyPI under the `pytag` name.
3. Include examples and quick-start in `README.md`.
4. (Optional) Add a `tests/` directory with a few basic tests.
