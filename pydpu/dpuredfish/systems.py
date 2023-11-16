import logging

import redfish


class Systems:
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
        # TODO: find system name dynamically
        self.system_name = "Bluefield"
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

    def get_processors(self):
        self.logger.info("Getting Processors")
        # TODO: create decorator for login/logout
        self._session.login(auth="session")
        response = self._session.get(
            "/redfish/v1/Systems/{}/Processors?$expand=.($levels=1)".format(
                self.system_name
            )
        )
        self.logger.debug(response.text)
        self._session.logout()
        for item in response.obj.Members:
            yield item

    def get_storage(self):
        self.logger.info("Getting Storage ...")
        # TODO: create decorator for login/logout
        self._session.login(auth="session")
        response = self._session.get(
            "/redfish/v1/Systems/{}/Storage?$expand=~($levels=1)".format(
                self.system_name
            )
        )
        self.logger.debug(response.text)
        self._session.logout()
        return response.obj

    def get_memory(self):
        self.logger.info("Getting Memory")
        # TODO: create decorator for login/logout
        self._session.login(auth="session")
        response = self._session.get(
            "/redfish/v1/Systems/{}/Memory?$expand=.($levels=1)".format(
                self.system_name
            )
        )
        self.logger.debug(response.text)
        self._session.logout()
        for ch in response.obj.Members:
            yield ch

    def get_networks(self):
        self.logger.info("Getting EthernetInterfaces")
        # TODO: create decorator for login/logout
        self._session.login(auth="session")
        response = self._session.get(
            "/redfish/v1/Systems/{}/EthernetInterfaces?$expand=.($levels=1)".format(
                self.system_name
            )
        )
        self.logger.debug(response.text)
        self._session.logout()
        for item in response.obj.Members:
            yield item
