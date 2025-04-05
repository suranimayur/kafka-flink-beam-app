from setuptools import setup, find_packages

setup(
    name='kafka-beam-app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'apache-beam[gcp]==2.46.0',
        'confluent-kafka==2.3.0',
        'SQLAlchemy==1.4.49',
        'sqlite3-api==2.0.1',
        'pytest==7.4.3',
        'pytest-cov==4.1.0',
        'python-dateutil==2.8.2',
        'pytz==2024.1',
        'pyyaml==6.0.1',
        'loguru==0.7.2'
    ],
    python_requires='>=3.8',
    author='Mayur Surani',
    author_email='suranimayur@gmail.com',
    description='A data processing pipeline using Apache Beam that processes messages from Kafka',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/suranimayur/kafka-flink-beam-app',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
) 