# ✅ 1.3 Ajustar recursos de un contenedor en tiempo real

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Limit a running container to 2 CPU cores and 1GB RAM
print(wc.adjust_container_resources("my_nginx", cpu_limit=2.0, memory_limit="1g"))
