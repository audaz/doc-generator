from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

# Text to be highlighted
# code = 'print("Hello World")'
code = """from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

# Text to be highlighted
code = 'print("Hello World")'

# Specify the lexer and formatter
lexer = PythonLexer()
formatter = HtmlFormatter(style='monokai', full=True)

# Generate the HTML output
html_output = highlight(code, lexer, formatter)

# Save the HTML output to a file
with open('output.html', 'w') as f:
    f.write(html_output)

# The HTML output is now saved in 'output.html'
print("HTML output generated and saved to 'output.html'")
"""

# Specify the lexer and formatter
lexer = PythonLexer()
formatter = HtmlFormatter(style='monokai', full=True)

# Generate the HTML output
html_output = highlight(code, lexer, formatter)

# Save the HTML output to a file
with open('output.html', 'w') as f:
    f.write(html_output)

# The HTML output is now saved in 'output.html'
print("HTML output generated and saved to 'output.html'")
