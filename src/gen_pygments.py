from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name



def generate_pygments(code_text,directory,img_id):
    print('function generate_pygments...')
    # Specify the lexer and formatter
    lexer = PythonLexer()
    formatter = HtmlFormatter(style='monokai', full=True)

    # Generate the HTML output
    html_output = highlight(code_text, lexer, formatter)
    html_file = f'{directory}\\output\\output_{img_id}.html'

    # Save the HTML output to a file
    with open(html_file, 'w') as f:
        f.write(html_output)

    # The HTML output is now saved in 'output.html'
    print(f"HTML output generated and saved to '{html_file}'")

    code_lines = code_text.splitlines()
    max = 0
    for c in code_lines:
        if int(c.count('')) > max:
            max = int(c.count(''))

    lines=len(code_lines)
    print(f"{max},{lines}")
    return max, lines, html_file


if __name__ == "__main__":

    code = """from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
    from pygments.styles import get_style_by_name

          kubectl --kubeconfig=/home/azureuser/.kube/config apply -f $(Build.SourcesDirectory)/k8s/deploy_temp.yaml    
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
    (max,lines) = generate_pygments(code)
    gen_code_image(max,lines)