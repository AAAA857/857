# kubernetes - RBAC篇

##### 简述:

```shell
   Kubernetes 认证分为角色+权限，角色有 serviceAccount ，userAccount，角色仅限能不能

与ApiServer交互，至于能执行什么操作则是权限所控制。
```

##### RBAC:

```shell

role:

     操控范围: namespace
     功能: 定义了可以在操作范围内执行的哪些动作
     
     例如:     
         resource:  pods/deployment			// 需要操作的组资源 
         vers: get,list,delete,watc			// 对应上面的组资源所拥有的执行动作
		 
		 # 创建一个role规则
		 kubectl create role yintiecheng-ua --verb=get,list,delete --resource=pods


rolebinding:

		控制范围: namespace
		功能:  将对应的serviceAccount 或 userAccount 绑定到 role  规则之上
		
		例如:
				# 绑定useraccount
		    kubectl create rolebinding  yintiecheng-ua --role=yintiecheng-ua --user=yintiecheng 
		    # 绑定serviceaccount
		    kubectl create rolebinding yintiecheng-sa --role=yintiecheng --serviceaccount=yintiecheng
		
		
cluserrole:


cluserrolebinding:





```

###### 绑定规则:

```shell

# 基于某个namespace权限授权

  role + rolebinding + user
 
# 基于全局namespace权限授权

  cluserrole + clusterrolebinding + user
  
# 统一role规则授权不同namespace。
  rolebinding + cluserrole + user  

```

