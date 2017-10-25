"""
Plugin definition for the SMART-opal Opal plugin
"""
from opal.core import plugins

from SMART-opal.urls import urlpatterns

class Smart-OpalPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our Opal application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.SMART-opal': [
            # 'js/SMART-opal/app.js',
            # 'js/SMART-opal/controllers/larry.js',
            # 'js/SMART-opal/services/larry.js',
        ]
    }

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}