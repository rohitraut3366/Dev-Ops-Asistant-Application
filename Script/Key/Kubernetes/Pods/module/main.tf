terraform {
  required_version = ">= 0.12"
}
provider "kubernetes" {
  config_context_cluster   = "minikube"
}
resource "kubernetes_pod" "test" {
  metadata {
    name = "${var.pod_name}"
  }
  labels{
    
  }
  spec{
    container {
      image = "${var.container_image}"
      name  = "${var.container_name}"
    }
  }
}