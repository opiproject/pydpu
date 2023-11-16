import logging

import redfish


class AccountService:
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

    def get_accounts(self):
        self.logger.info("Getting Accounts...")
        # TODO: create decorator for login/logout
        self._session.login(auth=redfish.AuthMethod.SESSION)
        response = self._session.get(
            "/redfish/v1/AccountService/Accounts?$expand=.($levels=1)"
        )
        self._session.logout()
        self.logger.debug(response.text)
        for entry in response.dict.get("Members"):
            yield entry
