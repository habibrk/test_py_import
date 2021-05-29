from ..foo.foo import Foo

def test_Foo():     
    print(Foo)

    f = Foo()

    print(f.set_attr('Hi'))

    print(f.get_attr())

    print(f.bar)

    print(f.bar.get_attr())