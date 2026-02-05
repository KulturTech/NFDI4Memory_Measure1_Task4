# Install: pip install langchain chromadb sentence-transformers

from langchain.document_loaders import JSONLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

# 1. Load your dashboard data
def load_format_data():
    # Parse your HTML file's JSON
    [
  {
    "Dateiart": "Text",
    "Datenformate": "XML Extensible Markup Language 1.1",
    "Quellen zur Ampel": "Schweizerisches Bundesarchiv (BAR): https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "JSON JavaScript Object Notation",
    "Quellen zur Ampel": "Schweizerisches Bundesarchiv (BAR): https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "CSV Comma-Separated Values",
    "Quellen zur Ampel": "lzv.nrw: https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social",
    "Ampel": "orange",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "TXT Textdatei (Codierung UTF-8)",
    "Quellen zur Ampel": "Schweizerisches Bundesarchiv (BAR): https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "PDF A Portable Document Format A",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "OOXML (Office Open Extensible Markup Language)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "orange",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "PDF/A-3 (*.pdf)",
    "Quellen zur Ampel": "Schweizerisches Bundesarchiv (BAR): https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "RTF Rich Text Format",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "XML mit DTD-Datei oder XML-Schema, JSON, HTML",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "HTML und XML",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "OpenDocument Formate (*.odm, *.odt, *.odg, *.odc, *.odf)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "JSON LD JavaScript Object Notation for Linked Data",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "RDFa Resource Description Framework in Attributes",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "DOCX Word",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "LaTeX und TeX",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "MD Markdown",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "DOC Word",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Text",
    "Datenformate": "PPT PowerPoint",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Unformatierter Text",
    "Datenformate": "Unformatierter Text (*.txt, *.asc, *.c, *.h, *.cpp, *.m, *.py, *.r usw.)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Unformatierter Text",
    "Datenformate": "MD Markdown",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "grün",
    "Kategorie": "text"
  },
  {
    "Dateiart": "Musik",
    "Datenformate": "MEI Music Encoding Initiative",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Musik",
    "Datenformate": "MusicXML",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Musik",
    "Datenformate": "Parsons Code",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Musik",
    "Datenformate": "PDF A Portable Document Format A",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "Master: baseline Tagged Image File Format (TIFF), unkomprimiert; TIFF mit Lempel-Ziv-Welch-Komprimierung (TIFF-LZW)",
    "Quellen zur Ampel": "lzv.nrw: https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "JPEG 1 und JPEG 2000 Joint Photographic Experts Group, verlustfrei komprimiert, lizenzfreie Bereiche",
    "Quellen zur Ampel": "lzv.nrw: https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "PDF-Format, Typ PDF/A-2",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "Präsentationsformate (Derivate): JPEG, JPEG 2000, Portable Network Graphics (PNG)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "DNG Rohdaten: Digital Negative",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "PSD Photoshop",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Rastergrafiken)",
    "Datenformate": "TIFF+EWF.XML- Tagged Image File Format und Exdended World Fil",
    "Quellen zur Ampel": "Schweizerisches Bundesarchiv (BAR): https://www.bar.admin.ch/dam/bar/de/dokumente/konzepte_und_weisungen/archivtaugliche_dateiformate.1.pdf.download.pdf/archivtaugliche_dateiformate.pdf",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "SVG Scalable Vector Graphics",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "DWG AutoCAD Drawing",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "rot",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "DXF Drawing Interchange Format, AutoCAD",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "orange",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "Extensible 3D, X3D (*.x3d, *.x3dv, *.x3db)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "grün",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "EPS Encapsulated Postscript",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "rot",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Bild (Vektorgrafiken) und CAD",
    "Datenformate": "INDD Grafik InDesign (*.indd), Illustrator (*.ait)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "image"
  },
  {
    "Dateiart": "Audio",
    "Datenformate": "Archivformat: Waveform Audio File-Format (WAV) in Verbindung mit Pulse Code Modulation (PCM); Free Lossless Audio Codec (FLAC)",
    "Quellen zur Ampel": "lzv.nrw: https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Audio",
    "Datenformate": "MP4 Advanced Audio Coding",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Audio",
    "Datenformate": "MP3 (*.mp3)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Audio",
    "Datenformate": "Präsentationsformat: MPEG-2 Audiolayer III (MP3)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "Codec FFV1 / Container MKV",
    "Quellen zur Ampel": "lzv.nrw: https://www.lzv.nrw/dateiformate/?mtm_campaign=tafellaunch&mtm_medium=social",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "TIFF mit FFV1 in Matroshka codiert",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "MPEG-4 Moving Picture Experts Group Standard",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "Präsentationsformat: MP4 (MPEG-4, part 14)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "MPEG-2 (*.mpg,*.mpeg)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "MOV QuickTime Movie",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "AVI Audio Video Interleave",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "WMV Windows Media Video",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "MJPEG2000 Moving Picture Experts Group Motion JPEG 2000",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "orange",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "DPX Digital Picture Exchange, SMPTE 268M-2003, v 2.0",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Video/Film",
    "Datenformate": "MXF Material Exchange Format, SMPTE 377M",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "3D",
    "Datenformate": "gITF Graphics Language Transmission Format",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "3D",
    "Datenformate": "OBJ Wavefront Object",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "3D",
    "Datenformate": "X3D Extensible 3D",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "3D",
    "Datenformate": "Präsentationsformat: glTF, X3D, OBJ",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "3D",
    "Datenformate": "COLLADA COLLAborative Design Activity",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "rot",
    "Kategorie": "multimedia"
  },
  {
    "Dateiart": "Tabellen",
    "Datenformate": "Extensible Markup Language (XML) 1.1, mit XML Schema Definition (XSD)",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Tabellen",
    "Datenformate": "CSV Comma-Separated Values",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Tabellen",
    "Datenformate": "XLSX Excel (Containerformat)",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "orange",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Tabellen",
    "Datenformate": "OpenDocument Formate (*.odm, *.odt, *.odg, *.odc, *.odf)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Tabellen",
    "Datenformate": "XLS, XLSB Excel (binäre Formate)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Datenbanken",
    "Datenformate": "SIARD Software Independent Archival of Relational Database",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Datenbanken",
    "Datenformate": "SQL Structured Query Language",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Datenbanken",
    "Datenformate": "MS Access 2010/2016",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "rot",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Datenbanken",
    "Datenformate": "Export und externe Speicherung der Datenbankinhalte empfohlen, z. B. als XML, CSV, JSON mit Entitäten-Relationen-Diagramm (ERD)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "Vektordaten: Environmental Systems Research Institute ESRI Shapefile",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "ESRI ArcGIS/ARCView ShapeFile",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "OGC GeoPackage (OpenSource)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "Rasterbilddaten als Geo-TIFF",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "ESRI World-File (Rastergrafik)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "KML Keyhole Mark-Up Language",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "orange",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "GML Geography Markup Language",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "Längen- und Breitenangaben (alternativ)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Geoinformationssysteme (GIS)",
    "Datenformate": "Rasterdaten: Open Geospatial Consortium GeoTIFF",
    "Quellen zur Ampel": "National Archives (USGS): https://www.archives.gov/records-mgmt/policy/transfer-guidance-tables.html#geospatialformats",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Webseiten",
    "Datenformate": "HTML5 Hypertext Markup Language",
    "Quellen zur Ampel": "kost-ceco: https://kost-ceco.ch/cms/kad_image_de.html",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Webseiten",
    "Datenformate": "XHTML Extensible Hypertext Markup Language",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Webseiten",
    "Datenformate": "Resource Description Framework in Attributes (RDFa) für das Einbetten von RDF-Statements in HTML und XHTML",
    "Quellen zur Ampel": "NFDI4Culture: https://docs.nfdi4culture.de/ta2-fair-handreichung/empfehlungen-dateiformate",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Statistik",
    "Datenformate": "R",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "orange",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Webarchiv",
    "Datenformate": "WARC-Format (Web Archive Format)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Webarchiv",
    "Datenformate": "HTML + CSS (Hyper Text Markup Language + Cascading Style Sheets)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bagit",
    "Datenformate": "Bagit (File Packaging Format)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bagit",
    "Datenformate": "ZIP-Format (PKZip)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bagit",
    "Datenformate": "GZIP (GNU Zip)",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bagit",
    "Datenformate": "TAR",
    "Quellen zur Ampel": "Herder-Institut Marburg: https://zenodo.org/records/18389871",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Rohdaten und Workspace",
    "Datenformate": "S-Plus (*.sdd) am ehesten als Text-Dateien",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Rohdaten und Workspace",
    "Datenformate": "Matlab *.mat am ehesten in HDF5 Format speichern. Nichttriviale Matlab *.mat ASCII Files vermeiden, denn sie können mit load nicht gelesen werden.",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "orange",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Rohdaten und Workspace",
    "Datenformate": "NC, CDF Network Common Data Format oder NetCDF",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Rohdaten und Workspace",
    "Datenformate": "H5, HDF5, HE5 Hierarchical Data Format (HDF5)",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Rohdaten und Workspace",
    "Datenformate": "Binäre Dateien wie veraltete Matlab Dateien *.mat (binär), R Dateien *.RData",
    "Quellen zur Ampel": "ETH Zürich: https://unlimited.ethz.ch/spaces/DD/pages/194127898/Archivtaugliche+Dateiformate",
    "Ampel": "rot",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bibilographische Daten (Zitationsformate)",
    "Datenformate": "allegro",
    "Quellen zur Ampel": "Verbundzentrale des GBV: https://format.gbv.de/application/bibliographic",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bibilographische Daten (Zitationsformate)",
    "Datenformate": "CSL-JSON",
    "Quellen zur Ampel": "Verbundzentrale des GBV: https://format.gbv.de/application/bibliographic",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bibilographische Daten (Zitationsformate)",
    "Datenformate": "BibJSON",
    "Quellen zur Ampel": "Verbundzentrale des GBV: https://format.gbv.de/application/bibliographic",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bibilographische Daten (Zitationsformate)",
    "Datenformate": "BibTeX",
    "Quellen zur Ampel": "Verbundzentrale des GBV: https://format.gbv.de/application/bibliographic",
    "Ampel": "grün",
    "Kategorie": "data"
  },
  {
    "Dateiart": "Bibilographische Daten (Zitationsformate)",
    "Datenformate": "CFF Citation File Format",
    "Quellen zur Ampel": "Verbundzentrale des GBV: https://format.gbv.de/application/bibliographic",
    "Ampel": "grün",
    "Kategorie": "data"
  }
    ]

# 2. Create vector store
embeddings = HuggingFaceEmbeddings()
vectordb = Chroma.from_documents(docs, embeddings)

# 3. Query
def ask_question(question):
    docs = vectordb.similarity_search(question, k=3)
    # Feed to LLM with context
    return answer

# Test
print(ask_question("What format is best for archiving PDFs?"))