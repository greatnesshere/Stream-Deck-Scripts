# helper script to visualize dictionary accesses
from sys import argv
import ast,json
def inspect(t,args:list):
    if t.__class__ is ast.Expression:
        return inspect(t.body,args)
    elif t.__class__ is ast.Subscript:
        assert t.slice.__class__ is ast.Constant
        # print("Slice",t.slice.value)
        args.append(t.slice.value)
        if t.value.__class__ is ast.Subscript:
            return inspect(t.value,args)
        else:
            assert t.value.__class__ is ast.Name
            # print("Value",t.value.id)
            return args
            args.append(t.value.id)
i=argv[1]if len(argv)>1 else input()
if i=="--help":
    print("usage: cat input.txt | python3 builder.py > output.txt")
    exit()
t=ast.parse(i,mode='eval')
# print(ast.dump(t,indent=4))
x=inspect(t,[])
#lifo
o=dict()
s=o
while x:
    c=x.pop()
    if len(x)>0:
        n=x[-1]
        # print(c,"next",n)
        if isinstance(n,str):
            s[c]=dict()
        else:
            assert isinstance(n,int)
            s[c]=[None for i in range(n+1)]
    else:
        s[c]=None
    s=s[c]
print(json.dumps(o,indent=4))