def sort_list(x: list):
    """receives a list of lists with numbers as input 
    and sorts them in ascending order of the sum inside these lists"""
    x.sort(key=sum)
    return x
    

