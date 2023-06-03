# Sonatype: Nexus Repository Manager Python SDK

- [Sonatype: Nexus Repository Manager Python SDK](#sonatype-nexus-repository-manager-python-sdk)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Quick Start Guide](#quick-start-guide)
  - [Detailed Documentation](#detailed-documentation)
  - [Contribute](#contribute)
  - [Acknowledgements](#acknowledgements)

## Overview

The Sonatype Nexus Python SDK is a powerful tool designed to facilitate the interaction of Python developers with Sonatype Nexus IQ Server and Nexus Repository Manager APIs. In addition, this SDK aims to simplify and streamline integrating the Nexus IQ Server and Nexus Repository Manager into your CI/CD pipelines.

**GitHub Repository**: [https://github.com/beholdenkey/nxrm-sdk](https://github.com/beholdenkey/nxrm-sdk)

## Prerequisites

Ensure you have the following prerequisites before you proceed with the installation:

- Python version 3.9 or later
- pip (Python package installer)

## Installation

You can install the Sonatype Nexus Python SDK using pip. Run the following command in your terminal:

```bash
pip install sonatype-nxrm-sdk
```

After successful installation, import the package in your Python script:

```python
import nxrm_sdk
```

## Quick Start Guide

Below is a simple example of how to delete a single asset using the SDK.

First, ensure that the package is correctly [installed](https://chat.openai.com/?model=gpt-4-browsing#installation) and then proceed as follows:

```python
import nxrm_sdk
from nxrm_sdk.apis.tags import assets_api
# Defining the host is optional and defaults to http://localhost/service/rest
# Check configuration.py for a complete list of supported configuration parameters.
configuration = nxrm_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nxrm_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = "id_example" # str | Id of the asset to delete

    try:
        # Delete a single asset
        api_instance.delete_asset(asset_id)
    except nxrm_sdk.ApiException as e:
        print(f"Exception when calling AssetsApi->delete_asset: {e}")

```

Please replace "id_example" with the ID of the asset you want to delete.

## Detailed Documentation

For more detailed documentation on the API and its usage, please visit the [Sonatype Nexus Python SDK GitHub Repository](https://github.com/beholdenkey/nxrm-sdk).

## Contribute

We welcome and appreciate any contributions. Please refer to the [Contribution Guidelines](CONTRIBUTING.md) for details on how you can contribute to this project.

## Acknowledgements

We would like to extend our gratitude to the [OpenAPI Generator](https://openapi-generator.tech) project and the [OpenAPI Initiative](https://www.openapis.org/). This SDK was initially generated using the OpenAPI Generator and would not have been possible without the OpenAPI Initiative.
