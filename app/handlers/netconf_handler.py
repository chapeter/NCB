import traceback

from ncclient import manager
from base_handler import BaseHandler
from app.ncclientextensions.operations import SendCommand
from lxml import etree
from base64 import b64encode


class NetConfHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.clientManager = None

    def get_capabilities(self, object_response, form_values):
        try:
            self.clientManager = manager.connect(host=form_values['server_ip'],
                                                 port=int(form_values['server_port']),
                                                 username=form_values['server_username'],
                                                 password=form_values['server_password'],
                                                 hostkey_verify=False,
                                                 device_params={},
                                                 look_for_keys=False, allow_agent=False)

            object_response.script("connected();")
            for cap in self.clientManager.server_capabilities:
                object_response.script("add_capability('" + cap + "');")
        except Exception as e:
            # Update the GUI
            object_response.script("create_notification('Something went wrong', '" + str(e).replace("'", "").
                                   replace('"', '').replace("\n", "")[0:100] + "', 'danger', 0);")
            object_response.script("setProgressBar(operations.response);")
            print traceback.print_exc()
        finally:
            if self.clientManager is not None:
                if self.clientManager.connected:
                    self.clientManager.close_session()

    def send_command(self, object_response, form_values):
        try:
            self.clientManager = manager.connect(host=form_values['server_ip'],
                                                 port=int(form_values['server_port']),
                                                 username=form_values['server_username'],
                                                 password=form_values['server_password'],
                                                 hostkey_verify=False,
                                                 device_params={},
                                                 look_for_keys=False, allow_agent=False)

            # Create a new SendCommand instance
            rpc_call = SendCommand(self.clientManager._session,
                                   device_handler=self.clientManager._device_handler,
                                   async=self.clientManager._async_mode,
                                   timeout=self.clientManager._timeout,
                                   raise_mode=self.clientManager._raise_mode)

            # Increase the default timeout
            rpc_call.timeout = 100

            # Do the request and save the response into a variable
            response = rpc_call.request(xml=etree.fromstring(form_values['xml_command']))

            # Update the GUI
            object_response.script("show_xml_response('" + b64encode(str(response)) + "');")

        except Exception as e:
            # Update the GUI
            object_response.script("show_xml_response('" + b64encode(str(e)) + "');")
            print traceback.print_exc()
        finally:
            if self.clientManager is not None:
                if self.clientManager.connected:
                    self.clientManager.close_session()
