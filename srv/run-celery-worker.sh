#!/bin/bash

cd ..
celery -A server.apps.main.tasks worker --loglevel=INFO
