import math
from aoigeos import polygon
from aoigeos import converters
from aoigeos import io

class HexGrid():
    def __init__(self, srid=4326):
        self.srid = srid

    def generate_hex_centroids(self, ullat, ullon, radius_dd, nrows, ncols):
        """

        """
        centers = []
        width = float(radius_dd) * 2
        horiz = width * 3.0 / 4.0
        height = (math.sqrt(3.0) / 2.0) * width
        vert = height / 2.0
        for i in range(0, ncols):
            x0 = (i * horiz) + float(ullon)
            for j in range(0, nrows):
                if i % 2 == 0:
                    y0 = float(ullat) - (j * vert * 2)
                else:
                    odlat = ullat - vert
                    y0 = float(odlat) - (j * vert * 2)
                centers.append((x0, y0, radius_dd))
        self.hex_centroids = centers

    def hex_grid_from_centroids(self):
        hex_grid = []
        for c in self.hex_centroids:
            p = polygon.GeoPolygon()
            p.from_centroid(6, c[1], c[0], c[2])
            hex_grid.append(p)
        self.hex_grid = hex_grid

    def wkt_grid_from_hexes(self):
        wkt_grid = []
        for h in self.hex_grid:
            h.to_wkt()
            wkt_grid.append(h.wkt)
        self.hex_grid_wkt = wkt_grid

    def ewkt_grid_from_hexes(self):
        ewkt_grid = []
        for h in self.hex_grid:
            h.to_ewkt()
            ewkt_grid.append(h.ewkt)
        self.hex_grid_ewkt = ewkt_grid

    def geojson_from_wkt_grid(self,out_file):
        geojson = {'type': 'FeatureCollection','features':[]}
        for i in range(0,len(self.hex_grid_wkt)):
            coords = converters.wkt_to_geojson_coords(self.hex_grid_wkt[i])
            row = {'type':'Feature','properties':{'name':'hex' + str(i)},'geometry':{'type':'Polygon'}}
            row['geometry'].update({'coordinates':coords})
            geojson['features'].append(row)
        self.geojson = geojson
        io.write_json(self.geojson,out_file)