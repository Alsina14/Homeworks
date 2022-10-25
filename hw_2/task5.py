import numpy as np

class Star:
    """accepts an absolute stellar magnitude as input"""
    def __init__(self, M):
        self.abs_m = M
        
    def __repr__(self):
        return str(self.abs_m)
        
    
    
    
def find_cluster_magnitude(star_list: list, r:float):
    """accepts as input a list with objects of the Star class and the distance in parsecs,
    returns the apparent magnitude of the cluster of stars from the list"""
    E0 = 2.48*10e-8
    E1 = np.empty((len(star_list)))
    for i in range(len(star_list)):
        m1 = star_list[i].abs_m - 5 + 5*np.log10(r)
        E1[i] = E0*2.512**(-m1)
        E = np.sum(E1)
    return -2.5*np.log10(E/E0)
    
    

s1, s2, s3 = Star(25), Star(18), Star(30) 
star_list = [s1, s2, s3]

print("Cluster magnitude =", find_cluster_magnitude(star_list, 20))

#sorting the list of objects of the Star type in ascending order of their absolute magnitude
print("Sort list of Stars:", sorted(star_list, key = lambda x: x.abs_m))