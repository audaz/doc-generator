
# ======================================================================
# === Auto Generated Code All Edits Will Be Lost During Regeneration ===
# ======================================================================
    
# ----- Get Availability Domains
data "oci_identity_availability_domains" "AvailabilityDomains" {
    compartment_id = var.tenancy_ocid
}
# => Access via the "element" function will allow for wrap-arounf of the returned Availability Domain List. 
# => This will allow the same code to be used in 3 AD Regions and 1 AD Regions.
locals {
    ad-1_name = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 0).name
    ad-2_name = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 1).name
    ad-3_name = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 2).name
    ad-1_id   = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 0).id
    ad-2_id   = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 1).id
    ad-3_id   = element(data.oci_identity_availability_domains.AvailabilityDomains.availability_domains, 2).id
}
# ------ Get All Service OCID
data "oci_core_services" "AllRegionServices" {
    filter {
        name = "cidr_block"
        values = ["all-*"]
        regex = true
    }
}
locals {
    all_services_id          = data.oci_core_services.AllRegionServices.services[0].id
    all_services_cidr_block  = data.oci_core_services.AllRegionServices.services[0].cidr_block
    all_services_destination = data.oci_core_services.AllRegionServices.services[0].cidr_block
}
# ------ Get Object Storage Service OCID
data "oci_core_services" "ObjectStorageRegionServices" {
    filter {
        name = "cidr_block"
        values = ["\\w*objectstorage"]
        regex = true
    }
}
locals {
    objectstorage_services_id          = data.oci_core_services.ObjectStorageRegionServices.services[0].id
    objectstorage_services_cidr_block  = data.oci_core_services.ObjectStorageRegionServices.services[0].cidr_block
    objectstorage_services_destination = data.oci_core_services.ObjectStorageRegionServices.services[0].cidr_block
}
    