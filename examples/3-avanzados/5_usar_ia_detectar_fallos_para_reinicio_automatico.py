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
