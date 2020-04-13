def dispatch_dict(operator,x,y):
    return {
        'add':lambda :x+y,
        'sub':lambda :x-y,
        'mul':lambda :x*y,
        'div':lambda :x//y,
        'pow':lambda :x**y,
    }.get(operator,lambda :'not present')()

print("The output is",dispatch_dict('mul',2,4))
print("The output is",dispatch_dict('add',6,8))
print("The output is",dispatch_dict('pow',2,10))
print("The output is",dispatch_dict('exp',5,7))
