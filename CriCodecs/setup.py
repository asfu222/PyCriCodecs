from setuptools import setup, Extension

setup(
    name="CriCodecs",
    version="0.2.4",
    ext_modules=[Extension('CriCodecs', ["adx.cpp", "CriCodecs.cpp", "crilayla.cpp", "hca.cpp"])]
)