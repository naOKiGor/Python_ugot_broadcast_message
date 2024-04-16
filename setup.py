from setuptools import setup

setup(
    name='uGot_Broadcast_message',
    version='0.0.1',
    description='=A broadcast communication Python Library for uGot',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=['ugot_broadcast_message', 'ugot_broadcast_message_pb2'],
    author='naOKiGor',
    author_email='evenaoki@gmail.com',
    url='https://github.com/naOKiGor/Python_ugot_broadcast_message',
    install_requires=['protobuf>=5.26.1'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)