def download_images(phrase):
  from google_images_search import GoogleImagesSearch
  gis = GoogleImagesSearch('AIzaSyA7ixP7OvgePvP1SRkhWbDod7U-grzry58', '256661aff3bb340bb')

  _search_params = {
      'q': phrase,
      'num': 5,
      'fileType': 'jpg',
      'rights': 'cc_publicdomain',
      'safe': 'high', ##
      'imgType': 'imgTypeUndefined', ##
      'imgSize': 'medium', ##
      'imgDominantColor': 'imgDominantColorUndefined', ##
      'imgColorType': 'color' ##
  }

  result = []
  try:
    import os
    import pathlib
    path = phrase + "-images"
    folder = pathlib.Path(path)
    if not folder.exists():
      os.mkdir(path)
    gis.search(search_params=_search_params, path_to_dir=path, width=300, height=300)
    for image in gis.results():
      result.append(image.url)
  except:
    pass

  return result