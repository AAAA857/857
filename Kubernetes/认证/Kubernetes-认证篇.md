# Kubernetes-认证篇

##### 简述：

```sh
UserAccount:
  一般是指由独立于Kubernetes之外的其他服务管理的用户账号.通常kubectl 命令就是使用到UserAccount 使其能管理k8s，但是userAccount 仅作的认证，对于具体能使用什么需要用到其他授权插件例如RBAC、ABAC等。
```

##### UserAccount创建:

创建私钥：

```shell
(umask 077;openssl genrsa -out yintiecheng.key 2048)
```

###### 生成证书签发请求:

```shell
openssl req -new -key yintiecheng.key -out yintiecheng.csr -subj "/O=k8s/CN=yintiecheng"

参数解释:
O= 组织信息
CN= 用户名 ，该名称为最终的user 名称
```

###### 颁发证书:

```shell
openssl x509 -req -in yintiecheng.csr -CA ca.crt -CAkey ca-key -CAcreateserial -out yintiecheng.crt -days 365

参数解释:
-in     颁发的证书请求
-CA     k8s根证书文件
-CAkey  k8s跟证书私钥文件
-CAcreateserial  指明文件不存在时自动生成
-out    颁发生成的证书文件
-days   证书天数


```

###### kubectl 查看当前配置:

```shell
# 查看当前集群配置
kubectl config view
```



###### kubectl 新增用户：

```shell
# 新增一个用户
kubectl config set set-credentials yintiecheng --client-certificate=./yintiecheng.crt --client-key=./yintiecheng.key --embed-certs=true

参数:
yintiecheng    						//创建的用户名称
--client-certificate			//用户的证书文件
--client-key							//用户的私钥文件
--embed-certs							//隐藏证书文件信息



```

###### kubectl 设置上文:

```shell

# 绑定k8s集群与用户关系
kubectl config set-context  yintiecheng --cluster=kubernetes --user=yintiecheng


参数:
yintiecheng				// 上下文中context名称
--cluster					// config 中cluster 集群名称
--user						// 用户
```

###### kubectl 切换当前使用用户:

```shell

# 切换链接的集群与账户
kubectl config use-context yintiecheng

参数:
yintiecheng 			//对应上面新增的上下文配置名称

# 检查新增当前配置
kubectl config view
```

