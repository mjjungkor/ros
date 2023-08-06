from setuptools import setup
from glob import glob
import os

package_name = 'mj_pkg'
share_dir='share/'+package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (share_dir+'/launch',glob(os.path.join('launch','*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mjjung',
    maintainer_email='mjjungkor@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simplepub=mj_pkg.simplepublisher:main',
            'simplesub=mj_pkg.simplesubscriber:main',
            'simpletimepub=mj_pkg.simpletimepublisher:main',
            'simpletimesub=mj_pkg.simpletimesubscriber:main',
            'messagepub=mj_pkg.messagepublisher:main',
            'messagesub1=mj_pkg.messagesubscriber1:main',
            'messagesub2=mj_pkg.messagesubscriber2:main',
            'messagetimepub=mj_pkg.simpletimepublisher:main',
            'messagetimesub=mj_pkg.messageTimeSubscriber:main',
            'simplesss=mj_pkg.SimpleServiceServer:main',
            'simplessc=mj_pkg.SimpleServiceClient:main',
            'simplesas=mj_pkg.SimpleActionServer:main',
            'simplesac=mj_pkg.SimpleActionClient:main'
        ],
    },
)
