# MediaFireDownloader
Script per il download di file RAR da MediaFire

# Utilizzo
   1) Scaricare e inserire il file nella cartella in cui si desidera scaricare i file rar;
   2) Creare un file .txt contenente tutti i link (uno per riga) alle pagine di download di mediafire desiderate;
   3) Sostituire il path del file contenente i link con quello del file da voi appena creato;
   4) Avviare lo script e attendere che si concluda.
   
# Realizzazione
Per la realizzazione sono state scelte le librerie seguenti:
   1) requests : utilizzata per scaricare il file rar;
   2) urllib.request : utilizzata per estrarre il codice html dalla pagina di download;
   3) BeautifulSoup : utilizzata per estrarre il link del download diretto.
   
# Funzionamento
Lo script una volta eseguito apre il file contenente i link e li estrae inserendoli in una lista, dopo di che scorre la lista elemento per elemento.
Per ogni elemento estrae il codice HTML della pagina a cui fa riferimento e ne estrae il campo relativo al link contenente il download diretto.
Usa il link appena trovato per scaricare il file rar.
