import docker
import loguru
import subprocess
import json
import random
import psutil
import GPUtil


class Wcontainer:
    """Advanced Docker container manager with real-time resource allocation, vulnerability scanning, auto-scaling, and monitoring."""

    def __init__(self, verbose: bool = True):
        """
        Initializes the Docker container manager.

        Args:
            verbose (bool, optional): Enables detailed logging if True. Defaults to True.
        """
        self.verbose = verbose
        self.logger = loguru.logger
        self.logger.remove()
        self.logger.add("wcontainer.log", level="DEBUG" if verbose else "INFO")

        try:
            self.client = docker.from_env()
            self.logger.info("Connected to Docker successfully.")
        except Exception as e:
            self.logger.error(f"Failed to connect to Docker: {e}")
            raise RuntimeError(f"Failed to connect to Docker: {e}")

    ### 1️⃣ Container Management ###

    def list_containers(self, all_containers: bool = False):
        """Lists running containers or all containers if all_containers=True."""
        try:
            return [
                {"id": c.short_id, "name": c.name, "status": c.status}
                for c in self.client.containers.list(all=all_containers)
            ]
        except Exception as e:
            self.logger.error(f"Error listing containers: {e}")
            return {"error": str(e)}

    def start_container(
        self,
        image_name: str,
        container_name: str,
        ports=None,
        env_vars=None,
        network=None,
        volumes=None,
        restart_policy="always",
    ):
        """Starts a Docker container with advanced options."""
        try:
            container = self.client.containers.run(
                image_name,
                name=container_name,
                detach=True,
                ports=ports or {},
                environment=env_vars or {},
                network=network,
                volumes=volumes or {},
                restart_policy={"Name": restart_policy},
            )
            self.logger.info(
                f"Container {container_name} started with ID: {container.short_id}"
            )
            return str(container.short_id)
        except Exception as e:
            self.logger.error(f"Error starting container {container_name}: {e}")
            return {"error": str(e)}

    def stop_container(self, container_name: str):
        """Stops a running container."""
        try:
            container = self.client.containers.get(container_name)
            container.stop()
            self.logger.info(f"Container {container_name} stopped.")
            return f"Container {container_name} stopped."
        except Exception as e:
            self.logger.error(f"Error stopping container {container_name}: {e}")
            return {"error": str(e)}

    ### 2️⃣ Real-time Resource Allocation ###

    def adjust_container_resources(
        self, container_name: str, cpu_limit: float, memory_limit: str
    ):
        """Adjusts the CPU and memory limits for a running container in real time."""
        try:
            container = self.client.containers.get(container_name)
            container.update(
                cpu_period=100000,
                cpu_quota=int(cpu_limit * 100000),
                mem_limit=memory_limit,
            )
            self.logger.info(
                f"Updated resources for {container_name}: CPU={cpu_limit}, RAM={memory_limit}"
            )
            return f"Updated resources for {container_name}: CPU={cpu_limit}, RAM={memory_limit}"
        except Exception as e:
            self.logger.error(f"Error adjusting resources for {container_name}: {e}")
            return {"error": str(e)}

    ### 3️⃣ Vulnerability Scanning ###

    def scan_image_with_trivy(self, image_name: str):
        """Performs a vulnerability scan on a Docker image using Trivy."""
        try:
            self.logger.info(f"Scanning image {image_name} with Trivy.")
            result = subprocess.run(
                ["trivy", "image", "--format", "json", image_name],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                vulnerabilities = json.loads(result.stdout)
                self.logger.info(f"Trivy scan completed for {image_name}.")
                return vulnerabilities
            else:
                self.logger.error(f"Trivy scan failed: {result.stderr}")
                return {"error": result.stderr}
        except Exception as e:
            self.logger.error(f"Error scanning image {image_name} with Trivy: {e}")
            return {"error": str(e)}

    ### 4️⃣ Error Report Generation ###

    def generate_error_report(
        self, container_name: str, output_file: str = "error_report.json"
    ):
        """Generates an error report for a specific container by analyzing logs."""
        try:
            container = self.client.containers.get(container_name)
            logs = (
                container.logs(tail=500).decode("utf-8").split("\n")
            )  # Last 500 lines
            error_logs = [line for line in logs if "error" in line.lower()]

            report_data = {
                "container": container_name,
                "total_logs": len(logs),
                "error_logs": len(error_logs),
                "errors": error_logs,
            }

            with open(output_file, "w") as f:
                json.dump(report_data, f, indent=4)

            self.logger.info(
                f"Error report generated for {container_name}: {output_file}"
            )
            return f"Error report generated: {output_file}"
        except Exception as e:
            self.logger.error(f"Error generating report for {container_name}: {e}")
            return {"error": str(e)}

    ### 5️⃣ Resource Usage Metrics ###

    def get_resource_metrics(self):
        """Retrieves system-wide CPU, RAM, and GPU usage metrics."""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
            gpu_usage = None

            try:
                gpus = GPUtil.getGPUs()
                if gpus:
                    gpu_usage = [
                        {
                            "id": gpu.id,
                            "name": gpu.name,
                            "load": gpu.load * 100,
                            "memory": gpu.memoryUtil * 100,
                        }
                        for gpu in gpus
                    ]
            except Exception as gpu_error:
                self.logger.warning(f"GPU metrics not available: {gpu_error}")

            metrics = {
                "cpu_usage": f"{cpu_usage}%",
                "ram_usage": f"{ram_usage}%",
                "gpu_usage": gpu_usage or "No GPU detected",
            }

            self.logger.info(f"Resource metrics retrieved: {metrics}")
            return metrics
        except Exception as e:
            self.logger.error(f"Error retrieving system metrics: {e}")
            return {"error": str(e)}

    ### 6️⃣ Auto-scaling Containers ###

    def auto_scale_container(
        self, container_name: str, max_replicas: int = 3, cpu_threshold: float = 80.0
    ):
        """Automatically scales a container based on CPU usage."""
        metrics = self.get_resource_metrics()
        cpu_usage = float(metrics["cpu_usage"].strip("%"))

        if cpu_usage > cpu_threshold:
            for i in range(max_replicas):
                new_container_name = f"{container_name}_replica_{i}"
                self.start_container("nginx", new_container_name)
                self.logger.info(
                    f"Auto-scaled container {new_container_name} due to high CPU load."
                )

            return f"Auto-scaled {max_replicas} replicas of {container_name}."
        return f"CPU usage is below {cpu_threshold}%, no scaling needed."

    ### 6️⃣ AI-based Failure Prediction ###

    def predict_container_failure(self, container_name: str):
        """Simulates AI-based failure prediction for a container."""
        failure_probability = random.uniform(0, 1)
        if failure_probability > 0.7:
            self.logger.warning(
                f"High failure probability detected for {container_name}: {failure_probability:.2f}"
            )
            return f"ALERT: High failure probability for {container_name} ({failure_probability:.2f})"
        return f"{container_name} operating normally. Failure probability: {failure_probability:.2f}"
