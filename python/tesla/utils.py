import requests
import constant as c
import json
import logging
import sys


def get_json_data(request):
    """

    :param request:
    :return:
    """
    log = logging.getLogger(__name__)
    result = None
    try:
        response = requests.get(request)
        if response.status_code != 200:
            log.error("Error in respond: %s", response.text)
            return result
        result = json.loads(response.text)
    except:
        e = sys.exc_info()[0]
        log.warning("<p>Error: %s</p>" % e)

    return result
