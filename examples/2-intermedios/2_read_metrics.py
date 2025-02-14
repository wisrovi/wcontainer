# ✅ 2.1 Obtener métricas de uso de CPU, RAM y GPU

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Get system-wide CPU, RAM, and GPU usage
print(wc.get_resource_metrics())
