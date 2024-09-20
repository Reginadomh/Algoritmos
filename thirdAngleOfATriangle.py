# To find the third angle of a triangle, we can use the fact that the sum of all interior angles in a triangle is always 180 degrees.

def third_angle(angle1, angle2):
    # The third angle is simply 180 minus the sum of the two given angles
    return 180 - (angle1 + angle2)

# Test cases
print(third_angle(60, 60))  # Should return 60
print(third_angle(45, 45))  # Should return 90
print(third_angle(30, 90))  # Should return 60
