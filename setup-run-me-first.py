# Hey there! If you found this, these are just a bunch of python modules that you can auto-install with this 1 script.
# Just make sure you have pip and python first before this.
import os
import time

libraries = [
    'colorama',
    'pyautogui',
    'keyboard',
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    'scipy',
    'scikit-learn',
    'tensorflow',
    'keras',
    'opencv-python',
    'pillow',
    'requests',
    'beautifulsoup4',
    'pyyaml',
    'flask',
    'django',
    'sqlalchemy',
    'pytest',
    'pytest-cov',
    'nltk',
    'gensim',
    'spacy',
    'tweepy',
    'pygame',
    'pyglet',
    'pygame-menu',
    'pytz',
    'python-dateutil',
    'arrow',
    'tabulate',
    'termcolor',
    'progressbar2',
    'tqdm',
    'wget',
    'networkx',
    'pydot',
    'graphviz',
    'folium',
    'geopy',
    'shapely',
    'pyshp',
    'cartopy',
    'bokeh',
    'plotly',
    'dash',
    'dash-bootstrap-components',
    'dash-core-components',
    'dash-html-components',
    'dash-renderer',
    'streamlit',
    'fastapi',
    'uvicorn',
    'starlette',
    'flask-restful',
    'flask-socketio',
    'websockets',
    'asyncio',
    'aiohttp',
    'pyserial',
    'python-socketio',
    'flask_sqlalchemy',
    'marshmallow',
    'sqlalchemy-utils',
    'psycopg2',
    'cx_Oracle',
    'pyodbc',
    'colour',
    'requests beautifulsoup4'
]

print("Alright, get ready to install over 70 common and required Python libraries for PythonOS. This will probably take a while, so just hang tight...")
time.sleep(5)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("GO!")
for lib in libraries:
    os.system(f'pip install {lib}')
print("Dependency installation complete. You may now boot kernel.py.")
time.sleep(5)