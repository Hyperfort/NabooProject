variable "datadog_api_key" {
  sensitive   = true
  type        = string
  description = "Datadog API key"
}

variable "datadog_app_key" {
  sensitive   = true
  type        = string
  description = "Datadog APP key"
}

variable "datadog_site" {
  type        = string
  description = "Datadog site (eg. datadoghq.com, datadoghq.eu)"
}

variable "environment" {
  type        = string
  description = "Current Environment"
}

variable "private_location_id" {
  type        = string
  description = "Datadog Private Location ID"
}
