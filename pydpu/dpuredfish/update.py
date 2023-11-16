import logging

import redfish


class UpdateService:
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

    def get_version(self, module):
        return self._session.get(
            "/redfish/v1/UpdateService/FirmwareInventory/{}".format(module)
        ).dict.get("Version")

    def get_versions(self):
        self.logger.info("Getting Versions...")
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get(
            "/redfish/v1/UpdateService/FirmwareInventory?$expand=.($levels=1)"
        )
        if "error" in response.dict or "Members" not in response.dict:
            error_message = "\n".join(
                msg.get("Message") for msg in response.dict.get("Messages", [])
            )
            raise RuntimeError(
                "Unable to get firmware list: HTTP {}: {}".format(
                    response.status, error_message
                )
            )
        return dict(
            (i.get("Id"), i.get("Version")) for i in response.dict.get("Members")
        )
