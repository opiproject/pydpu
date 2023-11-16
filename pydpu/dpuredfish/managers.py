import logging
import os.path

import redfish


class Managers:
    def __init__(self, host, user, password, **kwargs):
        """
        Create a new connection to DPU via Redfish.
        Due to timeout restrictions, every command will start its own session
        and tear it down once it completes.
        """
        self.logger = logging.getLogger("dpuredfish")
        self._host = host
        self._user = user
        self._password = password
        self._bmc_name = None
        self.logger.info("Connecting to %s", host)
        self._session = redfish.redfish_client(
            base_url=self._host,
            username=self._user,
            password=self._password,
            cafile=None,
            capath=None,
            max_retry=3,
            timeout=120,
            **kwargs
        )

    @property
    def bmc_name(self):
        self.logger.info("Getting System ID...")
        if self._bmc_name is not None:
            return self._bmc_name
        managers = self._session.get("/redfish/v1/Managers").obj.Members
        response = self._session.get(managers[0]["@odata.id"])
        self.logger.debug("Getting System ID ({})...".format(response.obj.Id))
        self._bmc_name = os.path.basename(managers[0]["@odata.id"])
        # TODO: should use response.obj.Id, but doesn't work on all devices (bug)
        # self._bmc_name = re.split(r"\d$", response.obj.Id)[0]
        return self._bmc_name

    def get_bmc_datetime(self):
        self.logger.info("Getting BMC time...")
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get("/redfish/v1/Managers/{}".format(self.bmc_name))
        self.logger.debug(response.text)
        self._session.logout()
        return response.dict.get("DateTime")

    def set_bmc_datetime(self, datetime_string):
        self.logger.info("Setting BMC time to {}".format(datetime_string))
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.patch(
            "/redfish/v1/Managers/{}".format(self.bmc_name),
            body={"DateTime": datetime_string},
        )
        self.logger.debug(response.text)
        self._session.logout()

    def get_bmc_networks(self):
        self.logger.info("Getting EthernetInterfaces")
        url = "/redfish/v1/Managers/{}/EthernetInterfaces?$expand=.($levels=1)".format(
            self.bmc_name
        )
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get(url)
        self.logger.debug(response.text)
        self._session.logout()
        for item in response.obj.Members:
            yield item

    def get_event_log(self, log_type="Journal"):
        self.logger.info("Getting BMC logs of type {}...".format(log_type))
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get(
            "/redfish/v1/Managers/{}/LogServices/{}/Entries".format(
                self.bmc_name, log_type
            )
        )
        self._session.logout()
        for entry in response.dict.get("Members"):
            yield entry

    def factory_reset(self):
        """
        Reset the BMC to default settings.
        """
        self.logger.info("Reset BMC to defaults")
        url = "/redfish/v1/Managers/{}/Actions/Manager.ResetToDefaults".format(
            self.bmc_name
        )
        body = {"ResetType": "ResetAll"}
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.post(url, body=body)
        self.logger.debug(response.text)
        self._session.logout()

    def reset_bmc(self, reset_type="ForceRestart"):
        """
        Restart the BMC.
        :param str reset_type: The type of reset to perform. Default is "ForceRestart".
                                Valid options are:
                               ForceOff, GracefulShutdown, GracefulRestart,
                               ForceRestart, Nmi, ForceOn, PushPowerButton, PowerCycle.
                               Note that above types valid according to redfish spec.
                               In reality, managers may implement a subset of types,
                               denoted by the ResetType@Redfish.AllowableValues field.
        """
        self.logger.info("Reset BMC")
        body = {"ResetType": "ForceRestart"}
        url = "/redfish/v1/Managers/{}/Actions/Manager.Reset".format(self.bmc_name)
        self._session.post(url, body=body)
