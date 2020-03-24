import os
from glob import glob

from setuptools import setup


package_name = 'telegram_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Loy van Beek',
    maintainer_email='loy.vanbeek@gmail.com',
    description='Send and receive messages with the Telegram chat application',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telegram_ros2_bridge = telegram_ros2.telegram_ros2_bridge:main'
        ],
    },
)
