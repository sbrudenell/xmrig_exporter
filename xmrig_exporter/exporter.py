import argparse
import http.server
import logging
import sys

import prometheus_client

import xmrig_exporter


def main():
    parser = argparse.ArgumentParser("Xmrig Exporter")

    parser.add_argument("--port", type=int, default=9189)
    parser.add_argument("--bind_address", default="0.0.0.0")
    parser.add_argument("--url", required=True)
    parser.add_argument("--token")
    parser.add_argument("--verbose", "-v", action="count")

    args = parser.parse_args()

    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(stream=sys.stdout, level=level)

    collector = xmrig_exporter.XmrigCollector(args.url, token=args.token)

    prometheus_client.REGISTRY.register(collector)

    handler = prometheus_client.MetricsHandler.factory(
            prometheus_client.REGISTRY)
    server = http.server.HTTPServer(
            (args.bind_address, args.port), handler)
    server.serve_forever()
