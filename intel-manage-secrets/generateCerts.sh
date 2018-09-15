#!/bin/bash
DIR="../certs"
if [ ! -d "$DIR" ]; then
  mkdir "$DIR"
  cp root.pem $DIR
  openssl genrsa -out $DIR/deviceCert.key 2048
  openssl req -subj "//C=IL/O=Makovation" -new -key $DIR/deviceCert.key -out deviceCert.csr
  openssl x509 -req -in deviceCert.csr -CA sampleCACertificate.pem -CAkey sampleCACertificate.key -CAcreateserial -out deviceCert.crt -days 3650 -sha256
  cat deviceCert.crt sampleCACertificate.pem > $DIR/deviceCert.crt
  rm deviceCert.*
fi
