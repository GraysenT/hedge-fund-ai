def auto_build_module(name, code):
    with open(f'/mnt/data/hedge_fund_ai/generated/{name}.py', 'w') as f:
        f.write(code)
    return f'Module {name} created.'
