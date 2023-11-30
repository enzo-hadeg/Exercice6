provider "github" {
  token = "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"
}
resource "github_repository" "mon_repo" {
  name        = "nom_du_repo"
  description = "Créé avec Terraform"
  private     = true
}
variable "nom_du_repo" {
  description = "Nom du dépôt GitHub"
  type        = string
}