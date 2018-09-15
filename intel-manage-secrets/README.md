# Connection to AWS IoT
- to connect to aws IoT you need to provide valid certificates
- in this case the certificates are signed by a rootCA
- when connecting for the first time with aws JIT will be triggered, creating a policy, a thing
and attaching them together allowing the device to connect to the cloud

## certificate commands
- generate certificates
```bash
bash generateCerts.sh
```
- clean certificates
```bash
bash cleanCerts.sh
```
- regenerate certificates
```bash
bash regenCerts.sh
```

## testing connection
- install mosquitto using `brew install mosquitto`
- subscribe to a topic
```bash
mosquitto_sub --cafile root.pem --cert deviceCert.crt --key deviceCert.key -h a2s7dpv6qj1qss.iot.us-west-2.amazonaws.com -p 8883 -q 1 -t  foo/bar -i testing --tls-version tlsv1.2 -d
```
- publish to a topic
```bash
mosquitto_pub --cafile root.pem --cert deviceCert.crt --key deviceCert.key -h a2s7dpv6qj1qss.iot.us-west-2.amazonaws.com -p 8883 -q 1 -t  foo/bar -i testing --tls-version tlsv1.2 -d
```

## clone this repo on any device
- clone command:
```bash
git clone https://18ce1ec5e702c5f6091bc04e4c2215e9f0475d76@github.com/nazihahmed/intel-manage-secrets.git
```

## update the JITP template
```bash
aws iot update-ca-certificate --certificate-id 70927b6521fb111462d795f009b2498a995d4e1b57cc0f9278bff3ee859cb510 --new-auto-registration-status ENABLE --registration-config file://str-jitp.txt
```
