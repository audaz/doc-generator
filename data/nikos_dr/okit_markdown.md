# Documentação da infraestrutura em nuvem

## Description

Created 2024-8-13 15:33:30 via OKIT

--------------------------------------

### Subnets

#### SUB_MGT_PRIV_ASHBURN_03


| Property              | Value                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------- |
| Availability Domain   | Regional                                                                                            |
| Compartment           | [management](#management)                                                                           |
| Name                  | SUB_MGT_PRIV_ASHBURN_03                                                                             |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management)                                                     |
| Private               | True                                                                                                |
| DNS Label             | subprova3                                                                                           |
| CIDR Block            | 172.29.112.0/20                                                                                     |
| Route Table           | [[RTB-PRIV](#rtb-priv)](#[rtb-priv](#rtb-priv))                                                     |
| Security List         | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

## Containers

### Compartments

#### management


Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2023-12-19T15:48:50.869Z |


#### production-cliente-b



Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:44:21.403Z |


#### production-mp



Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2023-12-19T15:51:23.514Z |


#### rtm-fnet



Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-02-14T20:16:13.639Z |


#### sandbox-cliente-b



Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:43:47.898Z |


#### sandbox-mp



Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2023-12-19T15:46:53.344Z |



## Networking

### Virtual Cloud Networks

#### VCN_172.30_PROD_MP


| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | VCN_172.30_PROD_MP |
| DNS Label       | vcn17230prodmp |
| CIDR Blocks     | 172.30.0.0/16 |
| NAT Gateway     | [natgw-01](#natgw-01) |
| Internet Gateway | [igw-01](#igw-01) |
| DRG Attachment  | [DRG_VCN_172_30_PRODUCTION](#drg_vcn_172_30_production) |
| Local Peering Gateway | [Peering-production-rotas-publicas](#peering-production-rotas-publicas) |
| Local Peering Gateway | [Peering-01](#peering-01) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:49:48.370Z |


#### VCN_172.29_MANAGEMENT


| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | VCN_172.29_MANAGEMENT |
| DNS Label       | vcn17229managem |
| CIDR Blocks     | 172.29.0.0/16 |
| NAT Gateway     | [NGW_MGT_PRIV](#ngw_mgt_priv) |
| Internet Gateway | [igw-01](#igw-01) |
| DRG Attachment  | [DRG_VCN_172_29](#drg_vcn_172_29) |
| Local Peering Gateway | [peering-management-01](#peering-management-01) |
| Local Peering Gateway | [teste](#teste) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:48:45.636Z |


### Subnets

#### SUB_MGT_PRIV_ASHBURN_03


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [management](#management) |
| Name            | SUB_MGT_PRIV_ASHBURN_03 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Private         | True |
| DNS Label       | subprova3 |
| CIDR Block      | 172.29.112.0/20 |
| Route Table     | [[RTB-PRIV](#rtb-priv)](#[rtb-priv](#rtb-priv)) |
| Security List   | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:01:08.727Z |


#### SUB_MGT_PRIV_ASHBURN_04


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [management](#management) |
| Name            | SUB_MGT_PRIV_ASHBURN_04 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Private         | True |
| DNS Label       | subproda4 |
| CIDR Block      | 172.29.104.0/24 |
| Route Table     | [[RTB-PRIV](#rtb-priv)](#[rtb-priv](#rtb-priv)) |
| Security List   | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:00:37.308Z |


#### SUB_MGT_PRIV_ASHBURN_02


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [management](#management) |
| Name            | SUB_MGT_PRIV_ASHBURN_02 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Private         | True |
| DNS Label       | subprova1 |
| CIDR Block      | 172.29.102.0/24 |
| Route Table     | [[RTB-PRIV](#rtb-priv)](#[rtb-priv](#rtb-priv)) |
| Security List   | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:59:32.762Z |


#### SUB_MGT_PRIV_ASHBURN_01


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [management](#management) |
| Name            | SUB_MGT_PRIV_ASHBURN_01 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Private         | True |
| DNS Label       | subprodprivashb |
| CIDR Block      | 172.29.100.0/24 |
| Route Table     | [[RTB-PRIV](#rtb-priv)](#[rtb-priv](#rtb-priv)) |
| Security List   | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:59:00.536Z |


#### SUB_MGT_PUB_ASHBURN_01


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [management](#management) |
| Name            | SUB_MGT_PUB_ASHBURN_01 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Private         | False |
| DNS Label       | subprodpubashbu |
| CIDR Block      | 172.29.101.0/24 |
| Route Table     | [[Default Route Table for VCN_172.29_MANAGEMENT](#default-route-table-for-vcn_172.29_management)](#[default-route-table-for-vcn_172.29_management](#default-route-table-for-vcn_172.29_management)) |
| Security List   | [Default Security List for VCN_172.29_MANAGEMENT](#default-security-list-for-vcn_172.29_management) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:58:23.933Z |


#### SUB_PROD_PRIV_ASHBURN_03


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [production-mp](#production-mp) |
| Name            | SUB_PROD_PRIV_ASHBURN_03 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Private         | True |
| DNS Label       | subprod4 |
| CIDR Block      | 172.30.112.0/20 |
| Route Table     | [[RTB_PROD_MP_PRIV](#rtb_prod_mp_priv)](#[rtb_prod_mp_priv](#rtb_prod_mp_priv)) |
| Security List   | [Default Security List for VCN_172.30_PROD_MP](#default-security-list-for-vcn_172.30_prod_mp) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:57:13.634Z |


#### SUB_PROD_PRIV_ASHBURN_04


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [production-mp](#production-mp) |
| Name            | SUB_PROD_PRIV_ASHBURN_04 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Private         | True |
| DNS Label       | subprod04 |
| CIDR Block      | 172.30.104.0/24 |
| Route Table     | [[RTB_PROD_MP_PRIV](#rtb_prod_mp_priv)](#[rtb_prod_mp_priv](#rtb_prod_mp_priv)) |
| Security List   | [Default Security List for VCN_172.30_PROD_MP](#default-security-list-for-vcn_172.30_prod_mp) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:56:40.540Z |


#### SUB_PROD_PRIV_ASHBURN_02


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [production-mp](#production-mp) |
| Name            | SUB_PROD_PRIV_ASHBURN_02 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Private         | True |
| DNS Label       | subprodprivb1 |
| CIDR Block      | 172.30.102.0/24 |
| Route Table     | [[RTB_PROD_MP_PRIV](#rtb_prod_mp_priv)](#[rtb_prod_mp_priv](#rtb_prod_mp_priv)) |
| Security List   | [Default Security List for VCN_172.30_PROD_MP](#default-security-list-for-vcn_172.30_prod_mp) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:55:42.997Z |


#### SUB_PROD_PRIV_ASHBURN_01


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [production-mp](#production-mp) |
| Name            | SUB_PROD_PRIV_ASHBURN_01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Private         | True |
| DNS Label       | subprodprivashb |
| CIDR Block      | 172.30.100.0/24 |
| Route Table     | [[RTB_PROD_MP_PRIV](#rtb_prod_mp_priv)](#[rtb_prod_mp_priv](#rtb_prod_mp_priv)) |
| Security List   | [Default Security List for VCN_172.30_PROD_MP](#default-security-list-for-vcn_172.30_prod_mp) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:53:14.539Z |


#### SUB_PROD_PUB_ASHBURN_01


| Property | Value    |
| -------- | -------- |
| Availability Domain | Regional |
| Compartment     | [production-mp](#production-mp) |
| Name            | SUB_PROD_PUB_ASHBURN_01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Private         | False |
| DNS Label       | subprodpubashbu |
| CIDR Block      | 172.30.101.0/24 |
| Route Table     | [[Default Route Table for VCN_172.30_PROD_MP](#default-route-table-for-vcn_172.30_prod_mp)](#[default-route-table-for-vcn_172.30_prod_mp](#default-route-table-for-vcn_172.30_prod_mp)) |
| Security List   | [Default Security List for VCN_172.30_PROD_MP](#default-security-list-for-vcn_172.30_prod_mp) |

Table
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:52:25.850Z |

