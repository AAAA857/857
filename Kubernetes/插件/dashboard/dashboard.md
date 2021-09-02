# Kubernetes - Dashboard

##### 简述:

```shell
dashboard 用于图形展示集群状态，副本数量，资源使用率信息。

官方文档:  https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/dashboard/dashboard.yaml

```

##### 安装:

```shell
# 下载最新官方编排文件
https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/dashboard/dashboard.yaml


# 下载镜像
镜像根据编排文件中的image进行下载


# 修改svc 为NodePort 类型 或者使用ingress进行外部访问
# 登录方式

  1.生产配置文件
  2.生产token进行登录
  
  
# token 登录方式

  1.创建serviceaccount
  
    kubectl create serviceaccount dashboard
    
  2.创建clusterrolebinding
    kubectl create clusterrolebinding --cluster-role=admin-cluster --serviceaccount=dashboard
    
  3.获取token
  
    kubectl get secret   // 获取secret
    kubectl describe secret -n <namespace> <dashboard-token>  // 复制里面的token ID



```

