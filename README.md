<p align="center">
  <a href="https://pypi.org/project/wcontainer/"><img src="https://img.shields.io/pypi/v/wcontainer?style=for-the-badge&logo=pypi&color=3b82f6" alt="PyPI version" /></a>
  <a href="https://linkedin.com/in/wisrovi-rodriguez"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://wisrovi.dev"><img src="https://img.shields.io/badge/Author-wisrovi.dev-111827?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portal" /></a>
  <a href="https://orcid.org/0009-0005-0710-1861"><img src="https://img.shields.io/badge/ORCID-0009--0005--0710--1861-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License" /></a>
</p>

# Wcontainer

**Wcontainer** is a library for specific docker container operations. The library offers a number of modules that make using docker containers easier and simpler.

# Description

Wcontainer is a library for specific docker container operations. The library offers a number of modules that make using docker containers easier and simpler.

## Installation

To install the library, use `pip`:

```bash
pip install wcontainer
```

# Description

The **wcontainer** library offers a number of modules that make using docker containers easier and simpler. The library is designed to be used in conjunction with the **docker** library, which is the official Python client for the Docker Engine API.

# Examples

This directory contains a collection of examples that demonstrate the usage of various modules and functionalities in this project. Each subfolder corresponds to a specific module and includes example scripts to help you understand how to use that module.

## Directory Structure

The examples are organized as follows:

```
examples/
    4-monitoreo_RT/
        monitoreo_tiempo_real.py
    3-avanzados/
        1_ajuste_dinamico_recursos.py
        2_escalar_contenedores_segun_uso_recursos.py
        3_escalar_antes_desplegar.py
        4_autonamizar_generacion_informe_errores.py
        5_usar_ia_detectar_fallos_para_reinicio_automatico.py
    2-intermedios/
        1_buscar_vulnerabilidades.py
        2_read_metrics.py
        3_informe de errores.py
    1-basicos/
        1_list_container.py
        2_start_new_container.py
        3_new_resources.py
```

## How to Use

1. Navigate to the module folder of interest, e.g., `examples/module1/`.
2. Open the `README.md` in that folder to get detailed information about the examples.
3. Run the scripts directly using:
   ```bash
   python example1.py
   ```

## Modules and Examples

### 1-basicos

#### Description

This module demonstrates specific functionalities.

- **1_list_container.py**: Example demonstrating functionality.

```python
# ✅ 1.1 Listar contenedores en ejecución

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)

# List only running containers
print(wc.list_containers())

# List all containers (including stopped ones)
print(wc.list_containers(all_containers=True))
```

- **2_start_new_container.py**: Example demonstrating functionality.

```python
# ✅ 1.2 Iniciar un contenedor con parámetros básicos

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)

# Start an Nginx container exposing port 8080
print(wc.start_container("nginx", "my_nginx", ports={"80/tcp": 8080}))
```

- **3_new_resources.py**: Example demonstrating functionality.

```python
# ✅ 1.3 Ajustar recursos de un contenedor en tiempo real

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Limit a running container to 2 CPU cores and 1GB RAM
print(wc.adjust_container_resources("my_nginx", cpu_limit=2.0, memory_limit="1g"))
```

### 2-intermedios

#### Description

This module demonstrates specific functionalities.

- **1_buscar_vulnerabilidades.py**: Example demonstrating functionality.

```python
# ✅ 2.2 Escanear una imagen Docker en busca de vulnerabilidades con Trivy

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Scan the latest Nginx image for security vulnerabilities
print(wc.scan_image_with_trivy("nginx"))
```

- **2_read_metrics.py**: Example demonstrating functionality.

```python
# ✅ 2.1 Obtener métricas de uso de CPU, RAM y GPU

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Get system-wide CPU, RAM, and GPU usage
print(wc.get_resource_metrics())
```

- **3_informe de errores.py**: Example demonstrating functionality.

```python
# ✅ 2.3 Generar un informe de errores de un contenedor

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Analyze logs and generate a JSON error report for the container
print(wc.generate_error_report("my_nginx", output_file="nginx_errors.json"))
```

### 3-avanzados

#### Description

This module demonstrates specific functionalities.

- **1_ajuste_dinamico_recursos.py**: Example demonstrating functionality.

```python
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
```

- **2_escalar_contenedores_segun_uso_recursos.py**: Example demonstrating functionality.

```python
# ✅  3.2 Detectar uso alto de recursos y escalar contenedores

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


resource_metrics = wc.get_resource_metrics()

# If CPU usage is higher than 80%, start another instance
if float(resource_metrics["cpu_usage"].strip("%")) > 80:
    print(wc.start_container("nginx", "nginx_replica"))

# 🔹 Explicación: Si el uso de CPU del sistema supera el 80%, lanza una nueva instancia del contenedor para distribuir la carga.
```

