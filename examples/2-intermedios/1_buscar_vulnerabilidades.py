# ✅ 2.2 Escanear una imagen Docker en busca de vulnerabilidades con Trivy

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)


# Scan the latest Nginx image for security vulnerabilities
print(wc.scan_image_with_trivy("nginx"))

