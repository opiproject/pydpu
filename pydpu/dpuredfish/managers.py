import logging

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
        # TODO: find bmc name dynamically
        self.bmc_name = "Bluefield_BMC"
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

    def get_bmc_datetime(self):
        self.logger.info("Getting BMC time...")
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get("/redfish/v1/Managers/{}".format(self.bmc_name))
        self.logger.debug(response.text)
        self._session.logout()
        return response.dict.get("DateTime")

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