- **3_escalar_antes_desplegar.py**: Example demonstrating functionality.

```python
# ✅  3.3 Escanear imágenes antes de desplegar en producción

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Run a security check before deployment
scan_result = wc.scan_image_with_trivy("my_application_image")

# If vulnerabilities are found, abort deployment
if "error" not in scan_result and any(scan_result.get("Vulnerabilities", [])):
    print("Deployment aborted: vulnerabilities detected.")
else:
    print("No critical vulnerabilities found, proceeding with deployment...")
    print(
        wc.start_container(
            "my_application_image", "production_app", ports={"5000/tcp": 5000}
        )
    )

# 🔹 Explicación: Antes de desplegar una imagen, el sistema revisa vulnerabilidades con Trivy. Si se encuentran fallos críticos, se cancela el despliegue.
```

- **4_autonamizar_generacion_informe_errores.py**: Example demonstrating functionality.

```python
# ✅  3.4 Automatizar la generación de informes de errores

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Check logs of multiple containers and generate error reports
containers = ["my_nginx", "backend_service", "database"]
for container in containers:
    print(wc.generate_error_report(container, output_file=f"{container}_errors.json"))


# 🔹 Explicación: Revisa los logs de varios contenedores y genera informes de errores individuales en formato JSON.
```

- **5_usar_ia_detectar_fallos_para_reinicio_automatico.py**: Example demonstrating functionality.

```python
# ✅  3.5 Detectar fallos en contenedores con IA y reiniciarlos automáticamente

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


containers = ["my_nginx", "backend_service"]

for container in containers:
    failure_prediction = wc.predict_container_failure(container)
    print(failure_prediction)

    if "ALERT" in failure_prediction:
        print(f"Restarting {container} due to high failure probability...")
        print(wc.start_container("nginx", f"{container}_restarted"))


# 🔹 Explicación: Usa la predicción de fallos con IA y reinicia automáticamente los contenedores con alta probabilidad de error.
```

### 4-monitoreo_RT

#### Description

This module demonstrates specific functionalities.

- **monitoreo_tiempo_real.py**: Example demonstrating functionality.

```python
# ✅  4️. Ejemplo Completo: Monitoreo en Tiempo Real

from wcontainer import Wcontainer
import time


wc = Wcontainer(verbose=True)


while True:
    print("\n📊 Checking system resources...")
    print(wc.get_resource_metrics())

    print("\n🔍 Scanning image for vulnerabilities...")
    print(wc.scan_image_with_trivy("nginx"))

    print("\n📂 Checking error logs for running containers...")
    containers = ["my_nginx", "backend_service"]
    for container in containers:
        print(wc.generate_error_report(container))

    print("\n⚡ Adjusting container resources...")
    print(wc.adjust_container_resources("my_nginx", cpu_limit=2.0, memory_limit="1g"))

    print("\n🛑 Predicting failures in containers...")
    for container in containers:
        failure_prediction = wc.predict_container_failure(container)
        print(failure_prediction)

        if "ALERT" in failure_prediction:
            print(f"Restarting {container} due to high failure probability...")
            print(wc.start_container("nginx", f"{container}_restarted"))

    print("\n⏳ Waiting 60 seconds before next check...\n")
    time.sleep(60)


# 🔹 Explicación:
# ✅ Recolecta métricas del sistema cada 60 segundos
# ✅ Escanea la imagen Nginx con Trivy
# ✅ Analiza los logs de errores de todos los contenedores
# ✅ Ajusta dinámicamente la asignación de recursos
# ✅ Detecta fallos con IA y reinicia contenedores automáticamente
```

# License

MIT

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👤 Autor & Afiliación Oficial

* **William Steve Rodriguez Villamizar (Wisrovi)**
* **Cargo:** Principal AI Engineer & Applied AI Solutions Architect | Scientific Researcher
* 📧 **Email:** [wisrovi.rodriguez@gmail.com](mailto:wisrovi.rodriguez@gmail.com) / [wisrovi@wisrovi.dev](mailto:wisrovi@wisrovi.dev)
* 🌐 **Portal Oficial:** [wisrovi.dev](https://wisrovi.dev)
* 💼 **LinkedIn:** [wisrovi-rodriguez](https://www.linkedin.com/in/wisrovi-rodriguez/)
* 🆔 **ORCID:** [0009-0005-0710-1861](https://orcid.org/0009-0005-0710-1861)
* 📦 **PyPI:** [pypi.org/user/wisrovi/](https://pypi.org/user/wisrovi/)
* 🐙 **GitHub:** [@wisrovi](https://github.com/wisrovi)
