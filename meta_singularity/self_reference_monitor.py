Here's a Python script that monitors how often modules cite themselves or others recursively. This script uses a simplified model where each module can cite other modules, and the script counts the citations recursively. It assumes that the module relationships are defined in a dictionary where keys are module names and values are lists of cited modules.

```python
def count_citations(modules, module_name, visited=None, depth=0):
    if visited is None:
        visited = set()
    
    # Avoid infinite recursion by checking if we've already visited this module
    if module_name in visited:
        return 0
    visited.add(module_name)
    
    # Base case: if the module cites no other modules
    if module_name not in modules or not modules[module_name]:
        return 0
    
    # Recursive case: count citations for each cited module
    count = 0
    for cited in modules[module_name]:
        if cited == module_name:
            count += 1  # Self-citation
        count += count_citations(modules, cited, visited.copy(), depth + 1)
    
    return count

def main():
    # Example of module citations
    modules = {
        'ModuleA': ['ModuleB', 'ModuleC'],
        'ModuleB': ['ModuleA', 'ModuleC'],
        'ModuleC': ['ModuleA'],
        'ModuleD': ['ModuleA', 'ModuleB', 'ModuleC', 'ModuleD']  # Self-citing and citing others
    }
    
    # Calculate and print the citation counts for each module
    for module in modules:
        print(f"{module} cites others (including self-citations) {count_citations(modules, module)} times recursively.")

if __name__ == "__main__":
    main()
```

This script defines a function `count_citations` that takes a dictionary of modules, a module name, and a set of visited modules to avoid infinite loops in case of cyclic citations. The function counts how many times each module is cited, including self-citations, by recursively checking each cited module.

The `main` function sets up an example dictionary representing modules and their citations, then iterates over each module to print out the total count of citations, including recursive ones. The script handles self-citations and cyclic dependencies by using a set of visited modules to prevent revisiting the same module in a recursive path.