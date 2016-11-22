import pycurl
from io import BytesIO
import socket
import time

urlList = ['www.google.cl', 'www.gmail.com', 'www.inmetrics.cl', 'www.github.com']
#urlList = ['bancapersonas.bancoestado.cl']
#url = 'google.com'

for url in urlList:
	buffer = BytesIO()
	retrieved_headers = BytesIO()
	print 'Obteniendo datos para : %s' % url
	dns_start = time.time()
	ip_address = socket.gethostbyname(url)
	dns_end = time.time()


	print 'DNS time            = %.3f seg - %.3f ms' % ((dns_end - dns_start), ((dns_end - dns_start) * 1000))
	print 'DNS IP            = %s ' % (ip_address)

	c = pycurl.Curl()
	c.setopt(c.URL, 'http://'+url+'/')
	c.setopt(c.WRITEDATA, buffer)
	c.setopt(c.FOLLOWLOCATION, True)
	#c.setopt(c.VERBOSE, True)
	#c.setopt(c.HEADERFUNCTION, retrieved_headers)
	c.perform()
	body = buffer.getvalue()

	print('TOTAL_TIME: %f seg. - %.2f ms' % (c.getinfo(c.TOTAL_TIME), (c.getinfo(c.TOTAL_TIME) * 1000))) 
	print('CONNECT_TIME: %.3f seg.' % c.getinfo(c.CONNECT_TIME))
	print('PRETRANSFER_TIME: %.3f seg' % c.getinfo(c.PRETRANSFER_TIME))
	print('STARTTRANSFER_TIME: %.3f s' % c.getinfo(c.STARTTRANSFER_TIME))
	print('REQUEST_URL: %s' % url)
	print('EFFECTIVE_URL: %s' % c.getinfo(c.EFFECTIVE_URL))
	print('HTTP_CODE: %d' % c.getinfo(c.HTTP_CODE))
	print('NAMELOOKUP_TIME: %.3f seg' % c.getinfo(c.NAMELOOKUP_TIME))
	print('CONNECT_TIME: %f' % c.getinfo(c.CONNECT_TIME))
	print('REDIRECT_TIME: %f' % c.getinfo(c.REDIRECT_TIME))
	print('REDIRECT_COUNT: %d' % c.getinfo(c.REDIRECT_COUNT))
	print('RESPONSE_CODE: %d' % c.getinfo(c.RESPONSE_CODE))
	print('PRIMARY_IP: %s' % c.getinfo(c.PRIMARY_IP))
	print('PRIMARY_PORT: %s' % c.getinfo(c.PRIMARY_PORT))
	print('OS_ERRNO: %d' % c.getinfo(c.OS_ERRNO))

	#print body
	print retrieved_headers

	c.close()