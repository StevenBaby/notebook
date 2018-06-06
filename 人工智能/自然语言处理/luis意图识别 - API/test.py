import requests
import dandan
import json

logger = dandan.logger.getLogger()


class LUIS(object):

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"

    def __init__(self, key=None, domain="westus.api.cognitive.microsoft.com"):
        self.key = key
        self.domain = domain
        self.session = requests.Session()
        self.session.headers = {
            'Content-Type': 'application/json',
            "Ocp-Apim-Subscription-Key": self.key,
        }

    def get_key(self):

        return self.key

    def get_response(self, api, params={}, method="GET", **kwargs):
        if "{domain}" in api:
            kwargs["domain"] = self.domain
        api = api.format(**kwargs)

        if method.upper() == self.GET:
            return self.session.get(api, params=params).json()
        elif method.upper() == self.POST:
            return self.session.post(api, data=json.dumps(params)).json()
        elif method.upper() == self.DELETE:
            return self.session.delete(api, params=params).json()

    def get_app_list(self, skip=0, take=100):
        api = "https://{domain}/luis/api/v2.0/apps/"

        params = {
            "skip": skip,
            "take": take,
        }
        return self.get_response(api, params)

    def get_app_info(self, name=None, appId=None):
        if not name and not appId:
            return None
        if appId:
            api = "https://{domain}/luis/api/v2.0/apps/{appId}"
            return self.get_response(api, appId=appId)

        apps = self.get_app_list()
        for app in apps:
            app = dandan.value.AttrDict(app)
            if app.name == name:
                return app
        return None

    def get_app_settings(self, appId):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/settings"
        return self.get_response(api, appId=appId)

    def get_endpoints(self, appId):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/endpoints"
        return self.get_response(api, appId=appId)

    def get_app_cultures_list(self):
        api = "https://{domain}/luis/api/v2.0/apps/cultures"
        return self.get_response(api)

    def get_app_domains_list(self):

        api = "https://{domain}/luis/api/v2.0/apps/domains"
        return self.get_response(api)

    def add_app(self, name, culture, description=""):

        api = "https://{domain}/luis/api/v2.0/apps/"

        params = {
            "name": name,
            "description": description,
            "culture": "en-us",
            "usageScenario": "IoT",
        }
        return self.get_response(api, method=self.POST, params=params)


class App(LUIS):

    def __init__(self, key, appId, domain="westus.api.cognitive.microsoft.com"):
        super().__init__(key=key, domain=domain)
        self.appId = appId
        self.info = self.get_app_info()
        versions = self.get_version_list()
        self.version = None
        for version in versions:
            version = dandan.value.AttrDict(version)
            if version.version == self.info.activeVersion:
                self.version = version
                break

        self.intents = dandan.value.AttrDict()

        intents = self.get_intents()
        for intent in intents:
            intent = dandan.value.AttrDict(intent)
            self.intents[intent.name] = intent

    def get_response(self, api, params={}, method="GET", **kwargs):

        if "{appId}" in api and "appId" not in kwargs:
            kwargs["appId"] = self.appId
        if "{versionId}" in api and "versionId" not in kwargs:
            kwargs["versionId"] = self.version.version

        return super().get_response(api, params=params, method=method, **kwargs)

    def get_app_info(self):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}"
        info = self.get_response(api, appId=self.appId)
        return dandan.value.AttrDict(info)

    def get_version_list(self, skip=0, take=100):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions"
        params = {
            "skip": skip,
            "take": take,
        }
        return self.get_response(api, params=params)

    def get_intents(self, skip=0, take=100, versionId=None):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/intents"

        params = {
            "skip": skip,
            "take": take,
        }
        if not versionId:
            versionId = self.version.version

        return self.get_response(api, params=params, versionId=versionId)

    def has_intent(self, name):
        for intent in self.get_intents():
            intent = dandan.value.AttrDict(intent)
            if intent.name == name:
                return True
        return False

    def get_intent(self, name=None, id=None):

        intents = self.get_intents()

        for intent in intents:
            intent = dandan.value.AttrDict(intent)
            if intent.id == id:
                return intent
            if intent.name == name:
                return intent
        return None

    def create_intent(self, name):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/intents"
        params = {
            "name": name,
        }
        return self.get_response(api, params=params, method=self.POST, versionId=self.version.version)

    def delete_intent(self, intentId):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/intents/{intentId}"

        params = {
            "deleteUtterances": True,
        }
        return self.get_response(api, params=params, method=self.DELETE, intentId=intentId)

    def has_entity(self, name):
        entities = self.get_entities()
        for entity in entities:
            entity = dandan.value.AttrDict(entity)
            if entity.name == name:
                return True
        return False

    def get_entity(self, entityId):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/entities/{entityId}"
        return self.get_response(api, entityId=entityId)

    def get_entities(self):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/entities"

        return self.get_response(api)

    def create_entity(self):

        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/entities"
        pass

    def query(self, utterance):
        api = "https://{domain}/luis/v2.0/apps/{appId}"
        params = {
            "verbose": True,
            "timezoneOffset": 0,
            "q": utterance,
        }
        return self.get_response(api, params=params)

    def get_train_status(self):

        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/train"

        return self.get_response(api, versionId=self.version.version)

    def train(self):

        api = "https://{domain}/luis/api/v2.0/apps/{appId}/versions/{versionId}/train"
        return self.get_response(api, method="POST", versionId=self.version.version)

    def publish(self, versionId=None, isStaging=False, region="westus"):
        api = "https://{domain}/luis/api/v2.0/apps/{appId}/publish"
        if not versionId:
            versionId = self.version.version

        params = {
            "versionId": versionId,
            "isStaging": isStaging,
            "region": region
        }
        return self.get_response(api, params=params, method=self.POST)

    def delete(self):
        """Delete the app, be careful for call this function
        """
        api = "https://{domain}/luis/api/v2.0/apps/{appId}"
        return self.get_response(api, method=self.DELETE)


def main():
    key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    appname = "MyFirstDummyApp"
    appname = "master"

    luis = LUIS(key=key)

    info = luis.get_app_info(name=appname)
    if not info:
        logger.debug("add app %s", appname)
        appId = luis.add_app(appname, "en-us", "This is my first dummy application")
        logger.debug(appId)
    else:
        appId = info.id

    logger.debug(appId)

    app = App(key=key, appId=appId)
    # response = app.has_entity("消息")
    response = app.get_entities()
    logger.debug(response)


if __name__ == '__main__':
    main()
