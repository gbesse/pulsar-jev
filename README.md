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

FR : le seuil par défaut est `0.8`. Les routes sont `yes`, `no`, `review` et `failure`. Une entrée vide ou supérieure à 32 Kio donne `review` ; une erreur de transport ou de réponse donne `failure`. Le client limite les appels à 10 000 par processus, à 10 s par appel et à 100 Kio par réponse. Un cache LRU conserve au plus 1 024 verdicts valides par empreinte SHA-256 ; il ne conserve pas le texte brut. Les données sont envoyées à TypeSafe Jev.

EN: the default threshold is `0.8`. Routes are `yes`, `no`, `review`, and `failure`. Empty input or input over 32 KiB becomes `review`; transport or response errors become `failure`. The client caps calls at 10,000 per process, 10 seconds per call, and 100 KiB per response. An LRU cache keeps at most 1,024 valid verdicts by SHA-256 digest; it does not store raw text. Data is sent to TypeSafe Jev.

ES: el umbral predeterminado es `0.8`. Las rutas son `yes`, `no`, `review` y `failure`. Una entrada vacía o superior a 32 KiB produce `review`; los errores de transporte o respuesta producen `failure`. El cliente limita las llamadas a 10 000 por proceso, a 10 s por llamada y a 100 KiB por respuesta. Una caché LRU conserva como máximo 1 024 decisiones válidas por huella SHA-256; no almacena el texto original. Los datos se envían a TypeSafe Jev.

## Deploy / Déployer / Desplegar

FR : `package.py` fabrique le ZIP attendu par Pulsar. Déployez-le avec la classe indiquée et des sujets d’entrée et de sortie. La sortie JSON contient `jev.route`, `jev.probability` et `jev.state_sha256`. Le paramètre `max_calls` borne les appels par instance de Function.

EN: `package.py` builds the ZIP expected by Pulsar. Deploy it with the named class and input/output topics. Output JSON contains `jev.route`, `jev.probability`, and `jev.state_sha256`. The `max_calls` parameter bounds calls per Function instance.

ES: `package.py` crea el ZIP esperado por Pulsar. Despliéguelo con la clase indicada y los temas de entrada y salida. El JSON de salida contiene `jev.route`, `jev.probability` y `jev.state_sha256`. El parámetro `max_calls` limita las llamadas por instancia de la función.

```sh
python package.py --output pulsar-jev.zip
pulsar-admin functions create --py pulsar-jev.zip --classname pulsar_jev.JevDecisionFunction \
  --inputs persistent://public/default/reviews \
  --output persistent://public/default/reviews-decided \
  --tenant public --namespace default --name jev-review \
  --user-config '{"question":"Does the review recommend the movie?","text_field":"text","max_calls":10000}'
```

## TLS / TLS / TLS

FR : si votre installation Python ne trouve pas les certificats racines, définissez `SSL_CERT_FILE` vers un bundle CA valide (par exemple `certifi.where()`). Ne désactivez pas la vérification TLS.

EN: if Python cannot find root certificates, set `SSL_CERT_FILE` to a valid CA bundle (for example `certifi.where()`). Keep TLS verification enabled.

ES: si Python no encuentra los certificados raíz, defina `SSL_CERT_FILE` con un paquete CA válido (por ejemplo `certifi.where()`). Mantenga activa la verificación TLS.

## Development / Développement / Desarrollo

`python -m unittest discover -p "test_*.py" -v`

Platform / Plateforme / Plataforma: [Apache Pulsar documentation](https://pulsar.apache.org/docs/2.10.x/functions-package/).

MIT license. Community project; not an official Apache Pulsar integration.
