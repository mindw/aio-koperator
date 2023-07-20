import setuptools

setuptools.setup(
    name='aio-koperator',
    version='0.1.0',
    url='https://github.com/mindw/aio-koperator',

    author='Gabi Davar',
    author_email='grizzly.nyo@gmail.com',

    description='A Kubernetes operator reference using aiohttp',
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    python_requires='>=3.6',

    install_requires=[
        'aiohttp==3.8.5',
        'cchardet<3',
        'uvloop<1.0;platform_system!="Windows"',
        'aiohttp-jinja2<2',
        'prometheus_async==19.2.0',
        'click >= 7, <=8',
        'kubernetes==12.0.1',
        'click-log'
    ],

    tests_require=[
        'pytest-aiohttp'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'aio-koperator=aio_koperator.server:cli']
    },
)
