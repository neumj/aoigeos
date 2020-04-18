import math

def decimaldegrees_meters(dd_float):
    """convert decimal degrees to meters.  based on standard decimal degree

    """
    dd = dd_float * 111325.
    return dd


def meters_decimaldegrees(meters_float):
    """convert meters to decimal degrees.  based on standard decimal degree

    """
    m = meters_float / 111325.
    return m


def great_circle_distance(lat_start, lon_start, lat_end, lon_end):
    EARTH_EQUATORIAL_RADIUS = 6335437
    EARTH_POLAR_RADIIUS = 6399592
    EARTH_AVERAGE_RADIUS = 6372795
    distance = 0.0
    r = EARTH_AVERAGE_RADIUS
    if round(lat_start,6) == round(lon_start,6) == round(lat_end,6) == round(lon_end,6):
        distance = 0
    a1 = lat_start * math.pi / 180
    b1 = lon_start * math.pi / 180
    a2 = lat_end * math.pi / 180
    b2 = lon_end * math.pi / 180
    distance = math.acos(math.cos(a1)*math.cos(b1)*math.cos(a2)*math.cos(b2) + \
                         math.cos(a1)*math.sin(b1)*math.cos(a2)*math.sin(b2) + \
                         math.sin(a1)*math.sin(a2))
    return distance

def wkt_to_geojson_coords(wkt):
    raw_coords_str = wkt.split('((')[1].split('))')[0].strip()
    clean_coords = [[float(a.strip().replace(' ',',').split(',')[0]), \
                 float(a.strip().replace(' ',',').split(',')[1])] \
                for a in raw_coords_str.split(',')]
    return [clean_coords]