## OBSERVABILITY

### PREREQUISITES
> Create the folder "elasticsearch_data": ```mkdir elasticsearch_data```

> Create the network "observability": ```docker network create observability```

> Create the file "metricbeat.yml" in the path "beats/metric" with the content below:
~~~yml
metricbeat.modules:
- module: docker
  metricsets: ["container", "cpu", "diskio", "event", "healthcheck", "image", "info", "memory", "network"]
  hosts: ["unix:///var/run/docker.sock"]
  period: 10s

- module: elasticsearch
  metricsets: ["node", "node_stats", "cluster_stats", "index"]
  period: 10s
  hosts: ["elasticsearch:9200"]  


output.elasticsearch:
  hosts: ["elasticsearch:9200"]

setup.kibana:
  host: "kibana:5601"

setup.dashboards.enabled: true
~~~

### METRIC SET UP
> Go to: ```http://localhost:5601/app/home#/tutorial_directory/metrics```
> Choose: "Docker metrics", below the page click on "Check data", should show the message: "Data successfully received from this module"

### HEARTBEAT 
> Check if the app is up
> Create the file "heartbeat.yml" in the path " beats/heartbeat" with the content below:
~~~yml
heartbeat.monitors:
- type: http
  schedule: '@every 5s'
  urls:
    - http://elasticsearch:9200
    - http://kibana:5601
    - http://app:8000

- type: icmp
  schedule: '@every 5s'
  hosts:
    - elasticsearch
    - kibana
    - apm
    - metricbeat

processors:
- add_cloud_metadata: ~

output.elasticsearch:
  hosts: 'elasticsearch:9200'
  username: 'elastic'
  password: 'changeme'
~~~
> Access: http://localhost:5601/app/uptime
___

> To access Elastic via web: ```http://localhost:5601/```