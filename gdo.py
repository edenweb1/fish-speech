import gdown
import zipfile
import os

# Lien de partage Google Drive (exemple)
url = "https://drive.google.com/uc?id=1S-984ImApWtKSZ4VoGDBmTeQc-fMHWyV"

# Nom du fichier local téléchargé
output = "fichier.zip"

# Télécharger
gdown.download(url, output, quiet=False)
current_dir = os.getcwd()

# Décompresser
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall(current_dir)

print("Fichier téléchargé et décompressé !")