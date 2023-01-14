# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import json


def json_encode(result, fail_reason):
    """
        组装成固定格式JSON
    :param result: 业务结果
    :param fail_reason: 失败原因(result为success时为空)
    :return: json_data
    """
    json_data = json.dumps(
        {
            'result': result,
            'fail_reason': fail_reason
        }
    ).encode('utf8')
    return json_data