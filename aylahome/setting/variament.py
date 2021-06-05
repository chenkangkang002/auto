'''公共的变量'''

# HOST = 'https://abp-test.ayla.com.cn'   #测试环境
HOST = 'https://abp-prod.ayla.com.cn'   #正式环境
# HOST_H5 = 'https://miya-h5-test.ayla.com.cn' #测试环境H5
HOST_H5 = 'https://miya-h5.ayla.com.cn/'  #正式

HOME_URL = '/api/v1/miya/home'
DEVICE_LIST_URL = '/api/v1/miya/device/list'
PROPERTIES_URL = '/api/v1/miya/device/{device}/properties'  #获取设备属性
MODEL_TEMPLATE_URL = '/api/v3/miya/spark/devicetypes/ZBSW0-A000002/modelTemplate'    #获取设备的物模板
TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMzI2Nzg2MDU4MDg3NjY5Nzk2IiwidXNlck5hbWUiOiIxNTg4NTUzNzgyMCIsImxvZ2luVHlwZSI6IjEiLCJsb2dpblNvdXJjZSI6IjUiLCJheWxhQXBwbGljYXRpb25JZCI6IjYiLCJ0eXBlIjoiYXV0aF90b2tlbiIsImlhdCI6MTYyMjczMDg0Mn0.l-m70rm1sXXHz7ITxy5AzxyL4EJgBcOGXUAeTw5QWOQ'

HOME_NAME = '原始家庭'
TIMEOUT = 5