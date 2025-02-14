# ✅ 1.2 Iniciar un contenedor con parámetros básicos

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)

# Start an Nginx container exposing port 8080
print(wc.start_container("nginx", "my_nginx", ports={"80/tcp": 8080}))
