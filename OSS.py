import oss2


class Oss(object):
    def __init__(self):
        # oss配置
        access_key = ""
        access_secret = ""
        oss_bucket = ""
        oss_basic_url = ""
        self.auth = oss2.Auth(access_key, access_secret)
        self.bucket = oss2.Bucket(self.auth, oss_basic_url, oss_bucket)

    def get_url(self, key, t1=600):
        # 根据key获取图片链接
        url = self.bucket.sign_url("GET", key, t1)
        return url

    def put_object(self, key, obj):
        # 上传本地文件到oss
        res = self.bucket.put_object(key, obj)
        return res
