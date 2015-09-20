__author__ = 'zephyre'

from datetime import datetime

import alfred
from bson import ObjectId
from bson.errors import InvalidId


def process(query_str):
    """ Entry point """
    query_str = query_str.strip().lower() if query_str else ''

    results = []
    if query_str == 'gen':
        ret = gen_objectid_result()
        results.append(ret)

        oid = ret.attributes['arg']
        results.extend(get_generation_time(oid))
    else:
        oid = parse_query_value(query_str)
        if oid:
            results.extend(get_generation_time(oid))

    if results:
        xml = alfred.xml(results)  # compiles the XML answer
        alfred.write(xml)  # writes the XML back to Alfred


def get_generation_time(oid):
    """
    Get the alfred result for the ObjectId generation time
    :param oid:
    :return:
    """
    import pytz
    from tzlocal import get_localzone

    gt = oid.generation_time.replace(tzinfo=pytz.UTC)
    t0 = pytz.UTC.localize(datetime.utcfromtimestamp(0))

    tz_cn = pytz.timezone('Asia/Shanghai')
    t1 = tz_cn.normalize(gt)

    tz_local = get_localzone()
    t2 = tz_local.normalize(gt)

    total_seconds = int((gt - t0).total_seconds())

    return [
        alfred.Item(title=str(gt), subtitle='Generation time in UTC', icon='', attributes={'arg': gt}),
        alfred.Item(title=str(t1), subtitle='Generation time in Asia/Shanghai', icon='', attributes={'arg': t1}),
        alfred.Item(title=str(t2), subtitle='Generation time in local timezone: %s' % tz_local.zone, icon='',
                    attributes={'arg': t1}),
        alfred.Item(title=str(total_seconds), subtitle='Unix Epoch Timestamp', icon='',
                    attributes={'arg': total_seconds})
    ]


def gen_objectid_result():
    oid = ObjectId()

    return alfred.Item(title=str(oid), subtitle='Generated ObjectId', icon='', attributes={'arg': oid})


def parse_query_value(query_str):
    """
    Parse the query string. If the input is invalid or doesn't exist, None will be returned
    :param query_str:
    :return:
    """

    try:
        oid = ObjectId(query_str)
    except InvalidId:
        oid = None

    return oid


# def alfred_items_for_value(oid):
# index = 0
# alfred_items = [
# alfred.Item(title=str(oid), subtitle='Original ObjectId', attributes={
# 'uid': alfred.uid(index),
#             'arg': oid,
#         }, icon='icon.png')
#     ]
#     return alfred_items


if __name__ == '__main__':
    try:
        arg = alfred.args()[0]
    except IndexError:
        arg = None
    process(arg)

