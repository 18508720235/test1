import sys,http.client
from logger import logger
import socket
s='127.0.0.1:62605'
p='JzmL2020'
q=sys.argv[1]
d=sys.argv[2]
try:
    u='http://%s/send_urgent/%s/11/%s/1/%s'%(s,p,q,d)
    c=http.client.HTTPConnection(s)
    c.request(method="GET",url=u)
    print('sending:', u)
    # logger.info(u)
except Exception as e:
    print("send massage except:%s"%e)
    logger.info(e)