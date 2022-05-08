#!/usr/bin/python

"""
#---------------------------------------------------------------------------------------------------
# Genetic REST Api
# Modules and code for Python Python 3.8.
#---------------------------------------------------------------------------------------------------
"""

import os

import logging

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse


OAPI_TAGS = [
    {
        "name": "healthcheck",
        "description": "Respond with 'status: alive', for monitoring purposes."
    }
]

APP = FastAPI(title="Kyndryl API",
              description="Kyndryl API for testing purposes",
              docs_url="/",
              openapi_tags=OAPI_TAGS)

@APP.get("/health", tags=["healthcheck"])
async def healthcheck():
    """Standard route for health check used to monitor service."""
    return JSONResponse(status_code=status.HTTP_200_OK, content={'status': 'alive'})

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info('Debug mode set to {:s}'.format(str(os.environ.get('debug'))))
LOGGER.root.setLevel(logging.DEBUG if bool(os.environ.get('debug') == 'True') else logging.INFO)
