terraform {
  required_version = ">= 1.0"
  required_providers {
    datadog = {
      source  = "DataDog/datadog"
      version = ">= 3.0"
    }
  }
}

provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
  api_url = "https://api.${var.datadog_site}"
}

module "characters_api_test" {
  source            = "./modules/synthetics_api_test"
  name              = "Characters API - GET /characters (NonProd)"
  url               = "http://host.docker.internal:8000/characters"
  method            = "GET"
  private_locations = [var.private_location_id]
  environment       = var.environment
  tags              = ["service:naboo-project", "component:characters", "env:${var.environment}", "team:mxlOS"]
  tick_every        = 300
}
