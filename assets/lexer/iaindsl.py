from pygments.lexer import RegexLexer
from pygments.token import *

class IainLexer(RegexLexer):
    name = 'Iain'
    aliases = ['iain']
    filenames = ['*.iain']
    
    tokens = {
        'root': [
                 (r' .*\n', Text),
                 (r'personal', Keyword),
                 (r'bio', Keyword),
                 (r'prefix', Keyword),
                 (r'name', Keyword),
                 (r':', Operator),
                 (r'{', Operator),
                 (r'}', Operator),
                 ('"', String, 'string'),
                 (r'.*\n', Text),
                 ],
                 'string': [
                            ('[^"]+', String),
                            ('"', String, '#pop'),
                            ]
}
