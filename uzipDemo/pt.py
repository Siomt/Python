import zipfile
try:
  zFile=zipfile.ZipFile("file.zip")
  zFile.extractall(pwd="secret".encode('ascii'))
  print("sucessd")
except Exception:
  print("fale")
  pass