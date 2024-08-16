# Queried Compartment /PerseusTech-SA and Sub-Compartments

# Description

Created 2024-8-13 15:33:30

--------------------------------------



## Compartments

- management
- production-cliente-b
- production-mp
- rtm-fnet
- sandbox-cliente-b
- sandbox-mp


---
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

##### Defined Tags
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

##### Defined Tags
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


### Internet Gateways

#### igw-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | igw-01 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Enabled         | True |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:13:02.942Z |


#### igw-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | igw-01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Enabled         | True |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:28:27.721Z |


### NAT Gateways

#### NGW_MGT_PRIV

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | NGW_MGT_PRIV |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Block Traffic   | False |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-02-02T15:47:28.156Z |


#### natgw-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | natgw-01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Block Traffic   | False |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:28:36.958Z |



### Local Peering Gateways

#### Peering-production-rotas-publicas

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | Peering-production-rotas-publicas |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Peered Virtual Cloud Network | [](#) |
##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T18:03:05.623Z |


#### Peering-01

| XXXXXXProperty | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | Peering-01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:44:15.699Z |


#### peering-management-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | peering-management-01 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:48:24.216Z |


#### teste

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | teste |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-02-02T18:13:53.063Z |


### Route Tables

#### RTB_PROD_MP_PRIV

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | RTB_PROD_MP_PRIV |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-02-02T19:26:12.694Z |


#### rotas-production-privadas-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | rotas-production-privadas-01 |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |



##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:49:49.971Z |


#### Default Route Table for VCN_172.30_PROD_MP

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | Default Route Table for VCN_172.30_PROD_MP |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |



##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:49:48.370Z |


#### RTB-PRIV

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | RTB-PRIV |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-02-02T17:54:41.476Z |


#### rotas-privadas-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | rotas-privadas-01 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:12:37.171Z |


#### Default Route Table for VCN_172.29_MANAGEMENT

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | Default Route Table for VCN_172.29_MANAGEMENT |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:48:45.636Z |


### Security Lists

#### Default Security List for VCN_172.29_MANAGEMENT

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | Default Security List for VCN_172.29_MANAGEMENT |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |



#### Egress Rules
| Protocol | Stateless |Destination| Details | Description |
| -------- | --------- | ----------- | ----------- | ----------- |
| All | False |0.0.0.0/0||  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:48:45.636Z |


#### Default Security List for VCN_172.30_PROD_MP

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | Default Security List for VCN_172.30_PROD_MP |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Egress Rules
| Protocol | Stateless |Destination| Details | Description |
| -------- | --------- | ----------- | ----------- | ----------- |
| All | False |0.0.0.0/0||  |
| TCP | False |172.30.100.0/24|Source - / Destination 10256-10256|  |
| TCP | False |172.30.100.0/24|Source - / Destination 30896-30896|  |
| TCP | False |172.30.100.0/24|Source - / Destination 30528-30528|  |
| TCP | False |172.30.100.0/24|Source - / Destination 30205-30205|  |
| TCP | False |172.30.100.0/24|Source - / Destination 30600-30600|  |
| TCP | False |172.30.100.0/24|Source - / Destination 31023-31023|  |
| TCP | False |172.30.100.0/24|Source - / Destination 31107-31107|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31288-31288|  |
| TCP | False |172.30.112.0/20|Source - / Destination 10256-10256|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31156-31156|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32590-32590|  |
| TCP | False |172.30.112.0/20|Source - / Destination 30034-30034|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31175-31175|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31312-31312|  |
| TCP | False |172.30.112.0/20|Source - / Destination 30142-30142|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31051-31051|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32069-32069|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31043-31043|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32407-32407|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32224-32224|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31902-31902|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32137-32137|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32021-32021|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31989-31989|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31819-31819|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32416-32416|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31242-31242|  |
| TCP | False |172.30.112.0/20|Source - / Destination 30230-30230|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31781-31781|  |
| TCP | False |172.30.112.0/20|Source - / Destination 30113-30113|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32097-32097|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31934-31934|  |
| TCP | False |172.30.112.0/20|Source - / Destination 32143-32143|  |
| TCP | False |172.30.112.0/20|Source - / Destination 30244-30244|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31419-31419|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31080-31080|  |
| TCP | False |172.30.112.0/20|Source - / Destination 31816-31816|  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T14:49:48.370Z |


### Network Security Groups

#### unifi_externo_sg

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | unifi_externo_sg |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | TCP | False |8.243.39.190/32|Source - / Destination 443-443| Link Cirion |
| Ingress | TCP | False |187.115.151.178/32|Source - / Destination 443-443| Link Vivo |
| Egress | TCP | False |8.243.39.190/32|Source - / Destination 80-80|  |
| Egress | TCP | False |187.115.151.178/32|Source - / Destination 80-80|  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-15T15:21:47.480Z |


#### prttg_sg

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | prttg_sg |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | ICMP | False |0.0.0.0/0||  |
| Ingress | TCP | False |172.16.0.0/12|Source - / Destination 3389-3389|  |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 80-80|  |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 443-443|  |
| Egress | All | False |0.0.0.0/0||  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-19T17:09:06.604Z |


#### jump_sg

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | jump_sg |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Egress | All | False |0.0.0.0/0||  |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 22-22|  |
| Ingress | ICMP | False |0.0.0.0/0||  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:11:00.410Z |


#### LOGSTASH-SIEM

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | LOGSTASH-SIEM |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 5000-5000|  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-26T13:56:13.258Z |


#### RabbitMQ

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | RabbitMQ |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | All | False |0.0.0.0/0|| LIBERA TUDO |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-15T17:19:43.316Z |


#### ELASTIC

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | ELASTIC |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 9200-9200| LIBERA ELASTIC |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 9300-9300| LIBERA ELASTIC |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 5601-5601|  |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 443-443| LIBERA HTTPS |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T19:09:34.138Z |


#### OKE

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | OKE |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | All | False |0.0.0.0/0|| Permite Tudo |
| Egress | All | False |0.0.0.0/0||  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-11T18:06:19.954Z |


#### MONITORAMENTO

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | MONITORAMENTO |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |



##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-24T12:13:52.347Z |


#### HTTP_HTTPS

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | HTTP_HTTPS |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 80-80| HTTP |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 443-443| HTTPS |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-23T21:45:31.971Z |


#### JD_TCP_COMP_WINDOWS

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | JD_TCP_COMP_WINDOWS |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 139-139| COMPARTILHAMENTO_WINDOWS |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 445-445| COMPARTILHAMENTO_WINDOWS |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-22T18:49:15.958Z |


#### jump-sg

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | jump-sg |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |

#### Security Rules
| Direction | Protocol | Stateless | Source/Destination | Details | Description |
| --------- | -------- | --------- | ----------- | ----------- | ----------- |
| Egress | All | False |0.0.0.0/0||  |
| Ingress | TCP | False |0.0.0.0/0|Source - / Destination 22-22|  |
| Ingress | ICMP | False |0.0.0.0/0||  |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:28:14.040Z |


### DRG Attachments

#### DRG_VCN_172_29

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | DRG_VCN_172_29 |
| Virtual Cloud Network | [VCN_172.29_MANAGEMENT](#vcn_172.29_management) |
| Dynamic Routing Gateway | [DRG-01](#drg-01) |
| Dynamic Route Table | [Autogenerated Drg Route Table for VCN attachments](#autogenerated-drg-route-table-for-vcn-attachments) |
| Route Table     | [](#) |

#### DRG_VCN_172_30_PRODUCTION

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | DRG_VCN_172_30_PRODUCTION |
| Virtual Cloud Network | [VCN_172.30_PROD_MP](#vcn_172.30_prod_mp) |
| Dynamic Routing Gateway | [DRG-01](#drg-01) |
| Dynamic Route Table | [Autogenerated Drg Route Table for VCN attachments](#autogenerated-drg-route-table-for-vcn-attachments) |
| Route Table     | [](#) |

### Dynamic Routing Gateways

#### DRG-01

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | DRG-01 |

#### Route Distributions
| Property | Value    |
| -------- | -------- |
| Type            | EXPORT |
| Name            | Default Export Route Distribution for DRG: DRG-01 |
##### Statements
| Action | Type / Attachment | Priority |
| ------ | ----------------- | -------- |
| ACCEPT          |                 | 1               |
| Property | Value    |
| -------- | -------- |
| Type            | IMPORT |
| Name            | Autogenerated Import Route Distribution for ALL routes |
##### Statements
| Action | Type / Attachment | Priority |
| ------ | ----------------- | -------- |
| ACCEPT          |                 | 1               |
| Property | Value    |
| -------- | -------- |
| Type            | IMPORT |
| Name            | Autogenerated Import Route Distribution for VCN Routes |
##### Statements
| Action | Type / Attachment | Priority |
| ------ | ----------------- | -------- |
| ACCEPT          | VCN             | 1               |
| ACCEPT          |                 | 2               |

#### Route Tables
| Property | Value    |
| -------- | -------- |
| Name            | Autogenerated Drg Route Table for VCN attachments |
| Import Route Distribution | [Autogenerated Import Route Distribution for ALL routes](#autogenerated-import-route-distribution-for-all-routes) |
| ECMP Enabled    | False |

#### RPC_DRG_ASH_TO_DRG_VNH

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | RPC_DRG_ASH_TO_DRG_VNH |
|                 |  |
| Dynamic Routing Gateway | [DRG-01](#drg-01) |
| Peer Id         | ocid1.remotepeeringconnection.oc1.sa-vinhedo-1.aaaaaaaak4ckpuyg4qkwfjxzl7zu3s3c5xsy3kllfrzfdxcao725v4aurjlq |
| Peer Region     | sa-vinhedo-1 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-04-04T21:55:19.243Z |


#### RPC-US-MGT-TO-SP-FNET

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | RPC-US-MGT-TO-SP-FNET |
|                 |  |
| Dynamic Routing Gateway | [DRG-01](#drg-01) |
| Peer Id         | ocid1.remotepeeringconnection.oc1.sa-saopaulo-1.aaaaaaaa4mds6y3nn2mv2rxhigiajjrrrxxoyr7mznkkzuggfwwukupk6aaq |
| Peer Region     | sa-saopaulo-1 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-03-08T23:11:26.176Z |


## Databases



### MySQL Database Systems

#### prd-grdb

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-grdb |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Hostname        | prd-grdb |
| Size (Gb)       | 50 |
| Version         | 8.4.0 |
| Shape           | MySQL.4 |
| Description     | Restored from backup &#34;minhaconta-prod - Backup - Thu, Jul 18, 2024, 22:49:51 UTC&#34; of DB system &#34;minhaconta-prod&#34;.

Backup ID: &#34;ocid1.mysqlbackup.oc1.iad.aaaaaaaaozaopd6bvztb7ie2pstkxeqat2qpudciuz27sive7efs5vwrsrkq&#34; |
| Port            | 3306 |
| Port X          | 33060 |

##### Freeform Tags
| Key      | Value    |
| -------- | -------- |
| Template | Production |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/eduardo.balthar@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-11T19:11:12.602Z |


#### minhaconta-prod

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | minhaconta-prod |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Hostname        | okitmysql264 |
| Size (Gb)       | 50 |
| Version         | 8.4.0 |
| Shape           | MySQL.16 |
| Description     | Minha Conta Produção OCI |
| Port            | 3306 |
| Port X          | 33060 |

##### Freeform Tags
| Key      | Value    |
| -------- | -------- |
| Template | Production |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/eduardo.balthar@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-11T19:11:12.602Z |


#### minhaconta-sandbox

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [sandbox-mp](#sandbox-mp) |
| Name            | minhaconta-sandbox |
| Subnet          | [](#) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Hostname        | minhaconta-sandbox |
| Size (Gb)       | 50 |
| Version         | 8.4.0 |
| Shape           | MySQL.8 |
| Description     | MySQL 8 |
| Port            | 3306 |
| Port X          | 33060 |

##### Freeform Tags
| Key      | Value    |
| -------- | -------- |
| Template | Development or testing |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/eduardo.balthar@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-13T18:46:00.337Z |


## Infrastructure

### Instances

#### LIFT-MIGRACAO-MDS

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | LIFT-MIGRACAO-MDS |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Oracle Linux |
| Operating System Version | 7.9 |
##### Cloud Init
```bash
#!/bin/bash
sudo useradd m2c
echo "m2c:welcome1" | chpasswd
echo "m2c  ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/assis.prestes@oracle.com |
| Oracle-Tags| CreatedOn | 2024-07-04T15:12:57.417Z |


#### OCI-BRITECHP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCI-BRITECHP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-18T17:28:02.543Z |


#### OCICFIP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCICFIP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T18:35:42.414Z |


#### OCICRKP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCICRKP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_02](#sub_prod_priv_ashburn_02)](#[sub_prod_priv_ashburn_02](#sub_prod_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-12T13:19:28.449Z |


#### OCIJDP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIJDP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T18:05:57.750Z |


#### OCIJUMPP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIJUMPP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-18T17:25:37.541Z |


#### OCIMETABASEP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIMETABASEP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard.E5.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-07-17T14:36:27.059Z |


#### OCISIEMP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCISIEMP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-24T19:06:29.271Z |


#### OCITEMAP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCITEMAP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-27T17:17:38.879Z |


#### OCIZAPP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIZAPP01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T17:54:28.637Z |


#### jump-production

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | jump-production |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:27:21.459Z |


#### oci-elastic-p01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | oci-elastic-p01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 20.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T18:14:56.048Z |


#### oci-rabbitmq-p01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | oci-rabbitmq-p01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T13:19:16.195Z |


#### prd-sql-terc-01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terc-01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard3.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard with SQL Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-14T14:24:33.762Z |


#### prd-sql-terc-02

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terc-02 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard3.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard with SQL Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-14T14:26:11.029Z |


#### prd-sql-terc-03

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terc-03 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard3.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard with SQL Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-04T16:38:54.096Z |


#### OCIADP02

| Property | Value    |
| -------- | -------- |
| Availability Domain | 2 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIADP02 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T19:31:39.932Z |


#### oci-rabbitmq-p02

| Property | Value    |
| -------- | -------- |
| Availability Domain | 2 |
| Compartment     | [production-mp](#production-mp) |
| Name            | oci-rabbitmq-p02 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_02](#sub_prod_priv_ashburn_02)](#[sub_prod_priv_ashburn_02](#sub_prod_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T13:54:23.919Z |


#### oci-rabbitmq-p03

| Property | Value    |
| -------- | -------- |
| Availability Domain | 3 |
| Compartment     | [production-mp](#production-mp) |
| Name            | oci-rabbitmq-p03 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_03](#sub_prod_priv_ashburn_03)](#[sub_prod_priv_ashburn_03](#sub_prod_priv_ashburn_03)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T15:19:29.734Z |


#### OCIADP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIADP01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_01](#sub_mgt_priv_ashburn_01)](#[sub_mgt_priv_ashburn_01](#sub_mgt_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-03-18T19:14:01.486Z |


#### OCIBLACKBOX-EXPORTER

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIBLACKBOX-EXPORTER |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_02](#sub_mgt_priv_ashburn_02)](#[sub_mgt_priv_ashburn_02](#sub_mgt_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 20.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-03-27T20:43:37.581Z |


#### OCIELASTICP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIELASTICP01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_02](#sub_mgt_priv_ashburn_02)](#[sub_mgt_priv_ashburn_02](#sub_mgt_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-21T13:34:40.253Z |


#### OCIGRAFANAP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIGRAFANAP01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_02](#sub_mgt_priv_ashburn_02)](#[sub_mgt_priv_ashburn_02](#sub_mgt_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-20T14:41:38.725Z |


#### OCIINFLUXDB01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIINFLUXDB01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_02](#sub_mgt_priv_ashburn_02)](#[sub_mgt_priv_ashburn_02](#sub_mgt_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 20.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-04-22T19:01:51.902Z |


#### OCIPROMETHEUSP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIPROMETHEUSP01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_02](#sub_mgt_priv_ashburn_02)](#[sub_mgt_priv_ashburn_02](#sub_mgt_priv_ashburn_02)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 20.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-03-27T18:23:19.648Z |


#### OCIPRTGP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIPRTGP01 |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_01](#sub_mgt_priv_ashburn_01)](#[sub_mgt_priv_ashburn_01](#sub_mgt_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2022 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-19T17:07:10.670Z |


#### OCIWIFIP01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIWIFIP01 |
| Subnet          | [[SUB_MGT_PUB_ASHBURN_01](#sub_mgt_pub_ashburn_01)](#[sub_mgt_pub_ashburn_01](#sub_mgt_pub_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Windows |
| Operating System Version | Server 2019 Standard |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-08T17:38:29.238Z |


#### OPENNVPN

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OPENNVPN |
| Subnet          | [[SUB_MGT_PUB_ASHBURN_01](#sub_mgt_pub_ashburn_01)](#[sub_mgt_pub_ashburn_01](#sub_mgt_pub_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-2 |
| Shape           | VM.Standard2.1 |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-01-29T18:46:04.177Z |


#### TESTE-VPN-BRITECH

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | TESTE-VPN-BRITECH |
| Subnet          | [[SUB_MGT_PRIV_ASHBURN_01](#sub_mgt_priv_ashburn_01)](#[sub_mgt_priv_ashburn_01](#sub_mgt_priv_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-1 |
| Shape           | VM.Standard.A1.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 20.04 |

##### Freeform Tags
| Key      | Value    |
| -------- | -------- |
| start | 0 8 * * * |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2023-11-23T20:03:07.562Z |


#### jump-management

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | jump-management |
| Subnet          | [[SUB_MGT_PUB_ASHBURN_01](#sub_mgt_pub_ashburn_01)](#[sub_mgt_pub_ashburn_01](#sub_mgt_pub_ashburn_01)) |
| Fault Domain    | FAULT-DOMAIN-3 |
| Shape           | VM.Standard.E4.Flex |
| Operating System | Canonical Ubuntu |
| Operating System Version | 22.04 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:08:02.130Z |


### Load Balancers

#### 86f8e0c6-b63d-4739-afe0-dd9ec9ba21ca

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 86f8e0c6-b63d-4739-afe0-dd9ec9ba21ca |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-11T19:59:31.961Z |


#### 9b64ea32-0ee2-491c-8e4d-c60169ea7832

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 9b64ea32-0ee2-491c-8e4d-c60169ea7832 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-11T20:22:55.328Z |


#### 28ade714-0eea-42cf-802c-c9812975ae2e

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 28ade714-0eea-42cf-802c-c9812975ae2e |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-11T20:23:26.703Z |


#### 13a87a1d-71ce-413c-95ab-3a90619f981a

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 13a87a1d-71ce-413c-95ab-3a90619f981a |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-11T20:24:56.920Z |


#### b32b0cb7-9860-4f76-9090-e0df9be03c54

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | b32b0cb7-9860-4f76-9090-e0df9be03c54 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-11T20:25:28.255Z |


#### 36c231d6-dd95-420c-82f4-c5a82b3d5f3a

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 36c231d6-dd95-420c-82f4-c5a82b3d5f3a |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | False |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-12T13:39:16.605Z |


#### 9e7cd0ce-168d-4b0b-acc0-75519339d92f

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 9e7cd0ce-168d-4b0b-acc0-75519339d92f |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | False |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-13T21:21:08.933Z |


#### 82fedac5-43d9-472d-82bd-7d2b53942ef4

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 82fedac5-43d9-472d-82bd-7d2b53942ef4 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-15T13:54:43.037Z |


#### 747432dd-6597-4df6-a43f-ef519bd84780

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 747432dd-6597-4df6-a43f-ef519bd84780 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-15T13:56:09.022Z |


#### 643c9c5c-b4fc-4b10-a573-bb4d6995eb0f

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 643c9c5c-b4fc-4b10-a573-bb4d6995eb0f |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-15T14:00:51.962Z |


#### 7efde407-268d-4b00-9c2d-6f7a04f32e83

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 7efde407-268d-4b00-9c2d-6f7a04f32e83 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-15T14:01:23.715Z |


#### 4ce18e9e-2588-424e-abdf-a95d8735d5c3

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 4ce18e9e-2588-424e-abdf-a95d8735d5c3 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-15T14:10:06.956Z |


#### lb_rabbitmq_p01

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | lb_rabbitmq_p01 |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_04](#sub_prod_priv_ashburn_04)](#[sub_prod_priv_ashburn_04](#sub_prod_priv_ashburn_04)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-15T18:48:46.350Z |


#### f25dc577-b013-4314-80d8-015c1bf41806

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | f25dc577-b013-4314-80d8-015c1bf41806 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T02:11:42.154Z |


#### eea3dc70-bf70-43e1-9d2a-82e6cd742326

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | eea3dc70-bf70-43e1-9d2a-82e6cd742326 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T02:12:13.441Z |


#### e66d1978-2a0f-40ff-bf3e-fa0c81405a0e

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | e66d1978-2a0f-40ff-bf3e-fa0c81405a0e |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T02:12:39.735Z |


#### 542e352d-fdfc-4fc3-bf4c-1a31eda1c4e3

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 542e352d-fdfc-4fc3-bf4c-1a31eda1c4e3 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T15:54:07.701Z |


#### 23892f98-de45-4a02-a22e-e4523048b5e3

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 23892f98-de45-4a02-a22e-e4523048b5e3 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T15:54:33.975Z |


#### dacecf9a-a593-404d-874a-6c6a441defd9

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | dacecf9a-a593-404d-874a-6c6a441defd9 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T15:55:00.241Z |


#### 9cfe2569-c0d0-457a-8ff2-4d5b853f617b

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 9cfe2569-c0d0-457a-8ff2-4d5b853f617b |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T20:03:23.080Z |


#### a9aeb716-91df-4659-93a3-ffb50fbf66f3

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | a9aeb716-91df-4659-93a3-ffb50fbf66f3 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-16T21:49:28.690Z |


#### 3a724d3e-7184-4bdd-90c2-e2d94fc8dbd4

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 3a724d3e-7184-4bdd-90c2-e2d94fc8dbd4 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-26T20:08:31.131Z |


#### 78084741-9560-4983-acaa-c3b5299012c1

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 78084741-9560-4983-acaa-c3b5299012c1 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | flexible |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T17:57:56.178Z |


#### 9d706fe5-a7c7-460d-a93a-62d5eb5545db

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 9d706fe5-a7c7-460d-a93a-62d5eb5545db |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T04:16:35.343Z |


#### b41f51ec-0331-4095-92a8-1198c4a06f85

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | b41f51ec-0331-4095-92a8-1198c4a06f85 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T05:10:41.223Z |


#### 0a78e1f7-d4bf-4805-a512-bb34f04016fc

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 0a78e1f7-d4bf-4805-a512-bb34f04016fc |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T06:39:11.426Z |


#### 177da5ee-e8a9-4b63-b202-c9a4d3b70cad

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 177da5ee-e8a9-4b63-b202-c9a4d3b70cad |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T06:39:38.175Z |


#### b9923eaa-88e5-4c65-8c91-748c4d633ca7

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | b9923eaa-88e5-4c65-8c91-748c4d633ca7 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T06:40:14.632Z |


#### eea8be76-be32-42a0-bfe1-c919f50f04b9

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | eea8be76-be32-42a0-bfe1-c919f50f04b9 |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T07:04:50.738Z |


#### 837cbcd8-90fd-4226-82c5-afaad14522bb

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | 837cbcd8-90fd-4226-82c5-afaad14522bb |
| Subnet          | [[SUB_PROD_PUB_ASHBURN_01](#sub_prod_pub_ashburn_01)](#[sub_prod_pub_ashburn_01](#sub_prod_pub_ashburn_01)) |
| Shape           | 100Mbps |
| Private         | True |
| Protocol        |  |
| Port            |  |
| Policy          |  |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T07:21:41.406Z |



## Storage

### Block Storage Volumes

#### jump-storage

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | jump-storage |
| Size (Gbs)      | 1536 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/cliff.bernaldo@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-29T16:03:42.454Z |


#### ocicfip01-d

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | ocicfip01-d |
| Size (Gbs)      | 60 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-04-29T17:26:41.586Z |


#### prd-sql-terceiros-01-dados

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-01-dados |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 20 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-13T15:00:30.637Z |


#### prd-sql-terceiros-01-logs

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-01-logs |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 20 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-13T15:01:14.101Z |


#### prd-sql-terceiros-01-backup

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-01-backup |
| Size (Gbs)      | 2048 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-13T15:01:31.074Z |


#### prd-sql-terceiros-02-dados

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-02-dados |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-14T14:28:27.625Z |


#### prd-sql-terceiros-02-logs

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-02-logs |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-14T14:28:46.346Z |


#### prd-sql-terceiros-02-backup

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-02-backup |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-05-14T14:29:01.361Z |


#### OCIZAPP01-DADOS

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIZAPP01-DADOS |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T17:46:58.820Z |


#### OCIJDP01-DADOS

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCIJDP01-DADOS |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T17:50:24.937Z |


#### OCICFIP01-DADOS

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCICFIP01-DADOS |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-05-17T17:55:37.666Z |


#### prd-temp-terc-dados

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-temp-terc-dados |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-12T14:29:52.074Z |


#### prd-temp-terc-logs

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-temp-terc-logs |
| Size (Gbs)      | 512 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-12T14:30:04.398Z |


#### prd-temp-terc-bck

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-temp-terc-bck |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-12T20:11:28.546Z |


#### oci-elastic-p01_var

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | oci-elastic-p01_var |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-14T18:25:19.948Z |


#### ocijumpp01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | ocijumpp01 |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-18T17:34:21.832Z |


#### britech-data

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | britech-data |
| Size (Gbs)      | 200 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/douglas.ribeiro@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-06-18T17:42:31.376Z |


#### ocisiemp01data

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | ocisiemp01data |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-24T18:54:40.897Z |


#### csi-781d2ffc-c053-4fcb-8c5a-ef62e6047cfc

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-781d2ffc-c053-4fcb-8c5a-ef62e6047cfc |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-28T18:39:43.767Z |


#### csi-3d3032f8-1090-4ccc-9038-ddb37b0a3d2c

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-3d3032f8-1090-4ccc-9038-ddb37b0a3d2c |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-28T18:39:43.773Z |


#### csi-ee2ba0f3-c5c6-41c6-a761-acdc746b520c

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-ee2ba0f3-c5c6-41c6-a761-acdc746b520c |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-28T18:39:43.823Z |


#### csi-f7f6c6f9-bece-4d18-b069-832a3344b712

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-f7f6c6f9-bece-4d18-b069-832a3344b712 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-28T18:39:43.841Z |


#### csi-348cfdd3-9dfa-464d-a130-0cd23358d7f7

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-348cfdd3-9dfa-464d-a130-0cd23358d7f7 |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-28T18:39:43.944Z |


#### csi-f7c00706-0c29-4e1a-9e2c-fad14a14e434

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-f7c00706-0c29-4e1a-9e2c-fad14a14e434 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:14:45.237Z |


#### csi-8e9023de-a992-44eb-9bc4-544fa896f68f

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-8e9023de-a992-44eb-9bc4-544fa896f68f |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:14:45.311Z |


#### csi-183ac959-4dd4-4ddc-a7ab-c9296bb69439

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-183ac959-4dd4-4ddc-a7ab-c9296bb69439 |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:14:45.342Z |


#### csi-61278c00-d2ea-4835-963d-81c8468841ab

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-61278c00-d2ea-4835-963d-81c8468841ab |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:14:45.381Z |


#### csi-c0ebb6ac-5a78-436a-968f-3fd6f5b43299

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-c0ebb6ac-5a78-436a-968f-3fd6f5b43299 |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:38:30.194Z |


#### csi-6879ca3e-05e9-4078-8cfe-d02f9e2f0566

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-6879ca3e-05e9-4078-8cfe-d02f9e2f0566 |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:38:30.326Z |


#### csi-5c406f5d-2742-4dc1-b44b-dac0b3b597fd

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-5c406f5d-2742-4dc1-b44b-dac0b3b597fd |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:38:30.347Z |


#### csi-7be1bfec-f89f-4053-ac38-cb80a9d1baa0

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-7be1bfec-f89f-4053-ac38-cb80a9d1baa0 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:38:30.400Z |


#### csi-fbf99edf-46f0-4a22-918e-07bde0656fff

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-fbf99edf-46f0-4a22-918e-07bde0656fff |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-01T18:38:30.509Z |


#### csi-6893a850-7e80-4dd9-94cb-6d15e64e4a4b

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-6893a850-7e80-4dd9-94cb-6d15e64e4a4b |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T19:27:16.147Z |


#### csi-5f19f43f-51a3-4a67-a282-5b5f812961be

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-5f19f43f-51a3-4a67-a282-5b5f812961be |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T19:27:16.201Z |


#### csi-cbc5628f-f439-43ad-aa7a-e7a05fbcdf72

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-cbc5628f-f439-43ad-aa7a-e7a05fbcdf72 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T19:27:16.234Z |


#### csi-e86c29e7-c684-4cff-8d1b-4bc9407bf987

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-e86c29e7-c684-4cff-8d1b-4bc9407bf987 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T19:42:40.307Z |


#### csi-e27b854d-4232-4581-a72b-b62f376450a0

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-e27b854d-4232-4581-a72b-b62f376450a0 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T20:13:56.957Z |


#### csi-9853d06f-b947-458f-88fd-c97de05eb784

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-9853d06f-b947-458f-88fd-c97de05eb784 |
| Size (Gbs)      | 100 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T20:13:57.094Z |


#### csi-9da82f16-b2e8-482f-8677-2d06861c4be3

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-9da82f16-b2e8-482f-8677-2d06861c4be3 |
| Size (Gbs)      | 50 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-02T20:24:38.197Z |


#### prd-sql-terceiros-03-logs

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-03-logs |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 20 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-04T16:59:26.774Z |


#### prd-sql-terceiros-03-dados

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-03-dados |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 20 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-04T17:00:46.058Z |


#### prd-sql-terceiros-03-backup

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | prd-sql-terceiros-03-backup |
| Size (Gbs)      | 2048 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-04T17:01:24.154Z |


#### OCICRKP01-DADOS

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | OCICRKP01-DADOS |
| Size (Gbs)      | 180 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/anderson.cardoso@nikos.com.br |
| Oracle-Tags| CreatedOn | 2024-07-12T13:20:30.205Z |


#### OCIELASTICP01-01

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [management](#management) |
| Name            | OCIELASTICP01-01 |
| Size (Gbs)      | 1024 |
| Backup Policy   |  |
| VPUs/Gb         | 10 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-02-21T13:42:08.344Z |


### Object Storage Buckets

#### db-migra

| Property | Value    |
| -------- | -------- |
| Compartment     | [production-mp](#production-mp) |
| Name            | db-migra |
| Namespace       | idnmdpddtgsm |
| Storage Tier    | Standard |
| Public Access Type | NoPublicAccess |

#### Infra-publico

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | Infra-publico |
| Namespace       | idnmdpddtgsm |
| Storage Tier    | Standard |
| Public Access Type | NoPublicAccess |

#### oci-logs._flowlogs.ocid1.compartment.oc1..aaaaaaaakodr4shuiorwg4lcgkqhu32h6oe33ofruoo6q4xdwg4e27jqdd5q

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | oci-logs._flowlogs.ocid1.compartment.oc1..aaaaaaaakodr4shuiorwg4lcgkqhu32h6oe33ofruoo6q4xdwg4e27jqdd5q |
| Namespace       | idnmdpddtgsm |
| Storage Tier    | Standard |
| Public Access Type | NoPublicAccess |


### File Systems

#### csi-fss-cf507124-573b-4e35-800f-94e312a28468

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-fss-cf507124-573b-4e35-800f-94e312a28468 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-07-13T02:46:09.561Z |


#### csi-fss-ddd08c08-d7be-49d9-bd88-546bf57b41a1

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | csi-fss-ddd08c08-d7be-49d9-bd88-546bf57b41a1 |


##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | ocid1.cluster.oc1.iad.aaaaaaaalbo7dd3gt3foojqnqdjwrkr23yj5mswwjhc2hjanwchqmgmifokq |
| Oracle-Tags| CreatedOn | 2024-06-14T22:50:53.938Z |


#### nfs-efs-mc-shared-prod

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | nfs-efs-mc-shared-prod |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-14T22:41:27.783Z |


### Mount Targets

#### MountTarget-efs-mc-shared-prod

| Property | Value    |
| -------- | -------- |
| Availability Domain | 1 |
| Compartment     | [production-mp](#production-mp) |
| Name            | MountTarget-efs-mc-shared-prod |
| Subnet          | [[SUB_PROD_PRIV_ASHBURN_01](#sub_prod_priv_ashburn_01)](#[sub_prod_priv_ashburn_01](#sub_prod_priv_ashburn_01)) |
| Hostname        |  |
| IP Address      |  |
| Max FS Stat Bytes |  |
| Max FS Stat Files |  |
##### Exports
| File System | Path | Source | Access | GID | UID | Squash | Privileged Access |
| ----------- | ---- | ------ | ------ | --- | --- | ------ | ----------------- |
| [csi-fss-cf507124-573b-4e35-800f-94e312a28468](#csi-fss-cf507124-573b-4e35-800f-94e312a28468) | /nfs-efs-mc-shared-prod-02 |  | Read Only | 65534 | 65534 | Root | True |
| [nfs-efs-mc-shared-prod](#nfs-efs-mc-shared-prod) | /nfs-efs-mc-shared-prod |  | Read Only | 65534 | 65534 | Root | True |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/marcelo.quintas@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-06-14T22:41:30.178Z |


## External

### Customer Premise Equipment

#### AWS_PROD_NILCO_3.220.246.120

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | AWS_PROD_NILCO_3.220.246.120 |
| Customer Router IP | 3.220.246.120 |
| Shape           | 0c14a129-ce70-43f3-bf07-e980a6784ae8 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T17:15:14.790Z |


#### CPE-INOA

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | CPE-INOA |
| Customer Router IP | 35.198.4.82 |
| Shape           | f9015b65-7d14-4832-a44a-cb4002f38597 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/luiz.paiva@orama.com.br |
| Oracle-Tags| CreatedOn | 2024-01-30T18:14:57.453Z |


#### AWS_PROD_NILCO_GW_54.84.88.121

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | AWS_PROD_NILCO_GW_54.84.88.121 |
| Customer Router IP | 54.84.88.121 |
| Shape           | 0c14a129-ce70-43f3-bf07-e980a6784ae8 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-18T15:21:04.043Z |


#### AWS_PROD_NILCO_34.232.218.32

| Property | Value    |
| -------- | -------- |
| Compartment     | [management](#management) |
| Name            | AWS_PROD_NILCO_34.232.218.32 |
| Customer Router IP | 34.232.218.32 |
| Shape           | 0c14a129-ce70-43f3-bf07-e980a6784ae8 |

##### Defined Tags
| Namespace | Key      | Value    |
| --------- | -------- | -------- |
| Oracle-Tags| CreatedBy | default/suporte@perseustech.dev |
| Oracle-Tags| CreatedOn | 2024-01-19T00:15:42.290Z |









