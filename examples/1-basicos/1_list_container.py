# ✅ 1.1 Listar contenedores en ejecución

from wcontainer import Wcontainer


wc = Wcontainer(verbose=True)

# List only running containers
print(wc.list_containers())

# List all containers (including stopped ones)
print(wc.list_containers(all_containers=True))
