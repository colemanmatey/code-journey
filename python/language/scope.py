"""
A scope is a textual region of a Python program where a namespace is directly accessible. 
“Directly accessible” here means that an unqualified reference to a name attempts to find 
the name in the namespace. Although scopes are determined statically, they are used dynamically. 

At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:
1. the innermost scope, which is searched first, contains the local names
2. the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, 
contain non-local, but also non-global names
3. the next-to-last scope contains the current module's global names
4. the outermost scope (searched last) is the namespace containing built-in names
"""

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    # local
    do_local()
    print("After local assignment:", spam)

    # nonlocal
    do_nonlocal()
    print("After nonlocal assignment:", spam)

    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
