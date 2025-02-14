# ✅ 2.3 Generar un informe de errores de un contenedor

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Analyze logs and generate a JSON error report for the container
print(wc.generate_error_report("my_nginx", output_file="nginx_errors.json"))


