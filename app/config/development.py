SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'mrjNHumbQ1bk8uCTS2srPiIpMmCv8hkXORSH6oJ7lymEmL1G9GVaRgkwlfwPabHytVEbteArL30IfPWmWFNLs6gjoK8uRxYAdLfP'
JWT_SECRET_KEY = 'wTlEln0fvBXv114odFMBatwUIGJgo1Dtlm8CB6pencCKSKh2qRvtLzGalcYHDQLIQxd2RQhFRdyfme9AqgU1vICU466nq1z6b8Rx'
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']