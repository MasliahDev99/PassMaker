from setuptools import setup, find_packages


def read_requirements(filename):
    """Lee un archivo de requerimientos y devuelve una lista de dependencias."""
    with open(filename,'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]   

setup(
    name='PassMaker', 
    version='0.1.0', 
    description='PassMaker es una herramienta para la generación,evaluación,gestión de contraseñas. Ofrece seguridad con encriptacion RSA y analisis de fortalezas', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='MasliahDev99',  
    author_email='', 
    url='https://github.com/MasliahDev99/PassMaker', 
    packages=find_packages(), 
    install_requires=read_requirements('requirements.txt'),
    classifiers=[  
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
