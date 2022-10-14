import math
from tracemalloc import start

name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]

radius = [6.83, 7.78, 8.73, 10.32, 1079, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]

height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

cost_per_can = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

volume_per_item = []

surface_area_per_item = []

storage_efficiency_per_item = []



def main() :
    compute_volume()
    compute_surface_area()
    for i in range(11):
        print (f"{name[i]} {compute_storage_efficiency(i):.2f}")
 
    

    

    
    
    

def compute_volume():
    for number, (r, h) in enumerate(zip(radius, height), start=1):
        volume = math.pi * r**2 * h
        volume_per_item.append(volume)
    return volume_per_item



def compute_surface_area():
    for number, (r, h) in enumerate(zip(radius, height), start=1):
        surface_area = (2 * math.pi) * r * (r + h)
        surface_area_per_item.append(surface_area)
    return surface_area_per_item

def compute_storage_efficiency(range):
    storage_efficiency = volume_per_item[range] / surface_area_per_item[range]
    return storage_efficiency



main()
