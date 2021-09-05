# Elasticsearch 7.6 部署方式(裸部署)

```shell
上传部署包:
elasticsearch-7.6.1-linux-x86_64.tar.gz
```

```shell
部署前置系统准备:

1. 创建es服务启动用户
   useradd es
   password es  // 密码自定义
   usermode -d <es家目录> es  // elascticsearch 家目录
   
2. 将elasticsearch⽤户添加到sudoers
   visudo
   
      es ALL=(ALL) NOPASSWD: ALL	// 100行左右添加
      
2. 修改⽂件限制，添加如下内容
   vim /etc/security/limits.conf
   
     * soft nofile 65536 
     * hard nofile 65536
     * soft nproc 65536
     * hard nproc 65536
     es hard memlock unlimited
     es soft memlock unlimited 
     
3.调整虚拟内存&最⼤并发连接
  vim /etc/sysctl.conf 
  
      vm.max_map_count=262144  
      fs.file-max=655360
      vm.swappiness=1
```

```shell
开始部署服务：

1. 解压部署包
   tar -zxvf /home/es/elasticsearch-7.6.1-linux-x86_64.tar.gz -C /usr/local/
```

```shell
1.修改es配置文件:
cd /usr/local/elasticsearch-7.6.1/config
2.请根据自己机器的IP修改（注意集群三节点都需要修改）
vim elasticsearch.yml

    #集群名称，通过组播的⽅式通信，通过名称判断节点属于哪个集群
    cluster.name: ytc_inner_elk_cluster
    #节点名称，要唯⼀
    node.name: ytc_inner_elk1
    #数据存放位置
    path.data: /data/elasticsearch/data
    #⽇志存放位置
    path.logs: /data2/elasticsearch/logs
    #es绑定的ip地址，开放⽹卡地址
    network.host: 这里写上你ES服务器的IP
    #是否开启master ⻆⾊选举
    node.master: true
    #是否开启数据节点⻆⾊
    node.data: true
    #是否锁住内存，避免交换(swapped)带来的性能损失,默认值是: false
    bootstrap.memory_lock : true
    #确定节点将多久决定开始选举或加⼊现有的群集之前等待
    discovery.zen.ping_timeout : 60s
    #向主节点发送加⼊请求
    discovery.zen.join_timeout : 60s
    #在主选举期间将忽略来⾃不符合master资格的节点
    discovery.zen.master_election.ignore_non_master_pings : true
    #选举最⼩同意数
    discovery.zen.minimum_master_nodes : 1
    #只要有这么多数据或主节点已加⼊集群，就可以恢复
    gateway.recover_after_nodes : 1
    #预期在群集中的（数据或主节点）节点数
    gateway.expected_nodes : 1
    #如果未达到预期的节点数，则恢复过程将等待配置的时间，然后再尝试恢复。
    gateway.recover_after_time : 5m
    #开放端⼝号http端口
    http.port: 9200
    #集群间传输端⼝号
    transport.tcp.port: 9300
    #集群发现 host 池
    discovery.seed_hosts: ["这里写上你ES服务器的IP","多节点写多个"]
    #集群初始化 master 节点，新增特性写一个IP即可
    cluster.initial_master_nodes: ["node1"]
    # 如果需要开启xpack认证功能将下面配置信息写入配置文件
    xpack.security.enabled: true
	  xpack.security.transport.ssl.enabled: true
	  xpack.security.transport.ssl.verification_mode: certificate
	  xpack.security.transport.ssl.keystore.path: elastic-certificates.p12
	  xpack.security.transport.ssl.truststore.path: elastic-certificates.p12
	 
```

初始化目录创建:

```shell
1. 创建数据存储目录以及logs目录（根据实际情况创建）
	 mkdir /data/elasticsearch/{data,logs}
2. 修改目录权限
   chown -R es.es /data/elasticsearch/

```

开启xpack：

```shell
注意: 如果需要开启xpack需要执行下面动作创建集群通信证书。
1. 创建集群通信正式
cd /usr/local/elasticsearch-7.6.1/bin
   #下面两个指令的交互，都直接输入回车即可。
   ./elasticsearch-certutil ca
   ./elasticsearch-certutil cert --ca elastic-stack-ca.p12
   
2. 移动证书文件
cd /usr/local/elasticsearch-7.6.1/
mv elastic-certificates.p12 elastic-stack-ca.p12  ./config

3. 修改证书权限
cd config
chmod 777 elastic-certificates.p12
chmod 777 elastic-stack-ca.p12

4. 若为集群，将证书分发至所有节点下config文件中
   #分发至所有节点
   #证书需要放置在elasticsearch config目录下面，所有节点都需要放
   scp elastic-certificates.p12 elastic-stack-ca.p12   root@XX.XX.XX.XX:/XX/XX
 
```

启动服务:

```shell
1. 切换到es用户启动
su - es

2. 启动服务验证
./bin/elasticsearch  // 此步骤为前台启动 ，如果没有任何报错信息 请加上 -d 选项丢到后台运行

3. 验证服务

curl http://127.0.0.1:9200   // 注意如果在开启xpack 认证功能后 访问会出现如下信息，需要创建密码

# {"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}},"status":401} 

4. 创建xpack密码:
cd /usr/local/elasticsearch-7.6.1/bin

   ./elasticsearch-setup-passwords interactive
   # 首先输入y.
   # 然后输入想要设置的密码
   # 大致会让你输入 elacstic 、kinan、logstas 等信息的密码 ，都正常输入就行
   
5. 在次访问es集群：
# elastic 为默认的账号
# baidu@123 为上面设置的密码
curl -XGET -u elastic:baidu@123 http://10.61.187.45:7200/_cat/nodes   // 看见正常集群信息表示es部署完成 
```

