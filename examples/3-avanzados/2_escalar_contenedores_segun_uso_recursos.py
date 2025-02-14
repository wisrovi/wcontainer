# ✅  3.2 Detectar uso alto de recursos y escalar contenedores

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


resource_metrics = wc.get_resource_metrics()

# If CPU usage is higher than 80%, start another instance
if float(resource_metrics["cpu_usage"].strip("%")) > 80:
    print(wc.start_container("nginx", "nginx_replica"))

# 🔹 Explicación: Si el uso de CPU del sistema supera el 80%, lanza una nueva instancia del contenedor para distribuir la carga.
