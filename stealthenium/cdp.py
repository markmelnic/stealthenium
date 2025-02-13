from json import dumps

def execute_cdp_cmd(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id

    if hasattr(driver.command_executor, '_url'):
        url = driver.command_executor._url + resource
    else:
        url = driver.command_executor._client_config.remote_server_addr + resource

    body = dumps({'cmd': cmd, 'params': params})

    response = driver.command_executor._request('POST', url, body)

    return response.get('value')
