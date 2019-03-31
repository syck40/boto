

class VPC:
    def __init__(self, client):
        self._client = client
        """ :type: pyboto3.ec2 """

    def create_vpc(self):
        print("Creating VPC...")
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16'
        )

    def add_name_tag(self, resource_id, resource_name):
        return self._client.create_tags(
            Resources=[resource_id],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': resource_name
                }
            ]
        )

    def create_igw(self):
        print("Create IGW")
        return self._client.create_internet_gateway()

    def attach_igw_to_vpc(self, vpc_id, igw_id):
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId=vpc_id
        )