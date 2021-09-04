#!/bin/bash

# elasticsearch 分片



Elasticsearch_Adderss=""
Elasticsearch_Port=""
Elasticsearch_node=""




function action() {


curl -XPOST -H 'Content-Type: application/json' http://${Elasticsearch_Adderss}:${Elasticsearch_Port}/_cluster/reroute -d '{


           "commands" : [


                {

                        "allocate_stale_primary": {

                                "index": "'$1'", 
                                "shard": '$2',
                                "node": "'${Elasticsearch_node}'",
                                "accept_data_loss": true



                        }




                        }



        ]


}


'


}


function main() {

for i in $(curl -s  -H 'Content-Type: application/json' http://${Elasticsearch_Adderss}:${Elasticsearch_Port}/_cat/shards|grep -i "UNASSIGNED"|awk '{print $1"@"$2}');do
        index=$(echo ${i}|awk -F@ '{print $1}')
        shards=$(echo ${i}|awk -F@  '{print $2}')

        count=$(curl -s  -H 'Content-Type: application/json' http://${Elasticsearch_Adderss}:${Elasticsearch_Port}/_cat/shards|grep -i "UNASSIGNED"|awk '{print $1}'|wc -l)

        echo “剩余index:$count”
        sleep 3

        action ${index} ${shards}
done





}
main



