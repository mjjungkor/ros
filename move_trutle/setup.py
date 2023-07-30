from setuptools import setup

package_name = 'move_trutle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'mt=move_trutle.moveTurtle:main',
            'mt2=move_trutle.moveTurtle2:main'
        ],
    },
)
