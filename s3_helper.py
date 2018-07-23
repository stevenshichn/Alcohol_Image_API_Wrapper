from boto.s3.connection import S3Connection
import os

AWS_ACCESS_KEY = 'AKIAJN7PXTJVNYDVS4HA'
AWS_SECRET_KEY = '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'


class S3_Operation(object):
    def __init__(self, aws_access_key = None, aws_secret_key = None):
        if aws_access_key is None:
            self.aws_access_key = AWS_ACCESS_KEY
        else:
            self.aws_access_key = aws_access_key
        if aws_secret_key is None:
            self.aws_secret_key = AWS_SECRET_KEY
        else:
            self.aws_secret_key = aws_secret_key

    def connect_S3(self):
        return S3Connection(self.aws_access_key, self.aws_secret_key)
    
    def get_bucket(self, bucketName):
        conn = self.connect_S3()
        if conn is not None:
            return conn.get_bucket(bucket_name=bucketName)
        else:
            return None;
    
    def download_file(self, bucket_name, file_in_bucket, target_file_in_local, use_exist = True):
        skip_download = False
        try:            
            if os.path.isfile(target_file_in_local):
                if use_exist:            
                    skip_download = True
                else:
                    os.remove(target_file_in_local)
        except:
            print('error in the file deletion')
        finally:
            if not skip_download:
                bucket = self.get_bucket(bucket_name)
                if bucket is not None:
                    key = bucket.get_key(file_in_bucket)
                    if key is not None:
                        print('downloading file : ' + file_in_bucket)
                        key.get_contents_to_filename(target_file_in_local)
                        print('downloaded file : ' + file_in_bucket)
# 
# conn = S3Connection('AKIAJN7PXTJVNYDVS4HA', '/51xBBDANvTdPPt+OU0i3db/uhgrYhWokU7PpjHc') 
# 
# # mybucket = conn.get_bucket('image-recognition-models')
# # print(str(len(mybucket.list())))
# 
# li = conn.get_bucket(bucket_name = 'image-recognition-models')
# print(li)
# key = li.get_key('model_vgg16.h5')
# key.get_contents_to_filename('new_model.h5')
# # li.download_file('model_vgg16.h5', 'new_model.h5')
