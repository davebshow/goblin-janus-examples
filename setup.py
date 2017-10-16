from setuptools import setup


setup(
    name="goblin_janus_examples",
    version="0.1",
    license="MIT",
    author="davebshow",
    author_email="davebshow@gmail.com",
    description="Goblin with JanusGraph examples",
    packages=["examples"],
    install_requires=["goblin==2.1.0rc3"]
)
