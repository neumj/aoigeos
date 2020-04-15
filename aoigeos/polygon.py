import math


class GeoPolygon():
    def __init__(self, srid=4326):
        self.srid = srid

    def from_centroid(self, num_sides, center_latitude, center_longitude, radius_decimal_degrees):
        if num_sides > 2:
            vertices = [None] * (num_sides + 1)
        for i in range(0, num_sides):
            angle_step = 360. / num_sides
            angle_deg = angle_step * i
            angle_rad = math.pi / 180.0 * angle_deg
            y_vert = center_latitude + radius_decimal_degrees * math.sin(angle_rad)
            if abs(y_vert) < 1e-5:
                y_vert = 0
            x_vert = center_longitude + radius_decimal_degrees * math.cos(angle_rad)
            if abs(x_vert) < 1e-5:
                x_vert = 0
            vert = {'x': x_vert, 'y': y_vert}
            vertices[i] = (vert)
            if i == 0:
                vertices[num_sides] = vert
        self.vertices = vertices
        self.center_latitude = center_latitude
        self.center_longitude = center_longitude
        self.radius = radius_decimal_degrees

    def to_wkt(self):
        v_str = ''
        for v in self.vertices:
            v_str = v_str + str(v['x']) + ' ' + str(v['y']) + ','
        v_str = v_str[0:-1]
        self.wkt = 'POLYGON(({v_str}))'.format(v_str=v_str)

    def to_ewkt(self):
        v_str = ''
        for v in self.vertices:
            v_str = v_str + str(v['x']) + ' ' + str(v['y']) + ','
        v_str = v_str[0:-1]
        self.ewkt = 'SRID={srid};POLYGON(({v_str}))'.format(srid=self.srid, v_str=v_str)
