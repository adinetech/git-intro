radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
    
def area_cylinder(r,h):
    return 2 * 3.14 * r * (r+h)

def volume_cylinder(r,h):
    return 3.14 * r * r * h

print("The area of the cylinder is: ", area_cylinder(radius, height))
print("The volume of the cylinder is: ", volume_cylinder(radius, height))
