# ✅  3.1 Autoajuste dinámico de recursos

import random
import time
from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Dynamically adjust CPU and RAM allocation every 10 seconds
for _ in range(5):
    print(
        wc.adjust_container_resources(
            "my_nginx", cpu_limit=random.uniform(1.0, 4.0), memory_limit="512m"
        )
    )
    time.sleep(10)


# 🔹 Explicación: Cada 10 segundos, el script cambia la cantidad de CPU y RAM asignada al contenedor.