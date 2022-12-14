#!/usr/bin/env python
"""Select operating system specific implementations of builder."""

import platform

# pylint: disable=unused-import,g-import-not-at-top,g-bad-name

if platform.system() == "Linux":
  from grr_response_client_builder.builders import linux
  DebianClientBuilder = linux.DebianClientBuilder
  CentosClientBuilder = linux.CentosClientBuilder

elif platform.system() == "Windows":
  from grr_response_client_builder.builders import windows
  WindowsClientBuilder = windows.WindowsClientBuilder

elif platform.system() == "Darwin":
  from grr_response_client_builder.builders import osx
  DarwinClientBuilder = osx.DarwinClientBuilder
