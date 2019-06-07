# ---------------------
# Calculating the buffer distance  using WPS specification
# ---------------------
from osgeo import ogr
from osgeo import osr


def title():
    return "Buffer distance calculation"


def abstract():
    return "A function that calculate buffer distance using vector data."


def inputs():
    return [
        ['geom', 'Input feature', 'The Neighnourhood ', 'application/json', True],
        ['distance', 'distance', 'The buffer distance in meter', 'integer', True]
    ]


def outputs():
    return [['result', 'Polygon', '1000 meter buffer', 'application/json']]


def execute(parameters):
    geom = parameters.get('geom')
    distance = parameters.get('distance')
    if (geom is not None) and (distance is not None):
        geom = geom['value']
        distance = distance['value']

    pt = ogr.CreateGeometryFromJson(geom)
    poly = pt.Buffer(distance)
    #print("Content-type: application/json")
    print()
    print( "%s buffered by %d is %s" % (pt.ExportToJson(), distance, poly.ExportToJson()))
