terraform {
  required_providers {
    datadog = {
      source = "DataDog/datadog"
    }
  }
}

resource "datadog_synthetics_test" "api_test" {
  type    = "api"
  subtype = "http"
  name    = var.name
  status  = "live"

  message = <<EOT
    Synthetic API Test for ${var.name}
    Environment: ${var.environment}
  EOT

  request_definition {
    method  = var.method
    url     = var.url
    timeout = 30
  }

  locations = var.private_locations

  assertion {
    type     = "statusCode"
    operator = "is"
    target   = "200"
  }
  assertion {
    type     = "responseTime"
    operator = "lessThan"
    target   = "2000"
  }

  options_list {
    tick_every = var.tick_every
    retry {
      count    = 2
      interval = 3000
    }
    follow_redirects    = true
    min_location_failed = 1
    monitor_name        = var.name
    monitor_priority    = 2
  }

  tags = var.tags
}
