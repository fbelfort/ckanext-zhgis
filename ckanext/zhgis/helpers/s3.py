from boto.s3.connection import S3Connection
from ckan.plugins.core import SingletonPlugin, implements
from ckan.plugins.interfaces import IConfigurable
from pylons import config

class S3():
    def __init__(self):
        try:
            self.key = config['ckanext.zhgis.s3_key']
            self.token = config['ckanext.zhgis.s3_token']
            self.bucket_name = config['ckanext.zhgis.s3_bucket']
        except KeyError as e:
            raise ConfigEntryNotFoundError("'%s' not found in config" % e.message)

    def __repr__(self):
        return "<S3 key:%s token:%s bucket_name:%s>" % (self.key, self.token, self.bucket_name)

    def list(self, prefix=None):
        conn = S3Connection(self.key,self.token)
        bucket = conn.get_bucket(self.bucket_name)
        return bucket.list(prefix=prefix)

class ConfigEntryNotFoundError(Exception):
    pass
