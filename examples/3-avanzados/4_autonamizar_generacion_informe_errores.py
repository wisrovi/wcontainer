# ✅  3.4 Automatizar la generación de informes de errores

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Check logs of multiple containers and generate error reports
containers = ["my_nginx", "backend_service", "database"]
for container in containers:
    print(wc.generate_error_report(container, output_file=f"{container}_errors.json"))


# 🔹 Explicación: Revisa los logs de varios contenedores y genera informes de errores individuales en formato JSON.