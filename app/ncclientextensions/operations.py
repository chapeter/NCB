from ncclient.operations.rpc import RPC


class SendCommand(RPC):
    """
    Create a new class that inherit from ncclient.operations.rpc.RPC
    """
    # Override request method
    def request(self, xml):
        # Send request
        return self._request(xml)
