#!/usr/bin/python3
# -*-coding:utf-8-*-

"""Send a reply from the proxy without sending any data to the remote server."""

import os
import subprocess
from collections import Sequence

from mitmproxy import http, ctx, command, types

proxy_dir = os.path.expanduser('~/.mitmproxy/json/')

# 自定义路径
custom_map = {}


class POPProxy:

    def __init__(self):
        self.proxy = False
        if not os.path.exists(proxy_dir):
            os.makedirs(proxy_dir)

    def response(self, flow: http.HTTPFlow) -> None:
        ctx.log.info('map response')
        if self.proxy:
            map_local(flow)

    # set proxy status
    @command.command("pop.proxy")
    def set_proxy(self, proxy: bool) -> None:
        self.proxy = proxy
        ctx.log.alert("proxy " + str(proxy))

    # toggle proxy status
    @command.command("pop.proxy_toggle")
    def toggle_proxy(self) -> None:
        self.proxy = not self.proxy
        ctx.log.alert("proxy " + str(self.proxy))

    # save response to local file
    @command.command("pop.save_response")
    def save_response(self, flows: Sequence[http.flow.Flow]) -> None:
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                save_response(f, False)

    # save response to local file and open it
    @command.command("pop.save_response_edit")
    def save_response_edit(self, flows: Sequence[http.flow.Flow]) -> None:
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                save_response(f, True)

    @command.command("pop.map_local")
    def map_local(self, flow: http.flow.Flow, path: types.Path) -> None:
        ctx.log.info('map local: %s >> %s' % (flow.request.path, path))
        custom_map[flow.request.path] = path


def map_local(flow: http.HTTPFlow):
    path = flow.request.path
    if path in custom_map:
        proxy_file = custom_map[path]
    else:
        proxy_file = get_proxy_file_path(flow)
    if os.path.exists(proxy_file):
        with open(proxy_file, 'r') as file:
            flow.response.headers['map_local'] = 'true'
            flow.response = http.Response.make(200, file.read(), flow.response.headers)


def save_response(flow: http.HTTPFlow, edit: bool):
    proxy_file = get_proxy_file_path(flow)
    with open(proxy_file, 'w') as file:
        file.write(flow.response.text)
        ctx.log.alert("Saved")

    if edit:
        subprocess.call(['st', proxy_file])


def get_proxy_file_path(flow: http.HTTPFlow):
    if flow.response and 'Content-Type' in flow.response.headers and 'application/json' in flow.response.headers['Content-Type']:
        return os.path.join(proxy_dir, '%s.json' % '_'.join(flow.request.path_components))
    else:
        return os.path.join(proxy_dir, '_'.join(flow.request.path_components))


addons = [
    POPProxy()
]
