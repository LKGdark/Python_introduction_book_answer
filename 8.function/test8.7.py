def make_album(singer_name,album_name,num = None):
    """打印歌手的专辑和其他内容"""
    album = {
        's_name':singer_name,
        'a_name':album_name,
    }
    if num:
        album['num'] = num
    return album

print(f"{make_album('xingyeai','asdasdsda',111)}")
print(f"{make_album('xi','asdasd',)}")
print(f"{make_album('yeai','ada')}")