# pulsar-jev

## Français

Function Python qui enrichit chaque événement JSON avec un verdict Jev.

Regroupez les deux fichiers dans le dossier `src/` d’une archive ZIP Pulsar, déployez la Function et définissez `JEV_API_KEY` sur le worker.

## English

Python Function enriching each JSON event with a Jev verdict.

Package `pulsar_jev.py` and `jev_common.py` inside `src/` in a Pulsar Python Function ZIP. Deploy with `--py func.zip --classname pulsar_jev.JevDecisionFunction --user-config '{"question":"Does this review recommend the movie?","text_field":"text"}'`, input and output topics. Set `JEV_API_KEY` in the function worker environment.

## Español

Función Python que amplía cada evento JSON con una decisión Jev.

Empaquete los dos archivos en el directorio `src/` de un ZIP Pulsar, despliegue la función y defina `JEV_API_KEY` en el worker.

## Contract / Contrat / Contrato

`yes`, `no`, `review`, `failure`; threshold default `0.8`. `review` is a real undecided state. Empty or oversized input becomes `review`; transport or invalid-response errors become `failure`. The shared client caps input at 32 KiB, response at 100 KiB, timeout at 10 s and calls at 10,000 per process; YAML templates enforce their own input and response bounds. No raw input is logged by this project. User data goes to the TypeSafe Jev API.

FR : `review` exige une revue humaine ; `failure` signale une erreur. Le contenu est envoyé à l’API TypeSafe Jev.

ES: `review` requiere revisión humana; `failure` indica un error. El contenido se envía a la API TypeSafe Jev.

## TLS / TLS / TLS

FR : si votre installation Python ne trouve pas les certificats racines, définissez `SSL_CERT_FILE` vers un bundle CA valide (par exemple `certifi.where()`). Ne désactivez pas la vérification TLS.

EN: if Python cannot find root certificates, set `SSL_CERT_FILE` to a valid CA bundle (for example `certifi.where()`). Keep TLS verification enabled.

ES: si Python no encuentra los certificados raíz, defina `SSL_CERT_FILE` con un paquete CA válido (por ejemplo `certifi.where()`). Mantenga activa la verificación TLS.

## Development / Développement / Desarrollo

`python -m unittest discover -p "test_*.py" -v`

Platform / Plateforme / Plataforma: [Apache Pulsar documentation](https://pulsar.apache.org/docs/2.10.x/functions-package/).

MIT license. Community project; not an official Apache Pulsar integration.
