# Kubernetes - flannel



##### docker网桥：

```shell

bridge:	虚拟一块网桥，全部桥接在此网桥上。
		
joined:

open:	使用宿主机网络名称空间

none:	不使用网络




```

```shell

请求:
container -> eth0 -> veth -> 网桥 -> 物理机eth0  -> DNAT  -> SNAT 



k8s 网络通信：

	容器间通信:
	
	pod之间通信:
	
	pod service之间通信:
		通过proxy组件实现，基于iptabls或ipvs规则生成
			
	外部与service通信:


```

