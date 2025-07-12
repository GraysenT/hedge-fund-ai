```python
import functools

def prevent_self_damage(func):
    """
    Decorator to prevent self-damaging signals by catching exceptions and preventing
    recursive errors by maintaining a call count.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'call_count'):
            wrapper.call_count = 0
        if wrapper.call_count > 10:
            raise RecursionError("Maximum recursion limit reached to prevent damage")
        wrapper.call_count += 1
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error prevented: {e}")
            result = None
        finally:
            wrapper.call_count -= 1
        return result
    return wrapper

@prevent_self_damage
def critical_system_function(data):
    """
    Example function that could potentially cause harm to the system if not handled properly.
    """
    if data == 1:
        return data
    elif data == 0:
        raise ValueError("Zero is not a valid input")
    else:
        return critical_system_function(data - 1) + critical_system_function(data - 2)

# Example usage
if __name__ == "__main__":
    print(critical_system_function(5))  # Test with a safe input
    print(critical_system_function(0))  # Test with a harmful input
```
This Python code defines a decorator `prevent_self_damage` that wraps around functions to protect them from self-damaging behaviors such as excessive recursion and unhandled exceptions. The `critical_system_function` demonstrates how this decorator can be applied to a recursive function, protecting the system from potential harm.