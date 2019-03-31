from src.ec2.vpc import VPC
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


if __name__ == "__main__":
    main()
