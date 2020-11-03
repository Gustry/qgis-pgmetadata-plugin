__copyright__ = "Copyright 2020, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"

import os

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from pg_metadata.processing.administration.create_administration_project import (
    CreateAdministrationProject,
)
from pg_metadata.processing.database.create import CreateDatabaseStructure
from pg_metadata.processing.database.recompute_values import RecomputeValues
from pg_metadata.processing.database.reset_html_template import (
    ResetHtmlTemplate,
)
from pg_metadata.processing.database.upgrade import UpgradeDatabaseStructure
from pg_metadata.qgis_plugin_tools.tools.resources import resources_path


class PgMetadataProvider(QgsProcessingProvider):

    def loadAlgorithms(self):

        flag = os.environ.get('PGMETADATA_USER', False)
        if flag:
            return

        # Admin
        self.addAlgorithm(CreateAdministrationProject())

        # Database
        self.addAlgorithm(CreateDatabaseStructure())
        self.addAlgorithm(RecomputeValues())
        self.addAlgorithm(ResetHtmlTemplate())
        self.addAlgorithm(UpgradeDatabaseStructure())

    def id(self):  # NOQA
        return "pg_metadata"

    def icon(self):
        return QIcon(resources_path("icons", "icon.png"))

    def name(self):
        return "PgMetadata"
