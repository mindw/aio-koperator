import click
import click_log
import logging
from . import __version__
from aiohttp import web
from prometheus_async.aio.web import server_stats

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


_REF = '<html><body><a href="/metrics">Metrics</a></body></html>'


async def _cheap(request):
    """
    A view that links to metrics.

    Useful for cheap health checks.
    """
    logger.info('called _cheap')
    return web.Response(text=_REF, content_type='text/html')


def create_app(loop=None):
    app = web.Application(loop=loop)
    app.router.add_get('/healthz', healthz)
    app.router.add_get('/metrics', server_stats)
    # Catch all requests
    app.router.add_get('/', _cheap)

    return app


async def healthz(request):

    logger.info('healthz')
    return web.HTTPOk()


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option('-p', '--port', type=click.INT, default=8080)
@click.version_option(version=__version__)
def cli(port):
    """ aiohttp server implementing k8s backend server with custom errors """

    log_format = '%a %l %u %t "%r" %s %b "%{X-Request-ID}o" "%{User-Agent}i"'

    app = create_app()
    web.run_app(app, port=port, access_log_format=log_format)
