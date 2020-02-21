from .elem import Elem, Text


class Html(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='html', attr=attr, content=content)


class Head(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='head', attr=attr, content=content)


class Body(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='body', attr=attr, content=content)


class Title(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='title', attr=attr, content=content)


class Meta(Elem):

    def __init__(self, attr={}):
        Elem.__init__(self, tag='meta', attr=attr, tag_type='simple')


class Img(Elem):

    def __init__(self, attr={}):
        Elem.__init__(self, tag='img', attr=attr, tag_type='simple')


class Table(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='table', attr=attr, content=content)


class Th(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='th', attr=attr, content=content)


class Tr(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='tr', attr=attr, content=content)


class Td(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='td', attr=attr, content=content)


class Ul(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='ul', attr=attr, content=content)


class Ol(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='ol', attr=attr, content=content)


class Li(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='li', attr=attr, content=content)


class H1(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='h1', attr=attr, content=content)


class H2(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='h2', attr=attr, content=content)


class P(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='p', attr=attr, content=content)


class Div(Elem):
    pass


class Span(Elem):

    def __init__(self, attr={}, content=None):
        Elem.__init__(self, tag='span', attr=attr, content=content)


class Hr(Elem):

    def __init__(self, attr={}):
        Elem.__init__(self, tag='hr', attr=attr, tag_type='simple')


class Br(Elem):

    def __init__(self, attr={}):
        Elem.__init__(self, tag='br', attr=attr, tag_type='simple')


def test_text():
    # Table, tr, td
    assert str(Html(content=[Head(), Body(content=[
        Table(content=(Tr(content=[Td(), Td()])))
    ])])) == '<html>\n' \
             '  <head></head>\n' \
             '  <body>\n' \
             '    <table>\n' \
             '      <tr>\n' \
             '        <td></td>\n' \
             '        <td></td>\n' \
             '      </tr>\n' \
             '    </table>\n' \
             '  </body>\n' \
             '</html>'
    # Span, br, p
    assert str(Html(content=[Head(), Body(content=[
        Div(content=[Span(), Br(), P()])
    ])])) == '<html>\n' \
             '  <head></head>\n' \
             '  <body>\n' \
             '    <div>\n' \
             '      <span></span>\n' \
             '      <br/ >\n' \
             '      <p></p>\n' \
             '    </div>\n' \
             '  </body>\n' \
             '</html>'
    # Meta, ul, li
    assert str(Html(content=[Head(content=[Meta(), Title()]),
                             Body(content=[
                                 Ul(content=[Li(), Li(), Li()])
                             ])]
                    )) == '<html>\n' \
                          '  <head>\n' \
                          '    <meta/ >\n' \
                          '    <title></title>\n' \
                          '  </head>\n' \
                          '  <body>\n' \
                          '    <ul>\n' \
                          '      <li></li>\n' \
                          '      <li></li>\n' \
                          '      <li></li>\n' \
                          '    </ul>\n' \
                          '  </body>\n' \
                          '</html>'
    print('Text behaviour : OK.')


if __name__ == '__main__':
    print("First example:\n", Html(content=[Head(), Body()]))
    print("\nSecond example:\n", Html(content=[
        Head(content=
             Title(content=Text("Hello ground!"))),
        Body(content=[
            H1(content=Text("Oh no, not again!")),
            Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"})
            ])
    ]))
    print("\nTests:")
    test_text()
