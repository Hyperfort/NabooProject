output "test_id" {
  value = datadog_synthetics_test.api_test.id
}

output "monitor_id" {
  value = datadog_synthetics_test.api_test.monitor_id
}
