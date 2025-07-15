def trade(a, b, item_a, item_b):
    if item_a in a.inventory and item_b in b.inventory:
        a.inventory.remove(item_a)
        b.inventory.remove(item_b)
        a.inventory.append(item_b)
        b.inventory.append(item_a)
        return "✅ Trade successful"
    return "❌ Trade failed"