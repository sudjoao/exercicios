from lark import Lark, InlineTransformer, Token

grammar = Lark(
r"""
    ?start: expr 
    
    ?expr : expr "+" term -> add
        | term
        
    ?term : term "*" atom -> mul
        | atom
        
    ?atom : NUMBER -> number
        | "(" expr ")"
        
    NUMBER : /\d+/
    
    %ignore /\s+/
    %ignore /\#.*/
"""
)

class Transformer(InlineTransformer):
    def add(self, arg1, arg2):
        return ["+", arg1, arg2]

    def mul(self, arg1, arg2):
        return ["*", arg1, arg2]
    
    def number(self, token):
        try:
            return float(token)            
        except:
            return int(token)


def ast(x):
    transformer = Transformer()
    return transformer.transform(grammar.parse(x))

assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]