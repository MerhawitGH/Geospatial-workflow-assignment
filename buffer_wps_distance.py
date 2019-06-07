# ---------------------
# Calculating the buffer distance  using WPS specification
# ---------------------
from osgeo import ogr
from osgeo import osr


def title():
    return "Buffer distance calculation"


def abstract():
    return "A function that Computes a buffer area around this geometry having the given width"


def inputs():
    return [
        ['geom', 'Input feature', 'The given area', 'application/json', True],
        ['distance', 'distance', 'The width of the buffer', 'integer', True]
    ]


def outputs():
    return [['result', 'Polygon', 'A polygonal geometry representing the buffer region', 'application/json']]


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
