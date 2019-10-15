def add_to_dict(d, k,v):
    try:
        old_val = d[k]
        d[k] = old_val + v
    except:
        d[k] = v
