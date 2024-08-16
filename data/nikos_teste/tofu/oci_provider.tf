
# ======================================================================
# === Auto Generated Code All Edits Will Be Lost During Regeneration ===
# ======================================================================
    
terraform {
    required_version = ">= 1.5.0"
}

# ------ Connect to Provider
provider "oci" {
    tenancy_ocid     = var.tenancy_ocid
    user_ocid        = var.user_ocid
    fingerprint      = var.fingerprint
    private_key_path = var.private_key_path
    region           = var.region
}

# ------ Home Region Provider
data "oci_identity_region_subscriptions" "HomeRegion" {
    tenancy_id = var.tenancy_ocid
    filter {
        name = "is_home_region"
        values = [true]
    }
}
locals {
    home_region = lookup(element(data.oci_identity_region_subscriptions.HomeRegion.region_subscriptions, 0), "region_name")
}

provider "oci" {
    alias            = "home_region"
    tenancy_ocid     = var.tenancy_ocid
    user_ocid        = var.user_ocid
    fingerprint      = var.fingerprint
    private_key_path = var.private_key_path
    region           = local.home_region
}

output "Home_Region_Name" {
    value = local.home_region
}
    