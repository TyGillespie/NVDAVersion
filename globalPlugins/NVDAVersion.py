# NVDAVersion.py
# A part of NVDAVersion.
# Copyright (C) 2020, Ty Gillespie. All rights reserved.
# GPL3 License.

"""Main file.
"""

import globalPluginHandler
from scriptHandler import script
import ui
import versionInfo

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(gesture="kb:NVDA+shift+v")
	def script_announceNvdaVersionRegular(self, gesture):
		ui.message(versionInfo.version)

	@script(gesture="kb:NVDA+shift+control+v")
	def script_announceNvdaVersionBrowseable(self, gesture):
		ui.browseableMessage(versionInfo.version)
