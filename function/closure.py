def outer_func(numbers = []):
    print(f"numbers: {numbers}")

    def inner_func():
        print(f"max: {max(numbers)}")
        print(f"min: {min(numbers)}")

    print("call inner_func() within outer_func()")
    inner_func()

    return inner_func

print("call outer_func()")
f = outer_func([1, 2, 3, 4])

print("call inner_func() outside of outer_func()")
f()