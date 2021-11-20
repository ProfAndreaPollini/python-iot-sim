# Python Iot Simulator

Questo progetto é pensato per una esercitazione del corso di Tecnologie e Progettazione di sistemi infomativi e di telecomunicazioni, nella classe quinta.



## ESERCITAZIONE

Collegarsi al web service che il nostro cliente ci ha segnalato per il lavoro che dobbiamo fare all'indirizzo: https://hf3xzw.deta.dev/ (qua troverai l'elenco di tutti i sensori presenti nel sistema).

Il sistema di cui dobbiamo costruire una dashboard di controllo é formato da quattro sensori di tipo toggle (che assumono i valori vero o falso).
 
```json
{
"description": "porta aperta",
"id": "s-04",
"lat": "32.9156",
"lng": "-117.14392",
"place": "Mira Mesa",
"readonly": false,
"state_code": "US",
"value": false
},
```

Sono presenti inoltre alcuni sensori di vario tipo che memorizzano valori reali.

```json
{
"description": "sensore di temperatura",
"id": "temperature-01",
"lat": "15.45144",
"lng": "78.14797",
"place": "Betamcherla",
"readonly": true,
"state_code": "IN",
"value": 30.638888363380268
},
```


Lo stato dei singoli sensori é reperibile  facendo una chiamata `GET all'uri` `https://hf3xzw.deta.dev/<id>` dove `<id>` é l'id del sensore.

Per i sensori di tipo toggle é possibile cambiarne lo stato effettuando una chiamata PUT all'indirizzo `https://hf3xzw.deta.dev/<id>/toggle`.

Link alternativo: https://python-iot-sim.professorandrea.repl.co/

Realizzare utilizzando un framework CSS a scelta una webapp per la visualizzazione dei dati, facendo anche ricorso a delle librerie per i grafici. Deve essere inoltre possibile effettuare la modifica dello stato dei toggle button.
