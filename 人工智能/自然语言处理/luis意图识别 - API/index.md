# luis意图识别 - API

[微软API地址](https://westus.dev.cognitive.microsoft.com/docs/services/5890b47c39e2bb17b84a55ff/operations/5890b47c39e2bb052c5b9c2f)

## 公共参数

### 可用位置
|位置|域名|
|-|-|
|美国西部| westus.api.cognitive.microsoft.com|
|西欧| westeurope.api.cognitive.microsoft.com|
|澳大利亚东部|australiaeast.api.cognitive.microsoft.com|

### 请求连接
 
https://[location].api.cognitive.microsoft.com/luis/api/v2.0/apps/


### 请求HTTP头

|key|value|描述|
|-|-|-|
|Content-Type(可选)|string|发送给API的请求体类型|
|Ocp-Apim-Subscription-Key|string|发送给API的请求体类型|


## 返回值

### Response 200

正确返回

### Response 400

请求错误，可能是参数错误

### Response 401

无法访问，未授权

可能得原因：

- 应该使用著作key，但是使用终端key
- 著作key不可用或为空
- 著作key与区域不符
- 你不是所有人或协作者
- API调用顺序不对


### Response 403

月配额超限

### Response 429

速率超限
