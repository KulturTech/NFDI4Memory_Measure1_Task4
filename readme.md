# Readme zu Priorisierten Dateiformaten in den historisch arbeitenden Fächern

**Ersteller*in Readme:** [Gomes, Sera Ria]

**Erstellungsdatum Readme:** [20.02.2026]

## Titel des Forschungsdatensatzes
Interaktiver Tafel gängiger Dateiformate (Langzeitarchvierung)

## Ort der Datenerhebung
Marburg an der Lahn, Hessen, Deutschland
[50.8086176 | 8.7585582]

**Version:** [1-0]

## Herausgeber*in: [Herder-Institut für Historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft]

**Herausgeber*in Identifier:** [GND: 3024025-6]

---

## Ersteller*innen des Datensatzes
- **Ersteller*in 1:** Gomes, Sera Ria
  - Identifier: [ORCID: 0009-0001-5237-9441]
  - Affiliation: Herder-Institut für Historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft, Marburg, Hessen, Deutschland

## Beteiligte
- **Körfer, Anna-Lena** [ORCID: 0009-0001-3362-9759]
  - Affiliation: Herder-Institut für Historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft, Marburg, Hessen, Deutschland
  - Typ: [ProjectLeader]
- **Pravdyuk, Anna** [ORCID: 0000-0001-7567-4008]
  - Affiliation: Herder-Institut für Historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft, Marburg, Hessen, Deutschland
  - Typ: [ProjectMember]
- **Donig, Simon** [ORCID: 0000-0002-1741-466X]
  - Affiliation: Herder-Institut für Historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft, Marburg, Hessen, Deutschland
  - Typ: [ProjectLeader]

---

## Projektname
NFDI4Memory
[DFG GEPRIS-Portal: https://gepris.dfg.de/gepris/projekt/501609550?context=projekt&task=showDetail&id=501609550&]

## Abstract
Die Interaktive Tafel gängiger Dateiformate (Langzeitarchivierung) ist eine webbasierte Anwendung, die im Rahmen von Measure 1, Task 4 der Task Area "Data Quality" von NFDI4Memory entwickelt wurde. Sie richtet sich an Forschende aus den historisch arbeitenden Wissenschaften sowie an Mitarbeitende in Kultur- und Gedächtniseinrichtungen (GLAM-Institutionen).

## Inhalt und Entstehungskontext
Die Anwendung stellt eine kuratierte Übersicht gängiger Dateiformate bereit, die auf den Ergebnissen einer Community-weiten Umfrage zu Praktiken, Standards und Bedarfen zur Datenqualität in den historisch arbeitenden Disziplinen basiert (DOI: 10.5281/zenodo.17434287). Die Auswahl der Dateiformate sowie ihre Bewertung orientieren sich an der Handreichung der Task Area „Data Quality" und an Konventionen etablierter Institutionen wie KOST-CECO, Landesinitiative Langzeitverfügbarkeit des NRW und dem Schweizerischen Bundesarchiv.

## Struktur und Aufbau
Die Datenbasis umfasst tabellarisch strukturierte Informationen zu Dateiformaten, gegliedert nach folgenden Spalten: Dateiart (Kategorie, z. B. Text & Textverarbeitung, Bild & Vektorgrafiken, Multimedia & Musik, Daten & Tabellen), Datenformat (spezifisches Format bzw. Dateiendung), Ampelstatus (Empfehlungsstatus zur Langzeitarchivierung) sowie Quelle(n) (Referenz auf zugrunde liegende Empfehlungen).

Der Ampelstatus unterscheidet zwischen drei Kategorien: empfohlen (grün), bedingt geeignet (orange) und nicht empfohlen (rot). Als Bewertungskriterien gelten offene und nicht-proprietäre Dokumentation, verlustfreie Speicherung ohne Kompression, einfache Dekodierbarkeit sowie die Bindung an einen ISO-Standard oder eine vergleichbare Normierung.

Die Webanwendung umfasst den Quellcode (HTML, CSS, JavaScript) sowie die zugrunde liegende Datendatei, aus der die interaktive Tabelle dynamisch generiert wird. Die Anwendung liest die Daten ein und ermöglicht eine filterbasierte Ansicht nach Dateikategorie und Empfehlungsstatus.

Die Anwendung ist unter einer Creative Commons Attribution 4.0 International Lizenz (CC BY 4.0) frei zugänglich.

###### **Schlagwörter**:					    [Forschungsdatenmanagement]
                                      [NFDI4Memory]
                                      [Geschichtswissenschaft]
                                      [Datenqualität]
                                      [Datenqualitätsmanagement]
                                      [Data Quality Assessment]
                                      [Datensammlung]
                                      [Repositorium]
                                      [Data set]

## Methode der Datenerhebung
[Händische Online-Recherche in Datenbanken sowie Portalen, Repositorien, digitalen Archiven und Datenaggregationsdiensten]

---

## Dateiliste
- `index.html` – Hauptdatei der Webanwendung; enthält Struktur, Filterlogik und die interaktive Tabelle der Dateiformate
- `default.css` – Stylesheet der Anwendung; definiert Layout und visuelle Gestaltung inkl. des Ampelsystems
- `images/` – Ordner mit Grafikdateien (SVG); enthält u. a. das NFDI4Memory-Logo
- `Notizen M1-T4.docx` – Interne Arbeitsnotizen zur Entwicklung der Task 4

**Dateiformate:** [.md]
                  [.html]
                  [.css]
                  [.csv]
                  [.json]
                  [.py]
                  [.svg]

---

###### **Anmerkungen**: 					    
                                                [Diese Arbeit ist im Rahmen des Konsortiums NFDI4Memory entstanden (www.nfdi4memory.de). Gefördert von der DFG, Projektnummer 50 1609550]

###### **Literatur**:                           
                                                [ETH Zürich (2025): "Archivtaugliche Dateiformate", (https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate)]
                                                [Körfer et al. (2025): "Konvention zu Priorisierten Dateiformaten am Herder-Institut für historische Ostmitteleuropaforschung - Institut der Leibniz-Gemeinschaft", Version 1-0, Zenodo, (https://doi.org/10.5281/zenodo.18389871)]
                                                [KOST-CECO: Koordinationsstelle für dauerhate Archivierung elektronischer Unterlagen: "Katalog archivischer Dateiformate", (https://kost-ceco.ch/cms/kad_main_de.html)]
                                                [Ogan, Kayhan/Quast, Andres (2024): "Interaktive Tafel gängiger Dateiformate", lzv.nrw: Landesinitiative Langzeitverfügbarkeit, (https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social)]
                                                [Ogan, Kayhan/Quast, Andres (2024): "lzv.nrw/file-formats-table", (https://github.com/lzv-nrw/file-formats-table), letzter Zugriff: 21. November 2024 ]
                                                [Schweizerisches Bundesarchiv (2020): "Standards für die Archivierung digitaler Unterlagen - Archivtaugliche Dateiformate", Version 2020/04, (https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf)]
                                                [Verbundzentrale des GBV: "Bibliografische Datenformate", (https://format.gbv.de/application/bibliographic)]
