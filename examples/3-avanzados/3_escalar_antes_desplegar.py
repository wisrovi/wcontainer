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
