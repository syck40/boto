

class VPC:
    def __init__(self, client):
        self._client = client
        """ :type: pyboto3.ec2 """

    def create_vpc(self):
        print("Creating VPC...")
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16'
        )