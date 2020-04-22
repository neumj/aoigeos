import geocoder
import yaml
from aoigeos import io
from aoigeos import converters as cv


class Geocode():
    def __init__(self, key_yaml='../env.yml'):
        try:
            with open("../env.yml", 'r') as stream:
                keys = yaml.safe_load(stream)
                self.bing_key = keys['bing_key']
        except:
            self.bing_key = ''

    def osm_all_points(self, location_str, max_return=1000):
        g = geocoder.osm(location_str, maxRows=max_return)
        if g.ok:
            self.geojson_point = g.geojson
        else:
            self.geojson_point = {'status': 'no_match', 'location_str': location_str}

    def osm_best_point(self, location_str, max_return=1000):
        self.osm_all_points(location_str, max_return=1000)
        i = 0
        rank = {'loc': i, 'importance': 0}
        for f in self.geojson_point['features']:
            if f['properties']['importance'] > rank['importance']:
                rank.update({'loc': i, 'importance': f['properties']['importance']})
        winner = self.geojson_point['features'][rank['loc']]
        self.geojson_point = cv.geojson_from_features([winner])

    def geocodefarm_point(self, location_str):
        g = geocoder.geocodefarm(location_str)
        if g.ok:
            self.geojson_point = g.geojson
        else:
            self.geojson_point = {'status': 'no_match', 'location_str': location_str}

    def bing_point(self, location_str):
        g = geocoder.bing(location_str, key=self.bing_key)
        if g.ok:
            self.geojson_point = g.geojson
        else:
            self.geojson_point = {'status': 'no_match', 'location_str': location_str}

    def polygon_from_point_bbox(self):
        ft = cv.feature_from_bbox(self.geojson_point['features'][0]['bbox'])
        self.geojson_polygon = cv.geojson_from_features([ft])

    def write_point(self, out_file):
        io.write_json(self.geojson_point, out_file)

    def write_polygon(self, out_file):
        io.write_json(self.geojson_polygon, out_file)
