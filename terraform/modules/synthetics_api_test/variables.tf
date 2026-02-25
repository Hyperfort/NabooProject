variable "name" {
  type = string
}

variable "url" {
  type = string
}

variable "method" {
  type = string
}

variable "private_locations" {
  type = list(string)
}

variable "environment" {
  type = string
}

variable "tags" {
  type = list(string)
}

variable "tick_every" {
  type    = number
  default = 3000
}
