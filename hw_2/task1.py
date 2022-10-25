import math

class CelestialObject:
    def __init__(self, dec, ra):
        self.dec = dec
        self.ra = ra
        
    def show_coordinates(self):
        print((self.dec, self.ra))
        
    def upper_culmination(self, latitude):
        if self.dec <= latitude:
            h = 90 - latitude + self.dec
        else:
            h = 90 + latitude - self.dec
        return h
    
    def lower_culmination(self, latitude):
        return latitude + self.dec - 90
    
    
    
    
class Star(CelestialObject):
    """takes the temperature in kelvins and the radius in the radius of the sun.
    Calculates the luminosity in the luminosities of the sun"""
    def __init__(self, t, r, **kwargs):
        super().__init__(**kwargs)
        self.temperature = t
        self.radius = r
        t_sun = 5780
        self.luminosity = r**2 * (t/t_sun)**4
        
        
        
class Galaxy(CelestialObject):
    """takes the distance in megaparsecs and the apparent magnitude.
    It calculates the absolute stellar magnitude from them"""
    def __init__(self, dist, mag, **kwargs):
        super().__init__(**kwargs)
        self.distance = dist
        self.apparent_mag = mag
        dist = dist/1000
        self.abs_mag = mag + 5 - 5*math.log10(dist)
        
        

star1 = Star(5000, 400, dec = 36, ra = 10)
star2 = Galaxy(10, 25, dec = 45, ra = 15)
print("Luminosity =", star1.luminosity, "sun luminosity")
print("Absolute magnitude =", star2.abs_mag)
print("Show star1 coordinates:")
star1.show_coordinates()
print("Star2 upper culmination:", star2.upper_culmination(60))