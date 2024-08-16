import time
import marko
from typing import TYPE_CHECKING, Any, Callable, TypeVar

import marko.inline

__all_blocks__ = (
    "Heading",
    "List",
    "Paragraph",
    "CodeBlock",
    "ThematicBreak",
    "BlankLine",

    "Document",
    "ListItem",
    "Quote",
    "FencedCode",
    "HTMLBlock",
    "LinkRefDef",
    "SetextHeading",
)

__all_inlines__ = (
    "Image",
    "Link",
    "RawText",

    "Emphasis",
    "StrongEmphasis",

    "LineBreak",
    "Literal",
    "InlineHTML",
    "CodeSpan",
    "AutoLink",
)


def render_content_from_markdown(element) -> Any:

    def render(element: marko.element.Element) -> Any:
        """Renders the given element to string.

        :param element: a element to be rendered.
        :returns: the output string or any values.
        """
        from marko.block import Document

        # Store the root node since it may be required by the render functions
        if not root_node:  # pragma: no cover
            if isinstance(element, Document):
                root_node = element
            else:
                # Make a dummy root node from it
                root_node = Document()
                root_node.children = [element]

        if hasattr(element, "get_type"):
            func_name = "render_" + element.get_type(snake_case=True)
            render_func = getattr( func_name, None)
            # if render_func is not None and (
            #     # getattr(render_func, "_force_delegate", False) or delegate   ### analisar melhor
            # ):
            #     return render_func(element)
        return render_children(element)

    def render_children(element: Any) -> Any:
        """
        Recursively renders child elements. Joins the rendered
        strings with no space in between.

        If newlines / spaces are needed between elements, add them
        in their respective templates, or override this function
        in the renderer subclass, so that whitespace won't seem to
        appear magically for anyone reading your program.

        :param element: a branch node who has children attribute.
        """
        rendered = [render(child) for child in element.children]  # type: ignore
        return "".join(rendered)
    
    render(element)

    def render_children(element: Any) -> Any:
        """
        Recursively renders child elements. Joins the rendered
        strings with no space in between.

        If newlines / spaces are needed between elements, add them
        in their respective templates, or override this function
        in the renderer subclass, so that whitespace won't seem to
        appear magically for anyone reading your program.

        :param element: a branch node who has children attribute.
        """
        rendered = [render(child) for child in element.children]  # type: ignore
        return "".join(rendered)
    
    render(element)



def parse_content_from_markdown(document,directory, file):
    with open(file, "r" , encoding="utf-8") as file:
        # user_message += file.read().replace("\n", "")
        content = file.read()
    d = marko.parse(content)
    # print(f'CONTEUDO: {d}')
    for line  in d.children:
        parse_block(line,document)

def parse_block(line,document):
        print(f'\nBLOCK {line}')
        time.sleep(2)
        if type(line) == marko.block.Heading:
            print('CABEÇALHO:')
            if hasattr(line, "children"):            
                for item in line.children:
                 if type(item) == marko.inline.RawText:
                    print(item.children)
                    # document.add_heading(f"{line}", level=0)
                    document.add_heading(item.children)
            # document.add_heading(f"{line}", level=0)
        elif type(line) == marko.block.BlankLine:
            print('BLANKLINE:')
            # document.add_paragraph(line)
            for item in line.children:
                print(f"ITEM:{item}")
                if type(item) == marko.inline.RawText:
                    print(item.__repr__)
                    document.add_paragraph(item.__repr__)
        elif type(line) == marko.block.Paragraph:
            print('PARAGRAPH:')
            for item in line.children:
                print(f"\nitem:{item}")
                # p1 = document.add_paragraph(item)
                parse_inline(item, document)
        elif type(line) == marko.block.ThematicBreak:
            print('ThematicBreak:')
            document.add_page_break()
        else:
            print('BLOCO NAO TRATADO:')
            # document.add_paragraph(line)
            # time.sleep(2)
        # time.sleep(1)

def parse_inline(block, document):
    print(f"BLOCK: type:{type(block)} block:{block}")
    if hasattr(block, "children"):
        # children = f" children={pformat(self.children)}"
        for item in block.children:
            parse_item(item,document)
        #     if type(item) == marko.inline.StrongEmphasis:
        #         for i in item.children:
        #             document.add_paragraph(i)
        #     else:
        #         print(item)
    else:
        print("BLOCK -> Sem children")
        parse_item(block,document)
    # time.sleep(1)

def parse_item(item,document):
        if type(item) == marko.inline.StrongEmphasis:
            document.add_paragraph()
        else:
            # print(f'NÃO TRATADO={item}')
            # document.add_paragraph()
            # time.sleep(10)
            pass