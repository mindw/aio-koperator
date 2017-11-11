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
        'aiohttp==2.3.2',
        'cchardet<3',
        'uvloop<1.0;platform_system!="Windows"',
        'aiohttp-jinja2<1.0',
        'prometheus_async==17.5.0',
        'click >= 6.7, <=7',
        'kubernetes==4.0.0b1',
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
