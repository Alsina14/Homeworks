def depth_list(x):
    """defines the maximum nesting depth of the list"""
    if type(x) is list:
        return 1 + max(map(depth_list, x))
    return 0
    

