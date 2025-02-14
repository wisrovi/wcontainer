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