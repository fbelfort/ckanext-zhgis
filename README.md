ckanext-zhgis
=============

Harvester for the Office for Spatial Development of the Canton of Zurich

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-zhgis.git#egg=ckanext-zhgis --src /home/www-data
cd /home/www-data/ckanext-zhgis
pip install -r pip-requirements.txt
python setup.py develop
```

Make sure to add `zhgis` and `zhgis_harvest` to `ckan.plugins` in your config file.

## Run harvester

```bash
source /home/www-data/pyenv/bin/activate
paster --plugin=ckanext-zhgis zhgis_harvest gather_consumer -c development.ini &
paster --plugin=ckanext-zhgis zhgis_harvest fetch_consumer -c development.ini &
paster --plugin=ckanext-zhgis zhgis_harvest run -c development.ini
```

CSW query:

```bash
source /home/www-data/pyenv/bin/activate
# Show output from CSW, 'query' is typically the name of a dataset like 'swissboundaries3D'
paster --plugin=ckanext-zhgis zhgis csw <query> -c development.ini

# Show output from CSW, 'id' being the unique identifier of a dataset like 'b3bd50ae-b026-40a0-8b39-1cbcd4c4ac98'
paster --plugin=ckanext-zhgis zhgis cswid <id> -c development.ini
```
