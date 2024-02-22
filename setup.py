from setuptools import setup

setup(
    name='hugbbley',
    version='0.1.0',    
    description='A ',
    url='https://github.com/emmano97/fastapi-lens',
    author='Emmanuel Edorh',
    author_email='emmanoedorh@gmail.com',
    # TODO: Check on license
    license='BSD 2-clause',
    packages=['hugbbley'],
    install_requires=["sqlalchemy ~= 1.4",
                      "sqlalchemy-utils",
                      "alembic",
                      "strawberry-graphql",
                      "strawberry-sqlalchemy-mapper",
                      "fastapi",
                      "toml"],
    extras_require={
        "dev": [
            "pytest",
            "faker"
        ]
    },
    # TODO: ADD THE CMD ENTRY
    entry_points={
        "console_scripts": ["hugbbley=hugbbley.core.console.stargaze:main"]
    },
)