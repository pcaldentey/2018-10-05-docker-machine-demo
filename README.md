# 2018-10-05-docker-machine-demo

https://p.caldentey.org/2018/11/23/docker-machine-con-generic-driver/



Construye la máquina vagrant
```
cd HOMEPROJ/vagrant && vagrant up
```
IP: 192.168.43.8

Usuario ssh vagrant, durante la construcción de la máquina se han copiado las claves del usuario que ejecuta *vagrant up*, con lo que para conectarte a la máquina virtual ejecuta

```
ssh vagrant@192.168.43.8
```

Y ahora puedes seguir jugando con dockermachine siguiendo los pasos del [post](https://p.caldentey.org/2018/11/23/docker-machine-con-generic-driver/)

