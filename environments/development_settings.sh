#!/bin/bash
# make a copy of this file to development_settings_local.sh
# and fill in the blanks
# do not add development_settings.sh to the sourcecode
# adding database usernames and passwords to the sourcecode
# is adviced against, due to security considerations.


#export DJOSER_DOMAIN=localhost:4200

export DJANGO_SECRET_KEY='8bu+4ca!3whpz)*yp)sr*d)=zyhmqo_ulb6sog^05ci%7vaz+g'
export DJANGO_DEBUG_STATE=True
export DJANGO_EMAIL_HOST=smtp.gmail.com
export DJANGO_EMAIL_HOST_USER=cuponengine@gmail.com
export DJANGO_EMAIL_HOST_PASSWORD=m0tordec0ntacto
export DJANGO_EMAIL_PORT=587
export DJANGO_RAVEN_CONFIG_DNS=https://31c9c7e9d8b541ad9606ee8a0fb90269:5593409472fe4481b143a2518be0a1bd@sentry.io/1204245
export DJANGO_GOOGLE_RECAPTCHA_SECRET_KEY=6LfSt6cUAAAAAHdUAhiyHQpzCeoZ-Cwz3b1bPmGY
export DJANGO_SETTINGS_MODULE=talanaTest.settings.dev