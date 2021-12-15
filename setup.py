import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'oop_stpprofile',      
  packages = ['oop_stpprofile'], 
  version = '0.0.1',  
  license='MIT', 
  description = 'oop_stpprofile by Suntipap1312',
  long_description=DESCRIPTION,
  author = 'Suntipap1312',                 
  author_email = 'Suntipap1312@gmail.com',     
  url = 'https://github.com/oop_stpprofile/oop_stpprofile',  
  download_url = 'https://github.com/oop_stpprofile/oop_stpprofile/archive/v0.0.1.zip',  
  keywords = ['oop', 'stpprofile', 'suntipap1312'],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)