# Python - Django 课程

## 架构图:![架构图](/Users/baidu/Desktop/架构图.png)

## 简述:

```python
MVC模型:  
   
    MVC 架构由三个组件组成 model(模型)、view(视图)、controller(控制器)
    
Django:
  
  django 属于 MVC 架构， 但是django 的Controller 控制器由Django自行管理，Django 重点关注模型是
  model(M) 、 Template(T)、View(V)  = MTV 模型
  
  
  M 代表（Model） 		即数据存取层
  T 代表（Template）  即表示层，html相关
  V 代表（View）			即逻辑层，也称之为代码层，用于获取M层数据在T层进行如何展示桥梁层。
 

```

### 路由:

```python
urls:  
  
  路由是整个项目的入口，定义的url对应到View中的函数。
  

```

##### path:

###### 简述:

```python
path: 
  
  path方法支持俩种访问方式:
      
      path()				// 不支持分组，不支持正则方式匹配
      re_path()			// 支持分组，支持正则方式匹配
      
```

###### 方法:

```python
# 导入模块 
from django.urls import path
from app01.views import *

# 在项目urls.py 中配置路由规则

urlpatterns = [
  
  # 格式
  # path('<路由url>',<视图函数名称>)
  path('admin/',views.admin)
  
]

```

##### Include:

###### 简述:

```python
include:
  每当Django遇到include()时，它都会截断直到该时间点匹配的URL的任何部分，并将剩余的字符串发送到包含的URLconf中以进行进一步处理。
  

关键点:
  
  列url：
  		
    	 www.app01.com/admin/code
      
  列规则:
    	# 第一层urls 配置
      urlpatterns = [
         path('admin/',include('app01.urls')) 
      ]
      
      # 第二层urls 配置
      urlpatterns = [
        path('code/',view.code)
      ]
      
  截胡:
    当用户访问网站，首先到第一层路由 www.app01.com/admin/ 到此匹配成功。
    
  
  将剩下的部分:
    当用户到达admin/后 第一层路由碰到include 会将 剩下的url 部分 分发至
    app01.urls 中，从而完成一次完整的匹配.

  
使用场景:
            |-->   子01程序URL 
  总URL入口 -|      
            |-->   子02程序URL 

```

###### 方法:

```python
# 配置在urls.py
# 导入模块
import django.urls import include
import django.urls import path

urlpatterns = [
  
  # 语法格式
  # path('<url>', include('<子urls.py路径>'))
  # 所有访问带admin/<任意url> 都会路由至子app01 的urls规则中
  path('admin/',include('app01.urls'))
  
]
```

##### re_path:

###### 简述:

```python




```

