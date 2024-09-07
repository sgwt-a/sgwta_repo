from math import sin, cos, acos, atan2, degrees, radians


def get_polar_angles_from_vec(vector):
    x, y, z = vector
    r = vector.length()  # r = root( x^2 + y^2 + z^2 )
    theta = acos(z / r)  # cos^(-1)( z / r )
    phi = atan2(y, x)  # phi = tan^(-1)( y / x )
    return degrees(phi), 0, degrees(theta)


def get_position_by_spherical_params(r, theta, phi):
    theta, phi = radians(theta), radians(phi)
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return x, y, z
