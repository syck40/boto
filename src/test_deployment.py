from src.ec2.vpc import VPC
from src.ec2.ec2 import EC2
from src.client_locator import EC2Client


def main():
    # Create a VPC
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    print("Starting to create VPC")
    vpc_response = vpc.create_vpc()

    print("Finished creating VPC:" + str(vpc_response))
    vpc_name = "Boto3-VPC"
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)
    print("Added" + vpc_name + "to " + vpc_id)

    igw_response = vpc.create_igw()
    igw_id = igw_response["InternetGateway"]["InternetGatewayId"]

    vpc.attach_igw_to_vpc(vpc_id, igw_id)

    public_subnet_cider = '10.0.1.0/24'
    subnet_response = vpc.create_subnet(vpc_id, public_subnet_cider)
    print('Subnet creating for VPC result ' + str(subnet_response))

    public_route_table_response = vpc.create_public_route_table(vpc_id)
    print('Route table creation result is ' + str(public_route_table_response))
    rtb_id = public_route_table_response['RouteTable']['RouteTableId']

    vpc.create_igw_to_public_route_table(rtb_id, igw_id)
    public_subnet_id = subnet_response['Subnet']['SubnetId']

    vpc.associate_subnet_with_route_table(public_subnet_id, rtb_id)

    vpc.allow_auto_assign_ip_addr_for_subnet(public_subnet_id)

    private_subnet_cider = '10.0.2.0/24'
    private_subnet_resp = vpc.create_subnet(vpc_id, private_subnet_cider)
    private_subnet_id = private_subnet_resp['Subnet']['SubnetId']

    vpc.add_name_tag(public_subnet_id, 'Boto3-Public-Subnet')
    vpc.add_name_tag(private_subnet_id, 'Boto3-Private-Subnet')

######## EC2 Instances #########
    ec2 = EC2(ec2_client)

    key_pair_name = 'Boto3-KeyPair'
    key_pair_response = ec2.create_key_pair(key_pair_name)

    print('Created key pair with name ' + str(key_pair_response))


if __name__ == "__main__":
    main()
