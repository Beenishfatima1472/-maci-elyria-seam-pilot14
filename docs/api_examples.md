# API Examples

## Health Check

```bash
curl http://localhost:8080/health
```

Expected response:

```json
{
  "service": "maci-seam-pilot",
  "status": "ok"
}
```

## Evaluate Packet

```bash
curl -X POST http://localhost:8080/evaluate \
  -H 'Content-Type: application/json' \
  -d @examples/valid_signal_packet.json
```

Expected outcome:

```text
CONDITIONALLY_ADMISSIBLE
BOUNDARY_RESULT_REQUIRED_BEFORE_BIND
```
